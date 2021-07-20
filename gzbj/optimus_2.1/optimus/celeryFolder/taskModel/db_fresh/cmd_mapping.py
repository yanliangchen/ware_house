#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cmd_mapping.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 10:03
# @Desc  : 

# dynamic
NOVA_LIST = 'nova list --field name,power_state,status,flavor,os-extended-volumes:volumes_attached,networks,host,created,image,instance_name,tenant_id,metadata --all-tenants'
CINDER_LIST = 'cinder list --all-tenants'
OPEN_STACK_LIST = 'openstack stack list'
# OPEN_STACK_LIST = 'openstack stack list --long'
OPEN_STACK_RESOURCE = 'openstack stack resource list {id}'
NOVA_SERVICE_LIST = 'nova service-list'
NOVA_FLAVOR_LIST = 'nova flavor-list --extra-specs'
NEUTRON_PORT_LIST = 'neutron port-list -c id -c name -c status -c binding:host_id -c binding:profile -c binding:vif_type -c binding:vif_details  -c device_id -c fixed_ips -c allowed_address_pairs -c mac_address -c qos_policy_id -c security_groups  -c port_security_enabled'

# static
NOVA_AGGREGATE_LIST = 'nova aggregate-list'
NOVA_AGGREGATE_SHOW = 'nova aggregate-show {id}'
OPEN_STACK_PROJECT_LIST = 'openstack project list'
OPEN_STACK_QUOTA_LIST = 'openstack quota list --project {id} --compute --detail'
CINDER_QUOTA_USAGE = 'cinder quota-usage {id}'
OPEN_STACK_HYPERVISOR_STATUS = 'openstack hypervisor stats show'
OPEN_STACK_VOLUME_TYPE_LIST = 'openstack volume type list'

# real time
OPEN_STACK_HOST_SHOW = 'openstack host show {name}'
EXEC_LIBVIRT = 'docker exec -it nova_libvirt bash'
