#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : neutron_port_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 11:32
# @Desc  : neutron port-list -c id -c name -c status -c binding:host_id -c binding:profile -c binding:vif_type -c binding:vif_details  -c device_id -c fixed_ips -c allowed_address_pairs -c mac_address -c qos_policy_id -c security_groups  -c port_security_enabled

# +--------------------------------------+------------+--------+-------------------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+-------------------+---------------+------------------------------------------+-----------------------+
# | id                                   | name       | status | binding:host_id         | binding:profile | binding:vif_type | binding:vif_details                                                                                                                                             | device_id                                                                     | fixed_ips                                                                           | allowed_address_pairs | mac_address       | qos_policy_id | security_groups                          | port_security_enabled |
# +--------------------------------------+------------+--------+-------------------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+-------------------+---------------+------------------------------------------+-----------------------+
# | 5a092bf9-0032-4def-a9e5-1330588e0588 |            | ACTIVE | compute1.k2.ericsson.se | {}              | vhostuser        | {'ovs_hybrid_plug': False, 'port_filter': False, 'vhostuser_socket': '/run/openvswitch/vhu5a092bf9-00', 'vhostuser_ovs_plug': True, 'vhostuser_mode': 'server'} | fb172b8f-104c-4770-a71f-83cdf3d1d7be                                          | {"subnet_id": "ad6046bf-d5b6-4f82-a9ef-269969d7eac0", "ip_address": "10.1.1.14"}    | []                    | fa:16:3e:6e:cf:1b |               | ['0719c08a-51a8-42a7-8c90-661f13230750'] | True                  |
# | bd949593-592e-41d0-9c2b-5825127395e9 |            | ACTIVE | cic-1.k2.ericsson.se    | {}              | vhostuser        | {'ovs_hybrid_plug': False, 'port_filter': False, 'vhostuser_socket': '/run/openvswitch/vhubd949593-59', 'vhostuser_ovs_plug': True, 'vhostuser_mode': 'server'} | dhcp03392c1d-28fd-55ac-93ce-f07291d384b8-c8ab830a-1346-4854-a870-a7e7a5257306 | {"subnet_id": "ad6046bf-d5b6-4f82-a9ef-269969d7eac0", "ip_address": "10.1.1.10"}    | []                    | fa:16:3e:d4:ea:ec |               | []                                       | False                 |


from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer, BOOLEAN, JSON


class NeutronPortTable(EriCICBase):
    __tablename__ = 'neutron_port_table'

    id = Column(String(50), nullable=False)
    name = Column(String(50), )
    status = Column(String(50), )
    binding_host_id = Column(String(50), )  # foreign key tenant table's key id
    binding_profile = Column(String(50), )
    binding_vif_type = Column(String(50), )
    device_id = Column(String(50), ) # foreign key from nova table
    subnet_id = Column(String(50), )
    ip_address = Column(String(50), )
    allowed_address_pairs = Column(String(255), )
    mac_address = Column(String(50), )
    qos_policy_id = Column(String(50), )
    security_groups = Column(JSON(), )
    port_security_enabled = Column(BOOLEAN(), )
    vif_details = Column(JSON(), )
    dc_id = Column(String(50), nullable=False)
    timestamp = Column(Integer(), nullable=False)

    # id = Column(String(50), nullable=False)
    # name = Column(String(50), )
    # status = Column(String(50), )
    # binding_host_id = Column(String(50), )  # foreign key tenant table's key id
    # binding_profile = Column(String(50), )
    # binding_vif_type = Column(String(50), )
    # device_id = Column(String(50), )
    # subnet_id = Column(String(50), )
    # ip_address = Column(String(50), )
    # allowed_address_pairs = Column(String(50), )
    # mac_address = Column(String(50), )
    # qos_policy_id = Column(String(50), )
    # security_groups = Column(String(50), )
    # port_security_enabled = Column(BOOLEAN(), )
    # vif_details = Column(String(50), )
    # dc_id = Column(String(50), nullable=False)
    # timestamp = Column(Integer(), nullable=False)

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, name, status, binding_host_id, binding_profile, binding_vif_type, device_id,
                 subnet_id, ip_address, allowed_address_pairs, mac_address, qos_policy_id, security_groups,
                 port_security_enabled, vif_details, dc_id, timestamp):
        self.id = _id
        self.name = name
        self.status = status
        self.binding_host_id = binding_host_id
        self.binding_profile = binding_profile
        self.binding_vif_type = binding_vif_type
        self.device_id = device_id
        self.subnet_id = subnet_id
        self.ip_address = ip_address
        self.allowed_address_pairs = allowed_address_pairs
        self.mac_address = mac_address
        self.qos_policy_id = qos_policy_id
        self.security_groups = security_groups
        self.port_security_enabled = port_security_enabled
        self.vif_details = vif_details
        self.dc_id = dc_id
        self.timestamp = timestamp
