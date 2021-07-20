#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : openstack_quota_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 14:29
# @Desc  : openstack quota list --project d9231b55df95474188bc3304e254d363 --compute --detail

from backend.myBluePrint.ericic_v2.model.ericic_base_model import BASE
from sqlalchemy import Column, String, Integer


class OpenstackQuotaModel(BASE):
    __tablename__ = 'openstack_quota_table'

    id = Column(String(50), primary_key=True)
    cores_in_use = Column(Integer(), )
    cores_limit = Column(Integer(), )
    ram_in_use = Column(Integer(), )
    ram_limit = Column(Integer(), )
    project_id = Column(String(50), )
    dc_id = Column(String(50), )
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, cores_in_use, cores_limit, ram_in_use, ram_limit, project_id, dc_id, timestamp):
        self.id = _id
        self.cores_in_use = cores_in_use
        self.cores_limit = cores_limit
        self.ram_in_use = ram_in_use
        self.ram_limit = ram_limit
        self.project_id = project_id
        self.dc_id = dc_id
        self.timestamp = timestamp
