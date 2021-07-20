#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_aggregate_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 13:41
# @Desc  : nova aggregate-list

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class NovaAggregateModel(EriCICBase):
    __tablename__ = 'nova_aggregate_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    availability_zone = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, name, availability_zone, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.availability_zone = availability_zone
        self.dc_id = dc_id
        self.timestamp = timestamp
