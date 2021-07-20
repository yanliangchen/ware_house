from flask import request
from backend.myBluePrint.ericic.service.vmService2 import VmCache
from backend.common.redisHandler import CACHE_RDS
from backend.myBluePrint.ericic.model.hostModelView import HostModelView
from backend.myBluePrint.ericic.baseDao.hostApiDao import HostApiDao
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel


class HostCache:

    @classmethod
    def dec_info_cache(cls, func):
        def inner(*args, **kwargs):
            _cls, cid, sort, order, query, column_list, offset, limit = args
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
                VmCache.gen_data_by_scripts(lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid)
                return func(*args, **kwargs)
            if CACHE_RDS.get('dc_cache:%s' % cid):
                return func(*args, **kwargs)
            else:
                VmCache.gen_data_by_scripts(lcm_ip, lcm_user, lcm_pwd, lcmrc_dir, openstackrc_dir, system_name, cid)
                return func(*args, **kwargs)

        return inner


class HostService:
    # host_column = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone',
    #                'cpu_percent', 'memory_percent', 'disk_percent']

    host_column = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone',]
    vm_column = ['uuid', 'name', 'status', 'power_state', 'networks', 'volume', 'create_time', 'vcpu', 'memory', 'disk',
                 'tenant']
    host_query = ['host', 'compute_state', 'cee_version', 'host_aggregate', 'availability_zone']

    @classmethod
    @HostCache.dec_info_cache
    def get_host_info(cls, cid, sort, order, query, column_list, offset, limit):
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
        column_list = [i for i in column_list if i in cls.vm_column + cls.host_column]
        host_columns = [i for i in column_list if i in cls.host_column]
        vm_columns = [i for i in column_list if i in cls.vm_column]
        if not len(host_columns):
            host_columns = cls.host_column
        if not len(column_list):
            vm_columns = cls.vm_column
        format_query = dict()
        for column in host_columns:
            if column not in cls.host_query:
                continue
            q = query.get(column, list())
            if len(q):
                format_query[column] = q
        format_query['data_center_id'] = (cid,)
        total_num = HostModelView.count_data_by_query(format_query)
        if 'host_id' not in host_columns:
            host_columns.append('host_id')
        res = HostModelView.split_data_by_query(host_columns, format_query, offset, limit, sort, order)
        response_data = list()
        for item in res:
            info_dict = dict()
            for column in host_columns:
                db_entity_attr_val = getattr(item, column)
                info_dict[column] = db_entity_attr_val
            response_data.append(info_dict)
        if 'id' not in vm_columns:
            vm_columns.append('id')
        host_id_list = [i['host_id'] for i in response_data]
        vm_infos = HostApiDao.get_vm_infos(host_id_list, vm_columns)
        for host_info in response_data:
            host_info['vm_info'] = vm_infos[host_info['host_id']]
        return dict(res=response_data, total_num=total_num)
