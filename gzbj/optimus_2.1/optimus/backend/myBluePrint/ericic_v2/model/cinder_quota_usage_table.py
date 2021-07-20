#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cinder_quota_usage_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 14:33
# @Desc  : cinder quota-usage f67d6213e83b49f18ff663f16c7d06e6

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer, JSON


class CinderQuotaUsageModel(EriCICBase):
    __tablename__ = 'cinder_quota_usage_table'

    id = Column(String(50), nullable=False)
    project_id = Column(String(50), )
    resource = Column(JSON(), )
    in_use = Column(Integer(), )
    reserved = Column(Integer(), )
    limit = Column(Integer(), )
    allocated = Column(Integer(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, project_id, resource, in_use, reserved, limit, allocated, dc_id, timestamp):
        self.id = _id
        self.resource = resource
        self.in_use = in_use
        self.reserved = reserved
        self.limit = limit
        self.allocated = allocated
        self.project_id = project_id
        self.dc_id = dc_id
        self.timestamp = timestamp
