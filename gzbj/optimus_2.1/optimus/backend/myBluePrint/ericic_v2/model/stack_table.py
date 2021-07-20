#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : stack_list.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/2 16:04
# @Desc  :

from sqlalchemy import Column, String, Integer
from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase


class StackModel(EriCICBase):
    __tablename__ = 'stack_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    project = Column(String(50), )  # this is the id of tenant
    stack_status = Column(String(50), )
    creation_time = Column(Integer(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, name, project, stack_status, dc_id, creation_time, timestamp):
        self.id = _id
        self.name = name
        self.project = project
        self.stack_status = stack_status
        self.dc_id = dc_id
        self.creation_time = creation_time
        self.timestamp = timestamp
