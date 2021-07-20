#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : openstack_hypervisor_stats_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 14:52
# @Desc  : openstack hypervisor stats show

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class OpenstackHypervisorStatsModel(EriCICBase):
    __tablename__ = 'openstack_hypervisor_stats_table'

    id = Column(String(50), nullable=False)
    local_gb = Column(Integer(), )
    local_gb_used = Column(Integer(), )
    memory_mg = Column(Integer(), )
    memory_mg_used = Column(Integer(), )
    vcpus = Column(Integer(), )
    vcpus_used = Column(Integer(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, local_gb, local_gb_used, memory_mg, memory_mg_used, vcpus, vcpus_used, dc_id, timestamp):
        self.id = _id
        self.local_gb = local_gb
        self.local_gb_used = local_gb_used
        self.memory_mg = memory_mg
        self.memory_mg_used = memory_mg_used
        self.vcpus = vcpus
        self.vcpus_used = vcpus_used
        self.dc_id = dc_id
        self.timestamp = timestamp
