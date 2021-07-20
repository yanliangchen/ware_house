#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_aggregate_host_relation_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 13:45
# @Desc  : nova aggregate-show <ha-id>


from backend.myBluePrint.ericic_v2.model.ericic_base_model import BASE
from sqlalchemy import Column, String, Integer, TEXT, PrimaryKeyConstraint


class AggregateHostRelation(BASE):
    __tablename__ = 'nova_aggregate_host_relation_table'

    ag_id = Column(String(255), nullable=False)
    aggregate_name = Column(String(255), )
    availability_zone = Column(String(255), )
    host = Column(String(255), )
    meta_data = Column(String(255), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('host', 'dc_id', 'ag_id'),
    )

    def __init__(self, ag_id, aggregate_name, availability_zone, host, meta_data, dc_id, timestamp):
        self.ag_id = ag_id
        self.aggregate_name = aggregate_name
        self.availability_zone = availability_zone
        self.host = host
        self.meta_data = meta_data
        self.dc_id = dc_id
        self.timestamp = timestamp
