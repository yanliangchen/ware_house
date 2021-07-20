#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : infrastructure_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/15 15:25
# @Desc  :
from backend.myBluePrint.ericic_v2.base_dao.infrastructure_dao import InfrastructureDao


class InfrastructureService:

    @classmethod
    def get_over_view(cls, cid):
        res = InfrastructureDao.get_over_view_info(cid)
        hyper_res = res['hyper']
        tenant_res = res['tenant']
        host_res = res['host']
        volume_res = res['volume']
        if hyper_res:
            res = dict(
                total_storage=hyper_res.local_gb,
                used_storage=hyper_res.local_gb_used,
                total_memory=hyper_res.memory_mg,
                used_memory=hyper_res.memory_mg_used,
                total_vcpus=hyper_res.vcpus,
                used_vcpus=hyper_res.vcpus_used,
                tenant_info=list(),
                host_info=dict(total=0, up=0, down=0),
                volume_info=list()
            )
            for tenant_quota, tenant_project in tenant_res:
                info = dict(
                    core_used=tenant_quota.cores_in_use,
                    ram_used=tenant_quota.ram_in_use,
                    name=tenant_project.name,
                    id=tenant_project.id,
                )
                res['tenant_info'].append(info)
            for host in host_res:
                state = host.state
                res['host_info']['total'] += 1
                if state.lower() == 'up':
                    res['host_info']['up'] += 1
                else:
                    res['host_info']['down'] += 1
            for volume in volume_res:
                info = dict(
                    id=volume.id,
                    name=volume.name,
                )
                res['volume_info'].append(info)
        else:
            res = None
        return res
