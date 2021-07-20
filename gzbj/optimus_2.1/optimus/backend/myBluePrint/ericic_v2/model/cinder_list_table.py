#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cinder_list_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 11:26
# @Desc  : cinder list --all-tenants
from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer, BOOLEAN, PrimaryKeyConstraint


class CinderModel(EriCICBase):
    __tablename__ = 'cinder_list_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    status = Column(String(50), )
    size = Column(Integer(), )
    volume_type = Column(String(50), )
    bootable = Column(BOOLEAN(), )
    attach_to = Column(String(50), )  # which vm does the volume belong to (foreign key nova table's key id)
    tenant_id = Column(String(50), )  # foreign key tenant table's key id
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'dc_id'),
    )

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, name, status, size, volume_type, bootable, attach_to, tenant_id, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.status = status
        self.size = size
        self.volume_type = volume_type
        self.bootable = bootable
        self.attach_to = attach_to
        self.tenant_id = tenant_id
        self.dc_id = dc_id
        self.timestamp = timestamp
