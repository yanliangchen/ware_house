#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : tenant_quota_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/28 16:46
# @Desc  :
from backend.common.scriptHandler import ScriptHandler
from backend.myBluePrint.ericic_v2.common.format_tools import table_format
from backend.myBluePrint.ericic_v2.base_dao.tenant_quota_dao import TenantQuotaDao

CMD = 'cinder quota-usage {tenant_id}'


class TenantQuotaService:

    @classmethod
    def get_tenant_quota_info(cls, cid, tid):
        data = dict(cores=dict(), ram=dict(), volume=dict())
        entities = TenantQuotaDao.get_dc_tenant_hpyer_entity(cid, tid)
        tenant_entity, dc_entity, hyper_entity = entities['tenant_entity'], entities['dc_entity'], entities['hyper']
        if tenant_entity and dc_entity and hyper_entity:
            dc_cores_total = hyper_entity.vcpus
            # dc_cores_used = hyper_entity.vcpus_used
            dc_ram_total = hyper_entity.memory_mg
            # dc_ram_used = hyper_entity.memory_mg_used

            entities = TenantQuotaDao.get_volume_quota_info(cid, tid)
            usage_quota, pool_entities = entities['usage_quota'], entities['pool_entities']
            cores_in_use = usage_quota.cores_in_use
            cores_limit = usage_quota.cores_limit
            data['cores']['limit'] = cores_limit
            data['cores']['in_use'] = cores_in_use
            data['cores']['total'] = dc_cores_total
            # data['cores']['other'] = dc_cores_used - cores_in_use
            # data['cores']['availability'] = dc_cores_total - cores_in_use

            cpu_quota = usage_quota.cores_limit if usage_quota.cores_limit != -1 else hyper_entity.vcpus
            cpu_used_quota = usage_quota.cores_in_use
            cpu_free = hyper_entity.vcpus - hyper_entity.vcpus_used
            cpu_total = hyper_entity.vcpus
            if hyper_entity.vcpus - hyper_entity.vcpus_used > cpu_quota - usage_quota.cores_in_use:
                data['cores']['availability'] = cpu_quota - cpu_used_quota
                data['cores']['other'] = cpu_total - cpu_quota
            else:
                data['cores']['availability'] = cpu_free
                data['cores']['other'] = cpu_total - cpu_free - cpu_used_quota

            ram_in_use = usage_quota.ram_in_use
            ram_limit = usage_quota.ram_limit
            data['ram']['limit'] = ram_limit
            data['ram']['in_use'] = ram_in_use
            data['ram']['total'] = dc_ram_total
            # data['ram']['other'] = dc_ram_used - cores_in_use
            # data['ram']['availability'] = dc_ram_total - ram_in_use

            ram_quota = usage_quota.ram_limit if usage_quota.ram_limit != -1 else hyper_entity.memory_mg
            ram_used_quota = usage_quota.ram_in_use
            ram_free = hyper_entity.memory_mg - hyper_entity.memory_mg_used
            ram_total = hyper_entity.memory_mg

            if hyper_entity.memory_mg - hyper_entity.memory_mg_used > ram_quota - usage_quota.ram_in_use:
                data['ram']['availability'] = ram_quota - ram_used_quota
                data['ram']['other'] = ram_total - ram_quota
            else:
                data['ram']['availability'] = ram_free
                data['ram']['other'] = ram_total - ram_free - ram_used_quota

            ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
            ssh_tunnel.source_file(dc_entity.openstackrc_dir)
            output = ssh_tunnel.execute_cmd(CMD.format(tenant_id=tid))
            output_parsed = table_format(output)
            output_info_dict = dict()
            for item in output_parsed:
                _type = item['Type']
                output_info_dict[_type] = item
            pool_name_list = [pool.name for pool in pool_entities]
            for pool_name in pool_name_list:
                info = output_info_dict['gigabytes_%s' % pool_name]
                limit = info['Limit'].strip()
                in_use = info['In_use'].strip()
                data['volume'][pool_name] = dict(limit=int(limit), in_use=in_use)
            data['volume']['default'] = dict(limit=int(output_info_dict['gigabytes']['Limit']),
                                             in_use=int(output_info_dict['gigabytes']['In_use']))
        return data

    # @classmethod
    # def _cinder_quota_parse(cls, output):
    #     res = dict()
    #     line_list = output.split('\n')
    #     start_index = -1
    #     for index in range(line_list):
    #         line = line_list[index]
    #         if line.startswith('+-') and line.endswith('-+'):
    #             start_index = index
    #             break
    #     info_lines = line_list[start_index: -2]
    #     for info in info_lines:
    #         info_splited = info.split('|')
    #         info_splited = [i for i in info_splited if i]
    #         _type, in_use, reserved, limit, allocated = info_splited
    #

# WARNING:cinderclient.shell:API version 3.59 requested,
# WARNING:cinderclient.shell:downgrading to 3.0 based on server support.
# +----------------------------------------------+--------+----------+-------+-----------+
# | Type                                         | In_use | Reserved | Limit | Allocated |
# +----------------------------------------------+--------+----------+-------+-----------+
# | backup_gigabytes                             | 0      | 0        | 1000  | 0         |
# | backups                                      | 0      | 0        | 10    | 0         |
# | gigabytes                                    | 4504   | 0        | -1    | 0         |
# | gigabytes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU01 | 1473   | 0        | -1    | 0         |
# | gigabytes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU02 | 673    | 0        | -1    | 0         |
# | gigabytes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU03 | 1      | 0        | -1    | 0         |
# | gigabytes_NFV-R-HZZZ-07A-ER-01-VOLT-S02TRU01 | 1866   | 0        | -1    | 0         |
# | per_volume_gigabytes                         | 0      | 0        | -1    | 0         |
# | snapshots                                    | 0      | 0        | -1    | 0         |
# | snapshots_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU01 | 0      | 0        | -1    | 0         |
# | snapshots_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU02 | 0      | 0        | -1    | 0         |
# | snapshots_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU03 | 0      | 0        | -1    | 0         |
# | snapshots_NFV-R-HZZZ-07A-ER-01-VOLT-S02TRU01 | 0      | 0        | -1    | 0         |
# | volumes                                      | 127    | 0        | -1    | 0         |
# | volumes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU01   | 28     | 0        | -1    | 0         |
# | volumes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU02   | 13     | 0        | -1    | 0         |
# | volumes_NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU03   | 1      | 0        | -1    | 0         |
# | volumes_NFV-R-HZZZ-07A-ER-01-VOLT-S02TRU01   | 37     | 0        | -1    | 0         |
# +----------------------------------------------+--------+----------+-------+-----------+
