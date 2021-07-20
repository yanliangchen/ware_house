#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_service_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/19 14:53
# @Desc  : 
from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class NovaServiceView(EriCICBase):
    __tablename__ = 'nova_service_view'

    id = Column(String(50), nullable=False)
    host = Column(String(50), )
    status = Column(String(50), )
    state = Column(String(50), )
    availability_zone = Column(String(50), )
    update_at = Column(Integer(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)
    vm_num = Column(Integer(), nullable=False)
    host_aggregate = Column(String())
