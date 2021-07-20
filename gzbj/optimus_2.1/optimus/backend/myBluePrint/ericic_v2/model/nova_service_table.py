#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_service_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 13:30
# @Desc  : nova service-list

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class NovaServiceModel(EriCICBase):
    __tablename__ = 'nova_service_table'

    id = Column(String(50), nullable=False)
    host = Column(String(50), )
    status = Column(String(50), )
    state = Column(String(50), )
    zone = Column(String(50), )
    update_at = Column(Integer(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, host, status, state, zone, update_at, dc_id, timestamp):
        self.id = _id
        self.host = host
        self.status = status
        self.state = state
        self.zone = zone
        self.update_at = update_at
        self.dc_id = dc_id
        self.timestamp = timestamp
