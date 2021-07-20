#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : host_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/19 13:53
# @Desc  :
from backend.myBluePrint.ericic_v2.base_dao.host_dao import HostDao


class HostService:

    @classmethod
    def get_nova_service(cls, cid, query, filter, limit, offset, sort, order):
        res, total = list(), 0
        dc_entity = HostDao.get_dc_entity_by_id(cid)
        if dc_entity:
            host_entities = HostDao.query_nova_service(cid, query, filter, limit, offset, sort, order)
            total = host_entities['count']
            host_list = [host_entity.host for host_entity in host_entities['res']]
            vm_tenant_entities_info = HostDao.get_vm_by_hids(cid, host_list)
            for host_entity in host_entities['res']:
                info = dict()
                info['id'] = host_entity.id
                info['host'] = host_entity.host
                info['state'] = host_entity.state
                info['status'] = host_entity.status
                info['availability_zone'] = host_entity.availability_zone
                info['update_at'] = host_entity.update_at
                info['dc_id'] = host_entity.dc_id
                info['timestamp'] = host_entity.timestamp
                info['vm_num'] = host_entity.vm_num
                info['host_aggregate'] = host_entity.host_aggregate
                info['vm_info'] = list()
                vm_tenant_entities = vm_tenant_entities_info[host_entity.host]
                for vm_tenant_entity in vm_tenant_entities:
                    vm_entity, tenant_entity = vm_tenant_entity
                    info['vm_info'].append(dict(
                        id=vm_entity.id,
                        name=vm_entity.name,
                        status=vm_entity.task_state,
                        tenant_id=tenant_entity.id,
                        tenant_name=tenant_entity.name,
                    ))
                res.append(info)
        return dict(res=res, total=total)
