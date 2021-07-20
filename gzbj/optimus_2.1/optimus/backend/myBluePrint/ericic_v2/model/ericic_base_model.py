#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : EricicBaseModel.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/4 18:19
# @Desc  : 
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint
from backend.Model.connection import MyBase, BASE


class EriCICBase(BASE):
    __abstract__ = True

    id = Column(String(50), nullable=False)
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'dc_id'),
    )
