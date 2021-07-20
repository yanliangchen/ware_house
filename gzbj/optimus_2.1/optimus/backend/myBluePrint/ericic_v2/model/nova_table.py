#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/2 16:12
# @Desc  :  the info comes form the cmd --> nova list --field name,power_state,task_state,flavor,os-extended-volumes:volumes_attached,networks,host,created,image,instance_name,tenant_id,metadata --all-tenants

from sqlalchemy import Column, String, Integer, JSON, PrimaryKeyConstraint
from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase


class NovaModel(EriCICBase):
    __tablename__ = 'nova_table'

    id = Column(String(50), nullable=False)
    # item_id = Column(String(50), )
    name = Column(String(50), )
    power_state = Column(String(50), )
    task_state = Column(String(50), )
    flavor = Column(String(50), )
    host = Column(String(50), )
    created = Column(Integer(), )
    image = Column(JSON(), )
    instance_name = Column(String(50), )
    tenant_id = Column(String(50), )
    meta_data = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', 'dc_id'),
    )

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, name, power_state, task_state, flavor, host, created, image, instance_name,
                 tenant_id, meta_data, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.power_state = power_state
        self.task_state = task_state
        self.flavor = flavor
        self.host = host
        self.created = created
        self.image = image
        self.instance_name = instance_name
        self.tenant_id = tenant_id
        self.meta_data = meta_data
        self.dc_id = dc_id
        self.timestamp = timestamp
