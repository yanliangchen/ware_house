#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : openstack_project_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 14:16
# @Desc  : openstack project list

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class OpenstackProjectModel(EriCICBase):
    __tablename__ = 'openstack_project_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, name, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.dc_id = dc_id
        self.timestamp = timestamp
