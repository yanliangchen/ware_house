#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : db_refresh_task.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/14 16:05
# @Desc  : 
from sqlalchemy import Column, String, Integer
from backend.Model.connection import BASE


class DBRefreshTaskModel(BASE):
    __tablename__ = 'db_refresh_task'

    id = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False, )
    start = Column(Integer(), nullable=False, default=8 * 60 * 60)
    end = Column(Integer(), nullable=False, default=18 * 60 * 60)
    interval = Column(Integer(), nullable=False)
    dc_id = Column(String(50), nullable=False, )
    version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, name, interval, dc_id):
        self.id = _id
        self.name = name
        self.interval = interval
        self.dc_id = dc_id
