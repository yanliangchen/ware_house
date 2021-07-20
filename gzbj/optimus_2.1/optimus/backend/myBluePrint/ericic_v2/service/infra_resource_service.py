#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : infra_resource_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 21:26
# @Desc  :
from backend.common.scriptHandler import ScriptHandler
from taskModel.db_fresh.common.format_tools import table_format
from taskModel.db_fresh.cmd_mapping import OPEN_STACK_HOST_SHOW
from backend.myBluePrint.ericic_v2.base_dao.infra_resource_dao import InfraResourceDao


# +-----------------------------+----------------------------------+-----+-----------+---------+
# | Host                        | Project                          | CPU | Memory MB | Disk GB |
# +-----------------------------+----------------------------------+-----+-----------+---------+
# | compute4.bjitte.ericsson.se | (total)                          |  56 |    385401 |     811 |
# | compute4.bjitte.ericsson.se | (used_now)                       |  24 |     45568 |       0 |
# | compute4.bjitte.ericsson.se | (used_max)                       |  24 |     45056 |       0 |
# | compute4.bjitte.ericsson.se | 4c9e929380e442599883cf00e3f87de4 |  24 |     45056 |       0 |
# +-----------------------------+----------------------------------+-----+-----------+---------+

class InfraResourceService:

    @classmethod
    def get_infra_resource(cls, cid, host_id):
        res = InfraResourceDao.get_dc_host_info(cid, host_id)
        dc_entity, host_entity = res['dc_entity'], res['host_entity']
        if dc_entity and host_entity:
            ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
            ssh_tunnel.source_file(dc_entity.openstackrc_dir)
            output = ssh_tunnel.execute_cmd(OPEN_STACK_HOST_SHOW.format(name=host_entity.host))
            if output == b'many found' or output == b'none found (HTTP 404)\n' or (not output):
                # todo : consider the situation when the output is many found
                return None
            output = table_format(output)
            response = dict()
            for item in output:
                project = item['Project']
                cpu = item['CPU']
                ram = item['Memory MB']
                rom = item['Disk GB']
                if project == '(total)':
                    response['total_cpu'] = int(cpu)
                    response['total_ram'] = int(ram)
                    response['total_rom'] = int(rom)
                elif project == '(used_now)':
                    response['used_cpu'] = int(cpu)
                    response['used_ram'] = int(ram)
                    response['used_rom'] = int(rom)
                elif project == '(used_max)':
                    pass
        else:
            response = None
        return response
