#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_flavor_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 11:15
# @Desc  : this table's info comes from nova flavor-list --extra-specs

from sqlalchemy import Column, String, Integer, JSON
from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase


class NovaFlavorModel(EriCICBase):
    __tablename__ = 'nova_flavor_table'

    id = Column(String(50), nullable=False)
    vcpus = Column(Integer(), )
    memory_mib = Column(Integer(), )
    disk = Column(Integer(), )
    extra_specs = Column(JSON(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, vcpus, memory_mib, disk, extra_specs, dc_id, timestamp):
        self.id = _id
        self.vcpus = vcpus
        self.memory_mib = memory_mib
        self.disk = disk
        self.extra_specs = extra_specs
        self.dc_id = dc_id
        self.timestamp = timestamp
