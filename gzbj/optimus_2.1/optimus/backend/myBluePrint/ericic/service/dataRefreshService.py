import uuid
import json
from flask import g
from concurrent.futures import ThreadPoolExecutor, as_completed
from backend.myBluePrint.ericic.baseDao.openstackHostDao import OpenstackHostDao
from backend.myBluePrint.ericic.common.call_script import OpenstackViewScriptHandler


class DataRefreshService:
    pool_num = 10

    @classmethod
    def update_openstack_host(cls):
        data_center_list = OpenstackHostDao.get_all_dc()
        # lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid
        tpool_param_list, res_list = [], []
        for item in data_center_list:
            jid = g.r_id
            if item.mode:
                cid = item.id
                lcm_ip = item.lcm_ip
                lcm_user = item.lcm_user
                lcm_pwd = item.lcm_pwd
                lcmrc_dir = item.lcmrc_dir
                openstackrc_dir = item.openstackrc_dir
                system_name = item.system_name
                tpool_param_list.append((lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid, jid))

        # tpool_param_list = [
        #     ('_lcm_ip', '_lcm_user', '_lcm_pwd', '_lcmrc_dir', '_openstackrc_dir', '_system_name', '1', g.r_id),
        #     ('_lcm_ip', '_lcm_user', '_lcm_pwd', '_lcmrc_dir', '_openstackrc_dir', '_system_name', '2', g.r_id)
        # ]

        def call_view_script_handler(_lcm_ip, _lcm_user, _lcm_pwd, _lcmrc_dir, _openstackrc_dir, _system_name, _cid, j):
            script_caller = OpenstackViewScriptHandler(_lcm_ip, _lcm_user, _lcm_pwd, job_id=j)
            _json_output = script_caller.call_cee_info_collect(_lcmrc_dir, _openstackrc_dir, _system_name, _cid)
            # test_file = 'jjj.json' if _cid == '1' else 'fake_data3.json'
            # with open(test_file,) as f:
            #     _json_output = f.read()
            return _cid, _json_output

        with ThreadPoolExecutor(max_workers=cls.pool_num) as executor:
            run_folder = {executor.submit(call_view_script_handler, *i): i for i in tpool_param_list}
            for future in as_completed(run_folder):
                this_cid, this_json_output = future.result()
                if this_cid and this_json_output:
                    res_list.append((this_cid, this_json_output))

        out_put_dicts = dict()
        for item in res_list:
            cid, json_output = item
            json_obj = json.loads(json_output)
            out_put = cls.output_format(cid, json_obj)
            out_put_dicts[cid] = out_put

        OpenstackHostDao.refresh_db(out_put_dicts)

    @classmethod
    def output_format(cls, cid, json_output):
        flavor_info = json_output['flavor']
        flavor_formated = cls._format_flavor(flavor_info, cid)
        hosts_info = json_output['compute_info']
        host_formated = cls._format_host(hosts_info, cid)
        az_ha_info = json_output['aggregate']
        host_formated = cls._fill_host_info(host_formated, az_ha_info)
        vm_info = json_output['vm_info']
        vm_formated = cls._format_vm(vm_info, cid)
        tenants = json_output['tenants']
        tenant_formated = cls._format_tenant(tenants, cid)
        volume_info = json_output['volume']
        volume_formated = cls._format_volume(volume_info, cid)
        vm_formated = cls._fill_vm_info(vm_formated, flavor_formated, tenant_formated, host_formated)

        flavor_res = [flavor for uid, flavor in flavor_formated.items()]
        host_res = [host for uid, host in host_formated.items()]
        vm_res = [vm for uid, vm in vm_formated.items()]
        tenant_res = [tenant for uid, tenant in tenant_formated.items()]
        volume_res = [volume for _, volume in volume_formated.items()]

        return dict(flavor=flavor_res, host=host_res, vm=vm_res, tenant=tenant_res, volume=volume_res)

    @classmethod
    def _fill_volume(cls, volume_formated, vm_formated):
        for volume_uuid, volume_item in volume_formated.items():
            vm_uuid = volume_item['vm_id']
            if vm_uuid:
                volume_item['vm_id'] = vm_formated[vm_uuid]['id']

    @classmethod
    def _format_volume(cls, volume_info, cid):
        res_dict = dict()
        for volume in volume_info:
            this_info_dict = dict()
            this_info_dict['_id'] = uuid.uuid4().hex
            this_info_dict['uuid'] = volume['ID']
            this_info_dict['name'] = volume['Name']
            this_info_dict['status'] = volume['Status']
            this_info_dict['size'] = volume['Size']
            this_info_dict['type'] = volume['Type'] if volume['Type'] else ''
            this_info_dict['bootable'] = False if volume['Bootable'] == 'false' else True
            this_info_dict['vm_id'] = None
            for attached_item in volume['Attached to']:
                this_info_dict['vm_id'] = attached_item['server_id']
                # this is vm's uuid and it needs to be translated into vm's id generated by system
                break
            this_info_dict['data_center_id'] = cid
            res_dict[volume['ID']] = this_info_dict
        return res_dict

    @classmethod
    def _format_tenant(cls, tenant_info, cid):
        res_dict = dict()
        for tenant in tenant_info:
            this_info_dict = dict()
            this_info_dict['_id'] = uuid.uuid4().hex
            this_info_dict['uuid'] = tenant['ID']
            this_info_dict['name'] = tenant['Name']
            this_info_dict['data_center_id'] = cid
            res_dict[tenant['ID']] = this_info_dict
        return res_dict

    @classmethod
    def _fill_vm_info(cls, vm_info, flavor_dict, tenant_dict, host_dict):
        for vm_uuid, vm_item in vm_info.items():
            flavor_uuid = vm_item['flavor_id']
            host_name = vm_item['host_id']
            tenant_uuid = vm_item['tenant_id']
            vm_item['flavor_id'] = flavor_dict[flavor_uuid]['_id']
            vm_item['host_id'] = host_dict[host_name]['_id'] if host_name != 'None' else 'None'
            vm_item['tenant_id'] = tenant_dict[tenant_uuid]['_id']
        return vm_info

    @classmethod
    def _format_vm(cls, vm_info, cid):
        res_dict = dict()

        def _power_state_trans(_power_state):
            if int(_power_state) == 1:
                _power_state = 'Running'
            elif int(_power_state) == 0:
                _power_state = 'NOSTATE'
            elif int(_power_state) == 4:
                _power_state = 'Shutdown'
            else:
                _power_state = 'NaN'
            return _power_state

        for item in vm_info:
            this_info_dict = dict()
            this_info_dict['_id'] = uuid.uuid4().hex
            this_info_dict['uuid'] = item['id']
            this_info_dict['name'] = item['name']
            this_info_dict['status'] = item['status']
            this_info_dict['power_state'] = _power_state_trans(item['power_state'])
            this_info_dict['create_time'] = item['created']
            this_info_dict['networks'] = item['networks']
            this_info_dict['flavor_id'] = item['flavor']
            # this is flavor's uuid and it needs to be translated into flavor's id generated by system
            this_info_dict['tenant_id'] = item['tenant_id']
            # this is tenant's uuid and it needs to be translated into tenant's id generated by system
            this_info_dict['host_id'] = item['host']
            # this is host_name and it needs to be translated into host id
            this_info_dict['data_center_id'] = cid
            this_info_dict['instance_name'] = item['instance_name']
            res_dict[item['id']] = this_info_dict
        return res_dict

    @classmethod
    def _format_flavor(cls, flavor_info, cid):
        res_dict = dict()
        for flavor in flavor_info:
            this_info_dict = dict()
            this_info_dict['_id'] = uuid.uuid4().hex
            this_info_dict['uuid'] = flavor['ID']
            this_info_dict['vcpu'] = flavor['VCPUs']
            this_info_dict['memory'] = flavor['RAM']
            this_info_dict['disk'] = flavor['Disk']
            this_info_dict['data_center_id'] = cid
            res_dict[flavor['ID']] = this_info_dict
        return res_dict

    @classmethod
    def _format_host(cls, host_info, cid):
        res_dict = dict()
        for host in host_info:
            this_info_dict = dict()
            this_info_dict['_id'] = uuid.uuid4().hex
            this_info_dict['name'] = host['Hypervisor Hostname']
            this_info_dict['host_aggregate'] = None
            this_info_dict['availability_zone'] = None
            this_info_dict['compute_state'] = host['State']
            this_info_dict['total_cpu'] = host['vCPUs']
            this_info_dict['free_cpu'] = host['vCPUs'] - host['vCPUs Used']
            this_info_dict['total_memory'] = host['Memory MB']
            this_info_dict['free_memory'] = host['Memory MB'] - host['Memory MB Used']
            this_info_dict['total_disk'] = host['Total Disk']
            this_info_dict['free_disk'] = host['Free Disk']
            this_info_dict['data_center_id'] = cid
            res_dict[host['Hypervisor Hostname']] = this_info_dict
        return res_dict

    @classmethod
    def _fill_host_info(cls, host_info, ha_az_info):
        # format ha az
        ha_az_dict = dict()
        for item in ha_az_info:
            az = item['availability_zone']
            ha = item['name']
            host_names = item['hosts']
            for host in host_names:
                ha_az_dict[host] = dict(availability_zone=az, host_aggregate=ha)
        # fill host infos
        for host_name, host_dict in host_info.items():
            host_dict['host_aggregate'] = ha_az_dict.get(host_name, dict(host_aggregate=None))['host_aggregate']
            host_dict['availability_zone'] = ha_az_dict.get(host_name, dict(availability_zone=None))[
                'availability_zone']
        return host_info
