#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : openstack_volume_type_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 14:26
# @Desc  : openstack volume type list

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class OpenstackVolumeTypeModel(EriCICBase):
    __tablename__ = 'openstack_volume_type_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    is_public = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, name, is_public, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.is_public = is_public
        self.dc_id = dc_id
        self.timestamp = timestamp
