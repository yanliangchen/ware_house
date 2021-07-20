import time
import json
import uuid
import paramiko
from flask import g
from config import SSH_TIMEOUT
from backend.common.loghandler import ServiceLog
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel
from backend.myBluePrint.ericic.model.hostModel import HostInfo
from backend.myBluePrint.ericic.model.vmHostView import VmHostView
from sqlalchemy.orm.attributes import InstrumentedAttribute


class VmService:

    # todo : the refresh function's granularity is too huge, maybe it needs to add a lock
    # @classmethod
    # def get_vm_info(cls, offset, limit, column_list, refresh, query_dict, sort, order, cid):
    #     total_num = VmHostView.count_by_cid(cid)
    #     if not cid:
    #         return dict(res=list(), total_num=total_num)
    #     if not refresh:
    #         # generate default column list from the cls' attribute, where the type of the attr is InstrumentedAttribute
    #         default_column_list = list()
    #         attributes_dict = VmHostView.__dict__
    #         for k, v in attributes_dict.items():
    #             if type(v) == InstrumentedAttribute:
    #                 default_column_list.append(k)
    #         column_list = [i for i in column_list if i in default_column_list]
    #         if len(column_list) == 0:
    #             column_list = ['uuid', 'name', 'status', 'power_state', 'host', 'networks', 'vcpu', 'memory', 'disk']
    #         if 'id' not in column_list:
    #             column_list.append('id')
    #         format_query = dict()
    #         for column in column_list:
    #             if column == 'id' or column == 'host_id' or column == 'timestamp':
    #                 continue
    #             q = query_dict.get(column, list())
    #             if len(q):
    #                 format_query[column] = q
    #         format_query['data_center_id'] = (cid, )
    #         res = VmHostView.split_data_by_query(column_list, format_query, offset, limit, sort, order)
    #         response_data = list()
    #         for item in res:
    #             info_dict = dict()
    #             for column in column_list:
    #                 db_entity_attr_val = getattr(item, column)
    #                 info_dict[column] = db_entity_attr_val
    #             response_data.append(info_dict)
    #         return dict(res=response_data, total_num=total_num)
    #     else:
    #         cls.refresh_vm_info(cid)
    #         return cls.get_vm_info(offset, limit, column_list, False, query_dict, sort, order, cid)

    @classmethod
    def refresh_vm_info(cls, cid):
        # import json
        # with open('backend/myBluePrint/ericic/fake_data.json') as f:
        #     demo_data = f.read()
        # info_data = json.loads(demo_data)
        info_data = cls._collect_ericic_data(cid)
        if info_data:
            formated_data = cls._format_input(info_data, cid)
            cls._insert_vm_info(formated_data, cid)

    @classmethod
    def _collect_ericic_data(cls, cid):
        data_center_obj = DataCenterModel.get_one_by_id(cid)
        if data_center_obj:
            lcm_ip = data_center_obj.lcm_ip
            lcm_user = data_center_obj.lcm_user
            lcm_pwd = data_center_obj.lcm_pwd
            ssh = paramiko.SSHClient()
            try:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(lcm_ip, 22, lcm_user, lcm_pwd, timeout=SSH_TIMEOUT)
                paramiko.SFTPClient.from_transport(ssh.get_transport())
                sftp = ssh.open_sftp()
                try:
                    # todo: to package the ssh exec_command function, because the service_log invade the service code so much
                    job_id = g.r_id
                    ssh.exec_command('mkdir %s' % job_id)
                    ServiceLog.info('%s - call script - mkdir' % job_id)
                    sftp.put('FilesFolder/ericic/script/infocollect.tar', '%s.tar' % job_id)
                    ServiceLog.info('%s - call script - scp' % job_id)
                    ssh.exec_command('tar -xvf %s.tar -C %s' % (job_id, job_id))
                    ServiceLog.info('%s - call script - unzip' % job_id)
                    ssh.exec_command('cd %s/infocollect; python get_node_info.py -l /home/ceeinfra/ceelcmrc -s DL33 -o /var/lib/cee/system/DL33/system/openstack/admin-openrc.sh' % job_id)
                    ServiceLog.info('%s - call script - run get_node_info.py' % job_id)
                    ssh.exec_command('cd %s/infocollect; python test_case/test_optimue_001.py' % job_id)
                    ServiceLog.info('%s - call script - run test_optimue_001.py' % job_id)
                    output = ssh.exec_command('cat /tmp/optimus_vms_usage')[1]
                    output = output.read()
                    ServiceLog.info('%s - call script - get_result - %s' % (job_id, output))
                    data = json.loads(str(output, 'utf-8'))
                    ssh.exec_command('rm -rf %s*' % job_id)
                    ServiceLog.info('%s - call script - rm files' % job_id)
                    return data
                finally:
                    sftp.close()
            finally:
                ssh.close()
        else:
            return None

    @classmethod
    def _format_input(cls, info, cid):
        flavor_list = info['flavor']
        vm_info_list = info['vm_info']
        aggregate_list = info['aggregate']
        compute_info_list = info['compute_info']

        timestamp = int(time.time())
        aggregate_dict = dict()
        for aggregate in aggregate_list:
            for host_name in aggregate['hosts']:
                aggregate_dict[host_name] = {
                    'availability_zone': aggregate['availability_zone'],
                    'high_availability': aggregate['name']
                }

        flavor_dict = dict()
        for flavor in flavor_list:
            fid = flavor['ID']
            flavor_dict[fid] = {
                'disk': flavor['Disk'],
                'memory': flavor['RAM'],
                'vcpu': flavor['VCPUs']
            }

        format_compute_dict = dict()
        for compute in compute_info_list:
            name = compute['Hypervisor Hostname']
            compute_state = True if compute['State'] == 'up' else False
            format_compute_dict[name] = {
                '_id': str(uuid.uuid4().hex),
                'name': name,
                'compute_state': compute_state,
                'data_center_id': cid,
                'high_availability': aggregate_dict.get(name, dict()).get('high_availability'),
                'availability_zone': None,
                'timestamp': timestamp
            }

        vm_dict = dict()
        for vm in vm_info_list:
            uid = vm['id']
            vm_name = vm['name']
            status = vm['status']
            power_state = vm['power_state']
            created_time = vm['created']
            networks = vm['networks'].split(',')
            flavor_info = flavor_dict.get(vm['flavor'], dict())
            if int(vm.get('power_state')) == 1:
                power_state = 'Running'
            elif int(vm.get('power_state')) == 0:
                power_state = 'NOSTATE'
            elif int(vm.get('power_state')) == 4:
                power_state = 'Shutdown'
            vm_dict[uid] = {
                '_id': str(uuid.uuid4().hex),
                'name': vm_name,
                'uuid': uid,
                'status': status,
                'power_state': power_state,
                'vcpu': flavor_info.get('vcpu'),
                'memory': flavor_info.get('memory'),
                'disk': flavor_info.get('disk'),
                'create_time': created_time,
                'networks': networks,
                'timestamp': timestamp,
                'host_id': format_compute_dict[vm['host']]['_id']
            }
            format_compute_dict[vm['host']]['availability_zone'] = vm['az']
        return dict(host_info=format_compute_dict, vm_info=vm_dict)

    @classmethod
    def _insert_vm_info(cls, info, cid):
        host_info_dict = info['host_info']
        vm_info_dict = info['vm_info']
        HostInfo.refresh_infos(host_info_dict, vm_info_dict, cid)
