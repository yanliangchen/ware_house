import os
import time
import json
from flask import g, request
from functools import wraps
from multiprocessing import Process, Event
from backend.common.redisHandler import LOCK_RDS, CACHE_RDS
from backend.common.scriptHandler import ScriptHandler
from backend.common.loghandler import LockLog
from backend.myException.myExecption import MyRuntimeError
from backend.myBluePrint.ericic.baseDao.vmApiDao import VmApiDao
from backend.myBluePrint.ericic.model.hostModelView import HostModelView
from backend.myBluePrint.ericic.model.vmHostView import VmHostView
from backend.myBluePrint.ericic.model.vmModelView import VmModelView
from backend.myBluePrint.ericic.common.upload_api import upload_api
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel


class VmLock:
    lock_expire = 10

    RELEASE_LUA_SCRIPT = """
        if redis.call("get",KEYS[1]) == ARGV[1] then
            return redis.call("del",KEYS[1])
        else
            return 0
        end
    """

    @classmethod
    def script_lock(cls, func):
        @wraps(func)
        def inner(*args, **kwargs):
            _cls, lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid = args
            key = cid
            # noinspection PyBroadException
            try:
                request_id = g.r_id
                refresh = request.args.get('refresh', 'false')
                refresh = True if refresh.lower() == 'true' else False
            except Exception:
                request_id = os.getpid()
                refresh = False
            lock_event = Event()
            p = Process(target=cls.lock_watcher, args=(lock_event, key))
            p.daemon = True
            try:
                LockLog.info('try to get lock -- key : %s ' % key)
                if not refresh:
                    if not LOCK_RDS.set(key, request_id, nx=True, ex=cls.lock_expire):
                        LockLog.info('failed to get lock -- key : %s ' % key)
                        loop = all_time = 0
                        while LOCK_RDS.get(key):
                            pending_time = cls.lock_expire / 2 - (loop / 10) * cls.lock_expire
                            if pending_time >= (cls.lock_expire / 3):
                                pending_time = pending_time
                            else:
                                pending_time = cls.lock_expire / 3
                            all_time += pending_time
                            if pending_time > cls.lock_expire * 1.5:
                                raise MyRuntimeError('resource overload, try again later', 503)
                            time.sleep(pending_time)
                            loop += 1
                        LockLog.info('detect the lock no longer exist -- key : %s ' % key)
                        return dict()
                else:
                    all_time = 0
                    while not LOCK_RDS.set(key, request_id, nx=True, ex=cls.lock_expire):
                        if all_time > cls.lock_expire * 1.5:
                            raise MyRuntimeError('resource overload, try again later', 503)
                        time.sleep(cls.lock_expire / 8)
                        all_time += cls.lock_expire / 8
                        LockLog.info('retry ! to get lock -- key : %s ' % key)
                LockLog.info('success to get lock -- key : %s ' % key)
                try:
                    p.start()
                    LockLog.info('func start')
                    res = func(*args, **kwargs)
                    LockLog.info('func end')
                finally:
                    lock_event.set()
                    LockLog.info('success to set the event -- key : %s ' % key)
                    del_script = LOCK_RDS.register_script(cls.RELEASE_LUA_SCRIPT)
                    if del_script(keys=[key, ], args=[request_id, ]):
                        LockLog.info('success to delete  lock -- key : %s ' % key)
                    else:
                        LockLog.info('failed to delete  lock -- key : %s ' % key)
                return res
            finally:
                LOCK_RDS.close()

        return inner

    @classmethod
    def lock_watcher(cls, lock_event, key):
        LockLog.info('watcher start -- key : %s ' % key)
        time.sleep(3 * cls.lock_expire / 4)
        while not lock_event.is_set():
            LOCK_RDS.expire(key, cls.lock_expire)
            LockLog.info('add expire key : %s' % key)
            time.sleep(3 * cls.lock_expire / 4)
        LockLog.info('exit watcher -- key : %s ' % key)


class VmCache:
    script_name = 'infocollect-Ericic4ceeNext'

    @classmethod
    def vm_view_cache(cls, func):
        @wraps(func)
        def inner(*args, **kwargs):
            _cls, offset, limit, column_list, query, sort, order, cid = args
            if not cid:
                return dict(res=list(), total_num=0)
            dc_obj = DataCenterModel.get_one_by_id(cid)
            if not dc_obj:
                return dict(res=list(), total_num=0)
            if not dc_obj.mode:
                return func(*args, **kwargs)
            lcm_ip = dc_obj.lcm_ip
            lcm_user = dc_obj.lcm_user
            lcm_pwd = dc_obj.lcm_pwd
            lcmrc_dir = dc_obj.lcmrc_dir
            openstackrc_dir = dc_obj.openstackrc_dir
            system_name = dc_obj.system_name
            refresh = request.args.get('refresh', 'false')
            refresh = True if refresh.lower() == 'true' else False
            if refresh:
                cls.gen_data_by_scripts(lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid)
            else:
                if not CACHE_RDS.get('dc_cache:%s' % cid):
                    cls.gen_data_by_scripts(lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid)
            return func(*args, **kwargs)

        return inner

    @classmethod
    @VmLock.script_lock
    def gen_data_by_scripts(cls, lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid):
        job_id = g.r_id
        script_obj = ScriptHandler(lcm_ip, lcm_user, lcm_pwd)
        script_obj.execute_cmd('mkdir /tmp/%s' % job_id)
        script_obj.scp_file('FilesFolder/ericic/script/%s.tar' % cls.script_name, '/tmp/%s.tar' % job_id)
        script_obj.execute_cmd('tar -xvf /tmp/%s.tar -C /tmp/%s' % (job_id, job_id))
        cmd_path = 'cd  /tmp/%s/%s' % (job_id, cls.script_name)
        cmd = 'python get_node_info.py -l %s -s %s -o %s' % (lcmrc_dir, system_name, openstackrc_dir)
        script_obj.execute_cmd('%s; %s' % (cmd_path, cmd))
        script_obj.execute_cmd('%s; python test_case/test_optimue_001.py -i %s -n %s' % (cmd_path, job_id, cid))
        # json_output = script_obj.execute_cmd('%s; cat output/%s.json' % (cmd_path, job_id))
        # json_output = script_obj.execute_cmd('%s; cat output/%s.json' % (cmd_path, job_id))
        target = '/tmp/%s/%s/output/%s.json' % (job_id, cls.script_name, job_id)
        aim = 'FilesFolder/ericic/script_output/%s.json' % job_id
        script_obj.get_file(target, aim)
        with open(aim) as f:
            json_output = f.read()
        target = '/tmp/%s/%s/output/%s_%s.xlsx' % (job_id, cls.script_name, cid, job_id)
        aim = 'FilesFolder/ericic/script_output/%s_%s.xlsx' % (cid, job_id)
        script_obj.get_file(target, aim)
        VmApiDao.delete_all_relate_info(cid)
        upload_api(json.loads(json_output), cid)
        try:
            p = CACHE_RDS.pipeline()
            p.set('dc_cache:%s' % cid, job_id, ex=60 * 5)
            p.set('excel_cache:%s' % cid, job_id)
            p.execute()
            p.close()
        finally:
            script_obj.execute_cmd('rm -rf /tmp/%s*' % job_id)
            CACHE_RDS.close()
            del script_obj

    #
    # @classmethod
    # def _inner_cache(cls, cid):
    #     import json
    #     dc_obj = DataCenterModel.get_one_by_id(cid)
    #     if dc_obj:
    #         lcm_user = dc_obj.lcm_user
    #         lcm_pwd = dc_obj.lcm_pwd
    #         lcm_ip = dc_obj.lcm_ip
    #         # get data by scripts
    #         ScriptHandler(lcm_ip, lcm_user, lcm_pwd)
    #         time.sleep(30)
    #         with open('backend/myBluePrint/ericic/fake_data3.json') as f:
    #             demo_data = f.read()
    #         info_data = json.loads(demo_data)
    #         # insert the data into db
    #         cls._insert_data_from_json(info_data, cid)


class VmService:
    # host_column = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone',
    #                'cpu_percent', 'memory_percent', 'disk_percent']
    host_column = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone', ]
    vm_column = ['uuid', 'name', 'status', 'power_state', 'networks', 'volume', 'create_time', 'vcpu', 'memory', 'disk',
                 'tenant']
    vm_query = ['name', 'status', 'power_state', 'networks', 'tenant', ]
    host_query = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone']
    vm_sort = ['vcpu', 'memory', 'disk']
    host_sort = []

    # Tips1：customized column show contains 2 parts -- vm info , host info
    # vm includes:uuid, name, status, power_state, network, flavor(vcpu, memory, disk), volume, create_time, tenant
    # host includes:host，compute_state, infra_resource(cpu_percent, memory_percent,disk_percent),
    #   cee_version, host_aggregate, availability_zone

    # Tips2: the support querying column in each part：
    # vm:name, status, power_status, network, tenant,
    # host:host, compute_state, cee_version, host_aggregate, availability_zone

    # Tips3: the sorted column supported in each part：
    # vm: vcpu(flavor), memory(flavor), disk(flavor)
    # host: null

    @classmethod
    @VmCache.vm_view_cache
    def service_switch(cls, offset, limit, column_list, query, sort, order, cid):
        try:
            limit = int(limit)
            offset = int(offset)
        except TypeError:
            limit = 50
            offset = 0
        if not cid:
            return dict(res=list(), total_num=0)
        # change the high level column name into low level column name
        # if 'infra_resource' in column_list:
        #     column_list.remove('infra_resource')
        #     column_list.extend(['cpu_percent', 'memory_percent', 'disk_percent'])
        if 'flavor' in column_list:
            column_list.remove('flavor')
            column_list.extend(['vcpu', 'memory', 'disk'])
        # judge which db does the api get data from
        host_switch = False
        vm_switch = False
        if len(column_list) == 0:
            column_list = ['uuid', 'name', 'status', 'power_state', 'networks', 'flavor', 'host', ]
        for host_c in cls.host_column:
            if host_c in column_list:
                host_switch = True
                break
        for vm_c in cls.vm_column:
            if vm_c in column_list:
                vm_switch = True
                break
        if (host_switch and vm_switch) or (not host_switch and not vm_switch):
            db_view_entity = VmHostView
            default_column = (cls.host_column + cls.vm_column)
            host_id_column = 'host_id'
            vm_id_column = 'vm_id'
            sort_list = [sort, 'vm_id']
        elif host_switch:
            db_view_entity = HostModelView
            default_column = cls.host_column
            sort_list = [sort, 'host_id']
            host_id_column = 'host_id'
            vm_id_column = None
        elif vm_switch:
            db_view_entity = VmModelView
            default_column = cls.vm_column
            host_id_column = 'host_id'
            vm_id_column = 'id'
            sort_list = [sort, 'id']
        else:
            raise MyRuntimeError('unexpect service condition', 400)
        column_list = [i for i in column_list if i in default_column]
        format_query = dict()
        for column in column_list:
            if column not in cls.host_query + cls.vm_query:
                continue
            q = query.get(column, list())
            if len(q):
                format_query[column] = q
        format_query['data_center_id'] = (cid,)
        response_data = list()
        total_num = db_view_entity.count_data_by_query(format_query)
        column_list.append(host_id_column)
        if vm_id_column:
            column_list.append(vm_id_column)
        res = db_view_entity.split_data_by_query(column_list, format_query, offset, limit, sort_list, order)
        for item in res:
            info_dict = dict()
            for column in column_list:
                if column == host_id_column:
                    db_entity_attr_val = getattr(item, column)
                    info_dict['host_id'] = db_entity_attr_val
                elif column == vm_id_column and vm_id_column:
                    db_entity_attr_val = getattr(item, column)
                    info_dict['vm_id'] = db_entity_attr_val
                elif column == 'volume':
                    info_dict['volume'] = list()
                else:
                    db_entity_attr_val = getattr(item, column)
                    info_dict[column] = db_entity_attr_val
            response_data.append(info_dict)
        if vm_id_column and 'volume' in column_list:
            response_data = cls._fill_volume_info(response_data, 'vm_id')
        return dict(res=response_data, total_num=total_num)

    @classmethod
    def _fill_volume_info(cls, response_data, vm_id_column):
        vm_id_list = [i[vm_id_column] for i in response_data]
        volume_info = VmApiDao.get_volume_by_vm_ids(vm_id_list)
        for item in response_data:
            vm_id = item[vm_id_column]
            if not vm_id:
                continue
            volume_entity_list = volume_info[vm_id]
            for volume_entity in volume_entity_list:
                volume_info_dict = dict()
                volume_info_dict['name'] = volume_entity.name
                volume_info_dict['status'] = volume_entity.status
                volume_info_dict['size'] = volume_entity.size
                volume_info_dict['type'] = volume_entity.type
                volume_info_dict['bootable'] = volume_entity.bootable
                item['volume'].append(volume_info_dict)
        return response_data
