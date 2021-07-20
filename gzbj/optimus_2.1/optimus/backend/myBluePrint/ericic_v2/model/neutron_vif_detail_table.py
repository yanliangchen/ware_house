#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : neutron_vif_detail_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 13:25
# @Desc  : neutron port-list -c id -c name -c status -c binding:host_id -c binding:profile -c binding:vif_type -c binding:vif_details  -c device_id -c fixed_ips -c allowed_address_pairs -c mac_address -c qos_policy_id -c security_groups  -c port_security_enabled

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer


class NeutronVifDetailModel(EriCICBase):
    __tablename__ = 'neutron_vif_detail_table'

    id = Column(String(50), nullable=False)
    vif_details = Column(String(50), )
    tenant_id = Column(String(50), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    def __init__(self, _id, vif_details, dc_id, timestamp):
        self.id = _id
        self.vif_details = vif_details
        self.dc_id = dc_id
        self.timestamp = timestamp
