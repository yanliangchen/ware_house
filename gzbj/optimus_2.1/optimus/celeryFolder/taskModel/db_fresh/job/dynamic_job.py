#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : dynamic_job.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/3 15:08
# @Desc  :
import json
import uuid
import time
from sqlalchemy import and_
from backend.Model.connection import SESSION, NO_FLUSH_SESSION
from backend.common.scriptHandler import ScriptHandler
from celeryFolder.taskModel.db_fresh.common.format_tools import table_format, time_format
from taskModel.db_fresh.cmd_mapping import NOVA_LIST, CINDER_LIST, OPEN_STACK_LIST, OPEN_STACK_RESOURCE, \
    NOVA_SERVICE_LIST, NOVA_FLAVOR_LIST, NEUTRON_PORT_LIST
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.nova_flavor_table import NovaFlavorModel
from backend.myBluePrint.ericic_v2.model.cinder_list_table import CinderModel
from backend.myBluePrint.ericic_v2.model.neutron_port_table import NeutronPortTable
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.openstack_stack_resource_table import OpenstackStackResourceModel
from backend.myBluePrint.ericic_v2.model.stack_table import StackModel
from backend.myBluePrint.ericic_v2.model.db_refresh_task import DBRefreshTaskModel
from backend.scheduler_handler.task_mapping import DYNAMIC_REFRESH


# 2409:8086:8618:2e4::38
# usr/pwd:     ceeinfra / r00tme

class DynamicRefresh:

    @classmethod
    def run(cls, dc_id, once=False):
        dc_entity = cls._get_dc_info(dc_id)
        dc_dict_info = dict(id=dc_entity.id, )
        if not dc_entity.mode:
            raise RuntimeError('offline dc does not support the db fresh function')
        ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
        # export the env
        # ssh_tunnel.execute_cmd('source %s' % dc_entity.openstackrc_dir)
        ssh_tunnel.source_file(dc_entity.openstackrc_dir)
        openstack_stack_list = cls._get_openstack_stack_list(ssh_tunnel, dc_dict_info)
        nova_list = cls._get_nova_list(ssh_tunnel, dc_dict_info)
        nova_flavor_list = cls._get_nova_flavor_list(ssh_tunnel, dc_dict_info)
        cinder_list = cls._get_cinder_list(ssh_tunnel, dc_dict_info)
        neutron_port_list = cls._get_neutron_port_list(ssh_tunnel, dc_dict_info)
        nova_service_list = cls._get_nova_service_list(ssh_tunnel, dc_dict_info)
        openstack_stack_resource_list = list()
        [openstack_stack_resource_list.extend(
            cls._get_openstack_stack_resource_list(ssh_tunnel, dc_dict_info, stack['_id'])) for stack in
            openstack_stack_list]
        distinct_dict = dict()
        [distinct_dict.setdefault(item['_id'], item) for item in openstack_stack_resource_list]
        openstack_stack_resource_list = [distinct_dict[key] for key in distinct_dict]
        # openstack_stack_list, nova_list, nova_flavor_list, cinder_list, nova_service_list = [], [], [], [], []
        cls._insert_dynamic_info(openstack_stack_list, nova_list, nova_flavor_list, cinder_list, neutron_port_list,
                                 nova_service_list, openstack_stack_resource_list, dc_id, once)
        return True

    @classmethod
    def _insert_dynamic_info(cls, openstack_stack_list, nova_list, nova_flavor_list, cinder_list, neutron_port_list,
                             nova_service_list, openstack_stack_resource_list, dc_id, once):
        openstack_stack_entities = [StackModel(**item) for item in openstack_stack_list]
        nova_entities = [NovaModel(**item) for item in nova_list]
        nova_flavor_entities = [NovaFlavorModel(**item) for item in nova_flavor_list]
        cinder_entities = [CinderModel(**item) for item in cinder_list]
        neutron_port_entities = [NeutronPortTable(**item) for item in neutron_port_list]
        nova_service_entities = [NovaServiceModel(**item) for item in nova_service_list]
        openstack_stack_resource_entities = [OpenstackStackResourceModel(**item) for item in
                                             openstack_stack_resource_list]
        # todo: 1. flush db by dc_id, than insert info into db
        db_session = NO_FLUSH_SESSION()
        try:
            db_session.query(StackModel).filter(StackModel.dc_id == dc_id).delete()
            db_session.query(NovaModel).filter(NovaModel.dc_id == dc_id).delete()
            db_session.query(NovaFlavorModel).filter(NovaFlavorModel.dc_id == dc_id).delete()
            db_session.query(CinderModel).filter(CinderModel.dc_id == dc_id).delete()
            db_session.query(NeutronPortTable).filter(NeutronPortTable.dc_id == dc_id).delete()
            db_session.query(NovaServiceModel).filter(NovaServiceModel.dc_id == dc_id).delete()
            db_session.query(OpenstackStackResourceModel).filter(OpenstackStackResourceModel.dc_id == dc_id).delete()

            db_session.add_all(openstack_stack_entities)
            db_session.add_all(nova_entities)
            db_session.add_all(nova_flavor_entities)
            db_session.add_all(cinder_entities)
            db_session.add_all(neutron_port_entities)

            db_session.add_all(nova_service_entities)
            db_session.add_all(openstack_stack_resource_entities)

            if not once:

                # db_session.add_all(openstack_stack_entities+nova_entities+nova_flavor_entities+cinder_entities+neutron_port_entities+nova_service_entities+openstack_stack_resource_entities)

                # add dc existing check to avoid the following phase as much as possible:
                # while the celery db fresh worker is running , the specify dc is deleted by the user
                # but even if the existing check, can not avoid the situation totally
                task_id = '%s:%s' % (dc_id, DYNAMIC_REFRESH)
                refresh_task_entity = db_session.query(DBRefreshTaskModel).filter(
                    DBRefreshTaskModel.id == task_id).one_or_none()
                if refresh_task_entity:
                    and_entity = and_(DBRefreshTaskModel.id == task_id,
                                      DBRefreshTaskModel.version == refresh_task_entity.version)
                    update_entity = {'version': refresh_task_entity.version + 1}
                    if db_session.query(DBRefreshTaskModel).filter(and_entity).update(update_entity):
                        db_session.commit()
                    else:
                        raise RuntimeError('the verify dc entity might been deleted')
                else:
                    db_session.rollback()
                    raise RuntimeError('can not find the task entity')
            else:
                db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e
        finally:
            db_session.close()

    @classmethod
    def _get_dc_info(cls, dc_id):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == dc_id).one_or_none()
        finally:
            db_session.close()
        return dc_entity

    # NOVA_LIST
    # +--------------------------------------+------------------------------------------------+----------------------------------+-------------+-----------------+----------------------+----------------------+
    # | ID                                   | Stack Name                                     | Project                          | Stack Owner | Stack Status    | Creation Time        | Updated Time         |
    # +--------------------------------------+------------------------------------------------+----------------------------------+-------------+-----------------+----------------------+----------------------+
    # | 9a9784d8-9a6d-4378-a364-c59a06a0c766 | NFV-R-HZZZ-07A-ER-01-HSTK-hnCHF003BER-nfs      | b6877db35e144283b8f57a67566c2d02 | None        | CREATE_COMPLETE | 2020-11-02T08:17:40Z | None                 |
    # | bc1de3e3-2101-4750-b1fa-411b4b708afa | APP-HZZZgdAMF004BER-07AER012                   | d9231b55df95474188bc3304e254d363 | None        | CREATE_COMPLETE | 2020-11-02T07:47:33Z | None                 |
    # | 1c48ea04-aa8c-4510-b6e0-b96193d90e07 | NFV-R-HZZZ-07A-ER-01-HSTK-hbUDM001FE101BER     | fb1263bf5a7543d2b787dcb1e7f07ace | None        | CREATE_COMPLETE | 2020-11-02T02:21:56Z | None                 |
    # | 8542a010-aa96-422b-afe6-33538ae9dd13 | APP-HZZZhnAMF005BER-07AER011                   | b6877db35e144283b8f57a67566c2d02 | None        | CREATE_COMPLETE | 2020-11-01T09:38:19Z | None                 |
    # | 921d2244-450f-4f58-9901-5d046d4b6595 | APP-HZZZhnSMF005BER-07AER011                   | b6877db35e144283b8f57a67566c2d02 | None        | CREATE_COMPLETE | 2020-11-01T08:30:55Z | None                 |
    # +--------------------------------------+------------------------------------------------+----------------------------------+-------------+-----------------+----------------------+----------------------+
    @classmethod
    def _get_openstack_stack_list(cls, ssh_tunnel, dc_dict_info):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(OPEN_STACK_LIST))
        # output_res = table_format(ssh_tunnel.execute_cmd('source /home/ceeinfra/admin-openrc.sh;'+OPEN_STACK_LIST))
        stack_info_list = list()
        for item in output_res:
            stack_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['ID'],
                name=item['Stack Name'],
                project=item['Project'],
                stack_status=item['Stack Status'],
                creation_time=time_format(item['Creation Time']),
                dc_id=dc_id,
                timestamp=timestamp,
            )
            if stack_info['stack_status'] == 'CREATE_COMPLETE':
                stack_info_list.append(stack_info)
        return stack_info_list

    # ceeinfra@e2e-lcm-1:~> nova list --field name,power_state,task_state,flavor,os-extended-volumes:volumes_attached,networks,host,created,instance_name,tenant_id,metadata --all-tenants
    # +--------------------------------------+------------------------------------------------+-------------+------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+----------------------+-------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    # | ID                                   | Name                                           | Power State | Task State | Flavor                               | os-extended-volumes: Volumes Attached                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Networks                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Host                         | Created              | Instance Name     | Tenant Id                        | Metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    # +--------------------------------------+------------------------------------------------+-------------+------------+--------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+----------------------+-------------------+----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    # | 26c16178-501e-451b-99e9-7419776c5a5e | NFV-R-HQBJ-16A-ER-01-VM-bjUDM001FE202BER-AP-A  | Running     | None       | c1838647-3d72-4418-98ed-75db80f4e19a | [{'id': '8b889b56-710d-443b-b987-b530a28ea8e3', 'delete_on_termination': False}, {'id': '401100cb-67fe-4d91-b23e-f9deb3e4cfd3', 'delete_on_termination': False}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | APP-HQBJbjUDM001FE202BER-16AER001-BAR=10.191.195.125; APP-HQBJbjUDM001FE202BER-16AER001-OM=10.191.131.37; APP-HQBJbjUDM001FE202BER-16AER001-PROV=10.191.131.45; APP-HQBJbjUDM001FE202BER-16AER001-SOAP=10.191.195.117; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-APZ-A=192.168.169.1; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-APZ-B=192.168.170.1; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-DRBD=169.254.213.1; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-LDE=169.254.208.1 | compute-c0105-08.ericsson.se | 2020-11-11T11:28:17Z | instance-00000cd6 | f128c53a25e547ee9689a1d629ab92f3 | {'ha-policy': 'ha-offline'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    # | 9701e2b3-5b15-4d3a-8cb0-6f8bcec4bdd8 | NFV-R-HQBJ-16A-ER-01-VM-bjUDM001FE202BER-AP-B  | Running     | None       | c1838647-3d72-4418-98ed-75db80f4e19a | [{'id': '631723fc-40af-4c65-af6b-8c764961c35c', 'delete_on_termination': False}, {'id': '0f5c7fb0-e23e-4897-bf6f-bbf77e82d32e', 'delete_on_termination': False}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | APP-HQBJbjUDM001FE202BER-16AER001-BAR=10.191.195.126; APP-HQBJbjUDM001FE202BER-16AER001-OM=10.191.131.38; APP-HQBJbjUDM001FE202BER-16AER001-PROV=10.191.131.46; APP-HQBJbjUDM001FE202BER-16AER001-SOAP=10.191.195.118; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-APZ-A=192.168.169.2; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-APZ-B=192.168.170.2; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-DRBD=169.254.213.2; NFV-R-HQBJ-16A-ER-01-VNET-bjUDM001FE202BER-LDE=169.254.208.2 | compute-c0105-04.ericsson.se | 2020-11-11T11:28:24Z | instance-00000cd9 | f128c53a25e547ee9689a1d629ab92f3 | {'ha-policy': 'ha-offline'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    @classmethod
    def _get_nova_list(cls, ssh_tunnel, dc_dict_info):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(NOVA_LIST))

        nova_info_list = list()
        for item in output_res:
            nova_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['ID'],
                name=item['Name'],
                power_state=item['Power State'],
                task_state=item['Status'],
                flavor=item['Flavor'],
                host=item['Host'],
                created=time_format(item['Created']),
                image=json.loads(item['Image'].replace("'", '"')) if item['Image'] else None,
                instance_name=item['Instance Name'],
                tenant_id=item['Tenant Id'],
                # meta_data=json.loads(item['Metadata'].replace("'", '"')) if item['Metadata'] else None,
                meta_data=str(item['Metadata']),
                dc_id=dc_id,
                timestamp=timestamp,
            )
            nova_info_list.append(nova_info)

        return nova_info_list

    # ceeinfra@e2e-lcm-1:~> nova flavor-list --extra-specs
    # +--------------------------------------+----------------------------------------------------+------------+------+-----------+------+-------+-------------+-----------+----------------------------------------------------------------------------------------------+
    # | ID                                   | Name                                               | Memory_MiB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public | extra_specs                                                                                  |
    # +--------------------------------------+----------------------------------------------------+------------+------+-----------+------+-------+-------------+-----------+----------------------------------------------------------------------------------------------+
    # | 02eb4bc7-bcdf-4294-9bf1-d50bc688c49c | smf01_vsfo_16vcpu_24576MBmem_40GBdisk              | 24576      | 40   | 0         |      | 16    | 1.0         | True      | {'hw:cpu_policy': 'dedicated', 'hw:mem_page_size': '1048576'}                                |
    # | 1                                    | m1.tiny                                            | 512        | 1    | 0         |      | 1     | 1.0         | True      | {}                                                                                           |
    # +--------------------------------------+----------------------------------------------------+------------+------+-----------+------+-------+-------------+-----------+----------------------------------------------------------------------------------------------+
    @classmethod
    def _get_nova_flavor_list(cls, ssh_tunnel, dc_dict_info):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(NOVA_FLAVOR_LIST))
        flavor_list = list()
        for item in output_res:
            flavor_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['ID'],
                vcpus=int(item['VCPUs']),
                memory_mib=int(item['Memory_MiB']),
                disk=int(item['Disk']),
                # extra_specs=item['extra_specs'],
                extra_specs=json.loads(item['extra_specs'].replace("'", '"')) if item['extra_specs'] else None,
                dc_id=dc_id,
                timestamp=timestamp,
            )
            flavor_list.append(flavor_info)
        return flavor_list

    # client@openstack-client:~> cinder list --all-tenants
    # WARNING:cinderclient.shell:API version 3.59 requested,
    # WARNING:cinderclient.shell:downgrading to 3.0 based on server support.
    # +--------------------------------------+----------------------------------+----------------+-----------------------------------------------------------------------------------------+-------+------------------------------------+----------+--------------------------------------+
    # | ID                                   | Tenant ID                        | Status         | Name                                                                                    | Size  | Volume Type                        | Bootable | Attached to                          |
    # +--------------------------------------+----------------------------------+----------------+-----------------------------------------------------------------------------------------+-------+------------------------------------+----------+--------------------------------------+
    # | 02245cf5-acb0-458f-8688-c442b8c05911 | fb1263bf5a7543d2b787dcb1e7f07ace | in-use         | nfv-r-hzzz-07a-er-01-vol-hbudm002uudr101ber-hbu2e1-fd0acd11-0d23-4ad7-b391-d5fb4b9314e0 | 2     | NFV-R-HZZZ-07A-ER-01-VOLT-S02TRU01 | false    | 53c9f18a-df63-493f-830c-b7173698b2cf |
    # | 04633bec-90f2-44dd-8325-7914b5a89c9b | b6877db35e144283b8f57a67566c2d02 | in-use         | NFV-R-HZZZ-07A-ER-01-VOL-HZZZhnSMF005BER-SFO5                                           | 40    | NFV-R-HZZZ-07A-ER-01-VOLT-S01TRU01 | true     | 36cbeaa0-c5cc-40c1-9168-08faff56bad4 |
    # +--------------------------------------+----------------------------------+----------------+-----------------------------------------------------------------------------------------+-------+------------------------------------+----------+--------------------------------------+
    @classmethod
    def _get_cinder_list(cls, ssh_tunnel, dc_dict_info):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(CINDER_LIST))
        cinder_list = list()
        for item in output_res:
            cinder_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['ID'],
                name=item['Name'],
                status=item['Status'],
                size=int(item['Size']) if item['Size'] else 0,
                volume_type=item['Volume Type'] if item['Volume Type'] != '-' else None,
                bootable=True if item['Bootable'] == 'true' else False,
                attach_to=item['Attached to'] if item['Attached to'] else None,
                tenant_id=item['Tenant ID'],
                dc_id=dc_id,
                timestamp=timestamp,
            )
            cinder_list.append(cinder_info)
        return cinder_list

    # ceeinfra@lcm2:~> neutron port-list -c id -c name -c status -c binding:host_id -c binding:profile -c binding:vif_type -c binding:vif_details  -c device_id -c fixed_ips -c allowed_address_pairs -c mac_address -c qos_policy_id -c security_groups  -c port_security_enabled
    # neutron CLI is deprecated and will be removed in the future. Use openstack CLI instead.
    # +--------------------------------------+------------+--------+-------------------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+-------------------+---------------+------------------------------------------+-----------------------+
    # | id                                   | name       | status | binding:host_id         | binding:profile | binding:vif_type | binding:vif_details                                                                                                                                             | device_id                                                                     | fixed_ips                                                                           | allowed_address_pairs | mac_address       | qos_policy_id | security_groups                          | port_security_enabled |
    # +--------------------------------------+------------+--------+-------------------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+-------------------+---------------+------------------------------------------+-----------------------+
    # | 5a092bf9-0032-4def-a9e5-1330588e0588 |            | ACTIVE | compute1.k2.ericsson.se | {}              | vhostuser        | {'ovs_hybrid_plug': False, 'port_filter': False, 'vhostuser_socket': '/run/openvswitch/vhu5a092bf9-00', 'vhostuser_ovs_plug': True, 'vhostuser_mode': 'server'} | fb172b8f-104c-4770-a71f-83cdf3d1d7be                                          | {"subnet_id": "ad6046bf-d5b6-4f82-a9ef-269969d7eac0", "ip_address": "10.1.1.14"}    | []                    | fa:16:3e:6e:cf:1b |               | ['0719c08a-51a8-42a7-8c90-661f13230750'] | True                  |
    # | bd949593-592e-41d0-9c2b-5825127395e9 |            | ACTIVE | cic-1.k2.ericsson.se    | {}              | vhostuser        | {'ovs_hybrid_plug': False, 'port_filter': False, 'vhostuser_socket': '/run/openvswitch/vhubd949593-59', 'vhostuser_ovs_plug': True, 'vhostuser_mode': 'server'} | dhcp03392c1d-28fd-55ac-93ce-f07291d384b8-c8ab830a-1346-4854-a870-a7e7a5257306 | {"subnet_id": "ad6046bf-d5b6-4f82-a9ef-269969d7eac0", "ip_address": "10.1.1.10"}    | []                    | fa:16:3e:d4:ea:ec |               | []                                       | False                 |
    @classmethod
    def _get_neutron_port_list(cls, ssh_tunnel, dc_dict_info):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(NEUTRON_PORT_LIST))
        # output_res = json.loads(command_to_json().str2json(output))
        neutron_list = list()
        for item in output_res:
            fixed_ips = item['fixed_ips'].replace("'", '"')
            fixed_ips = json.loads(fixed_ips if fixed_ips else dict(subnet_id=None, ip_address=None))
            if item['binding:vif_details']:
                vif_details = item['binding:vif_details'].replace("'", '"')
                vif_details = json.loads(vif_details.replace("True", '"True"').replace("False", '"False"'))
            else:
                vif_details = dict()
            neutron_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['id'] if item['id'] else uuid.uuid4().hex,
                name=item['name'],
                status=item['status'],
                binding_host_id=item['binding:host_id'],
                binding_profile=item['binding:profile'],
                binding_vif_type=item['binding:vif_type'],
                device_id=item['device_id'],
                subnet_id=fixed_ips['subnet_id'],
                ip_address=fixed_ips['ip_address'],
                # allowed_address_pairs=json.loads(item['allowed_address_pairs'].replace("'", '"')) if item[
                #     'allowed_address_pairs'] else None,
                allowed_address_pairs=item['allowed_address_pairs'],
                mac_address=item['mac_address'],
                qos_policy_id=item['qos_policy_id'],
                security_groups=json.loads(item['security_groups'].replace("'", '"')) if item[
                    'security_groups'] else None,
                # security_groups=item['security_groups'],
                port_security_enabled=False if item['port_security_enabled'] == 'False' else True,
                vif_details=vif_details,
                dc_id=dc_id,
                timestamp=timestamp,
            )
            neutron_list.append(neutron_info)
        # import pprint
        # pprint.pprint(neutron_list)
        return neutron_list

    @classmethod
    def _get_nova_service_list(cls, ssh_tunnel, dc_dict_info):
        #
        # def _inner_nova_service_clear(_info_res):
        #     _res_list = list()
        #     for i in _info_res:
        #         i_name = i['host']
        #         if

        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(NOVA_SERVICE_LIST))
        # output_res = json.loads(command_to_json().str2json(output))
        nova_service_list = list()
        for item in output_res:
            item_binary = item['Binary']
            if str(item_binary) == 'nova-compute':
                nova_service_info = dict(
                    # id=uuid.uuid4().hex,
                    _id=item['Id'],
                    host=item['Host'],
                    status=item['Status'],
                    state=item['State'],
                    zone=item['Zone'],
                    update_at=time_format(item['Updated_at']),
                    dc_id=dc_id,
                    timestamp=timestamp,
                )
                nova_service_list.append(nova_service_info)
        return nova_service_list

    # client@openstack-client:~> openstack stack resource list b6612306-4b2b-4523-a90f-1a480c853f1a
    # +-----------------------+--------------------------------------+-----------------------+-----------------+----------------------+
    # | resource_name         | physical_resource_id                 | resource_type         | resource_status | updated_time         |
    # +-----------------------+--------------------------------------+-----------------------+-----------------+----------------------+
    # | mm_instance5          | eb85a0ac-cdc8-400e-94d9-772d5707146d | OS::Nova::Server      | CREATE_COMPLETE | 2020-11-02T13:54:01Z |
    # | port2_onmnet          | f01c75ef-2ae9-4e34-a43d-44548e50ecfb | OS::Neutron::Port     | CREATE_COMPLETE | 2020-11-02T13:54:01Z |
    # | bootable2_volume      | 4b38a6bf-8560-4073-acc5-f254c87a12d9 | OS::Cinder::Volume    | CREATE_COMPLETE | 2020-11-02T13:54:01Z |
    # | ONM_Network1          | 5b41a4e5-d1bc-47e5-9a4e-5e4feaeb36c3 | OS::Neutron::Net      | CREATE_COMPLETE | 2020-11-02T13:54:02Z |
    # +-----------------------+--------------------------------------+-----------------------+-----------------+----------------------+
    @classmethod
    def _get_openstack_stack_resource_list(cls, ssh_tunnel, dc_dict_info, stack_id):
        dc_id = dc_dict_info['id']
        timestamp = int(time.time())
        output_res = table_format(ssh_tunnel.execute_cmd(OPEN_STACK_RESOURCE.format(id=stack_id)))
        # output_res = json.loads(command_to_json().str2json(output))
        openstack_stack_resource_list = list()
        for item in output_res:
            openstack_stack_resource_info = dict(
                # id=uuid.uuid4().hex,
                _id=item['physical_resource_id'],
                resource_name=item['resource_name'],
                physical_resource_id=item['physical_resource_id'],
                resource_type=item['resource_type'],
                resource_status=item['resource_status'],
                stack_id=stack_id,
                dc_id=dc_id,
                timestamp=timestamp,
            )
            openstack_stack_resource_list.append(openstack_stack_resource_info)
        # import pprint
        # pprint.pprint(openstack_stack_resource_list)
        return openstack_stack_resource_list
