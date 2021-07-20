#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : openstack_stack_resource_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 13:36
# @Desc  : openstack stack resource list fe7fd613-c7b4-4ba9-938c-f4a943b78331


from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class OpenstackStackResourceModel(EriCICBase):
    __tablename__ = 'openstack_stack_resource_table'

    id = Column(String(50), nullable=False)
    resource_name = Column(String(50), )
    physical_resource_id = Column(String(50), )
    resource_type = Column(String(50), )
    resource_status = Column(String(50), )
    stack_id = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, resource_name, physical_resource_id, resource_type, resource_status, stack_id, dc_id,
                 timestamp):
        self.id = _id
        self.resource_name = resource_name
        self.physical_resource_id = physical_resource_id
        self.resource_type = resource_type
        self.resource_status = resource_status
        self.stack_id = stack_id
        self.dc_id = dc_id
        self.timestamp = timestamp
