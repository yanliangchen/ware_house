#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : static_job.py
# @Author: yanliang.li
# @Email:
# @Date  : 2020/12/3 15:08
# @Desc  :
from sqlalchemy import and_
from taskModel.db_fresh.cmd_mapping import *
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.common.scriptHandler import ScriptHandler
from taskModel.db_fresh.common.command_to_json import command_to_json
import json
import time
from backend.myBluePrint.ericic_v2.model.nova_aggregate_table import NovaAggregateModel
from backend.myBluePrint.ericic_v2.model.nova_aggregate_host_relation_table import AggregateHostRelation
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel
from backend.myBluePrint.ericic_v2.model.openstack_volume_type_table import OpenstackVolumeTypeModel
from backend.myBluePrint.ericic_v2.model.openstack_hypervisor_stats_table import OpenstackHypervisorStatsModel
from backend.myBluePrint.ericic_v2.model.openstack_quota_table import OpenstackQuotaModel
from backend.myBluePrint.ericic_v2.model.cinder_quota_usage_table import CinderQuotaUsageModel
from backend.common.loghandler import BDLog
import uuid
from backend.scheduler_handler.task_mapping import STATIC_REFRESH
from backend.myBluePrint.ericic_v2.model.db_refresh_task import DBRefreshTaskModel


class StaticRefresh:

    @classmethod
    def run(cls, dc_id, once=False):
        dc_entity = cls._get_dc_info(dc_id)
        if not dc_entity.mode:
            raise RuntimeError('offline dc does not support the db fresh function')
        ssh_cee = ScriptHandler(
            dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd
        )
        ssh_cee.source_file(dc_entity.openstackrc_dir)
        # nova aggregate-list    索引为0是二阶需要一阶返回的id
        response_nova_id_list = cls._get_nova_list(dc_id, ssh_cee=ssh_cee)
        # 索引为1 是要插入的数据

        response_nova_data_list = response_nova_id_list[1]

        # nova aggregate-list show
        nova_show_data_list = cls._get_nova_aggregate_show(dc_id=dc_id, id_list=response_nova_id_list[0],
                                                           ssh_cee=ssh_cee)

        # openstack project list
        open_stack_project_list = cls._get_open_stack_project_list(ssh_cee=ssh_cee, dc_id=dc_id)

        open_stack_project_list_data = open_stack_project_list[1]

        # openstack volume type list
        volume_list_data = cls._get_openstack_volume_type_list(dc_id=dc_id, ssh_cee=ssh_cee)

        # openstack hypervisor stats show
        hype_v_list_data = cls._get_openstack_hypervisor_stats_show(ssh_cee=ssh_cee, dc_id=dc_id)

        # openstack quota list --project {id} --compute --detail
        cinda_quota_data = cls._get_openstack_quota_list(dc_id=dc_id, ssh_cee=ssh_cee,
                                                         project_id_list=open_stack_project_list[0])

        # cinder quota-usage {id}
        cinder_quota_usage_data = cls._get_cinder_quota_usage(dc_id=dc_id, ssh_cee=ssh_cee,
                                                              project_id_list=open_stack_project_list[0])
        # print(cinder_quota_usage_data)
        cls.static_data_insert(dc_id=dc_id, response_nova_data_list=response_nova_data_list,
                               response_nova_data_show_list=nova_show_data_list,
                               open_stack_project_list_data=open_stack_project_list_data,
                               volume_list_data=volume_list_data, hype_v_list_data=hype_v_list_data,
                               cinda_quota_data=cinda_quota_data, cinder_quota_usage_data=cinder_quota_usage_data,
                               once=once)

        # cls.static_data_insert(dc_id=dc_id,response_nova_data_list=response_nova_data_list,response_nova_data_show_list=nova_show_data_list)

    @classmethod
    def _get_cinder_quota_usage(cls, dc_id, ssh_cee, project_id_list):
        cinder_usage_list = []
        timestamp = time.time()
        for project_id in project_id_list:
            stack_list_ret = ssh_cee.execute_cmd(CINDER_QUOTA_USAGE.format(id=project_id))
            command_res = command_to_json()
            response_json_list = json.loads(command_res.test(stack_list_ret))
            if response_json_list:
                for cinder_usage in response_json_list:
                    cinder_usage_id = uuid.uuid4().hex
                    resource = cinder_usage['Type']
                    in_use = cinder_usage['In_use']
                    Reversed = cinder_usage['Reserved']
                    Limit = cinder_usage['Limit']
                    allocated = cinder_usage.get('Allocated', 0)
                    if allocated == '':
                        allocated = 0
                    cinder_u = CinderQuotaUsageModel(_id=cinder_usage_id, project_id=project_id,
                                                     resource=resource, in_use=in_use, reserved=Reversed,
                                                     allocated=allocated, dc_id=dc_id, timestamp=timestamp, limit=Limit)

                    cinder_usage_list.append(cinder_u)
        return cinder_usage_list

    @classmethod
    def _get_openstack_quota_list(cls, dc_id, ssh_cee, project_id_list):

        cinder_quota_list = []
        timestamp = time.time()
        for project_id in project_id_list:
            stack_list_ret = ssh_cee.execute_cmd(OPEN_STACK_QUOTA_LIST.format(id=project_id))
            command_res = command_to_json()
            response_json_list = json.loads(command_res.test(stack_list_ret))
            data_dict = {}
            quota_id = uuid.uuid4().hex
            if response_json_list:
                for cinder_quota in response_json_list:
                    if cinder_quota['Resource'] == 'cores':
                        data_dict['cores_in_use'] = cinder_quota['In Use']
                        data_dict['cores_limit'] = cinder_quota['Limit']
                    if cinder_quota['Resource'] == 'ram':
                        data_dict['ram_in_use'] = cinder_quota['In Use']
                        data_dict['ram_limit'] = cinder_quota['Limit']

                quota_u = OpenstackQuotaModel(_id=quota_id, cores_in_use=data_dict['cores_in_use'],
                                              cores_limit=data_dict['cores_limit'], ram_in_use=data_dict['ram_in_use'],
                                              ram_limit=data_dict['ram_limit'],
                                              project_id=project_id,
                                              timestamp=timestamp, dc_id=dc_id)
                cinder_quota_list.append(quota_u)
        return cinder_quota_list

    @classmethod
    def _get_openstack_hypervisor_stats_show(cls, ssh_cee, dc_id):
        stack_list_ret = ssh_cee.execute_cmd(OPEN_STACK_HYPERVISOR_STATUS)
        command_res = command_to_json()
        response_json_list = json.loads(command_res.test(stack_list_ret))
        timestamp = time.time()
        if response_json_list:
            hype_v_list = []
            item_id = uuid.uuid4().hex
            data_dict = {}
            for every_hype_v in response_json_list:

                if every_hype_v['Field'] == 'local_gb':
                    data_dict['local_gb'] = every_hype_v['Value']
                if every_hype_v['Field'] == 'local_gb_used':
                    data_dict['local_gb_used'] = every_hype_v['Value']
                if every_hype_v['Field'] == 'memory_mb':
                    data_dict['memory_mg'] = every_hype_v['Value']
                if every_hype_v['Field'] == 'memory_mb_used':
                    data_dict['memory_mg_used'] = every_hype_v['Value']
                if every_hype_v['Field'] == 'vcpus':
                    data_dict['vcpus'] = every_hype_v['Value']
                if every_hype_v['Field'] == 'vcpus_used':
                    data_dict['vcpus_used'] = every_hype_v['Value']

            hype_v_u = OpenstackHypervisorStatsModel(_id=item_id, local_gb=data_dict['local_gb'],
                                                     local_gb_used=data_dict['local_gb_used'],
                                                     memory_mg=data_dict['memory_mg'],
                                                     memory_mg_used=data_dict['memory_mg_used'],
                                                     vcpus=data_dict['vcpus'], vcpus_used=data_dict['vcpus_used'],
                                                     dc_id=dc_id, timestamp=timestamp)
            hype_v_list.append(hype_v_u)
            return hype_v_list

    @classmethod
    def _get_openstack_volume_type_list(cls, dc_id, ssh_cee):
        stack_list_ret = ssh_cee.execute_cmd(OPEN_STACK_VOLUME_TYPE_LIST)

        command_res = command_to_json()
        response_json_list = json.loads(command_res.test(stack_list_ret))
        timestamp = time.time()
        if response_json_list:
            volume_list = []
            for every_volume in response_json_list:
                ID = every_volume['ID']
                Name = every_volume['Name']
                is_public = every_volume['Is Public']
                volume_list_u = OpenstackVolumeTypeModel(_id=ID, name=Name, is_public=is_public, dc_id=dc_id,
                                                         timestamp=timestamp)
                volume_list.append(volume_list_u)
            return volume_list
        else:
            # the else situation was added by gaofzhan ad 2020/12/17 to a
            return list()

    @classmethod
    def _get_open_stack_project_list(cls, dc_id, ssh_cee):
        stack_list_ret = ssh_cee.execute_cmd(OPEN_STACK_PROJECT_LIST)
        command_res = command_to_json()
        response_json_list = json.loads(command_res.test(stack_list_ret))
        timestamp = time.time()
        if response_json_list:
            open_stack_project_list = []
            project_id_list = []
            dup_dict = dict()
            for item in response_json_list:
                id = item['ID']
                dup_dict[id] = item
            response = list()
            for item in response_json_list:
                name = item['Name']
                _id = name.split('-')[0]
                if _id in dup_dict:
                    pass
                else:
                    response.append(item)

            for every_openstack in response:
                ID_dict = {}
                ID = every_openstack['ID']
                ID_dict['project_id'] = ID
                project_id_list.append(ID_dict['project_id'])
                Name = every_openstack['Name']
                open_stack_u = OpenstackProjectModel(_id=ID, name=Name, dc_id=dc_id, timestamp=timestamp)
                open_stack_project_list.append(open_stack_u)
            return project_id_list, open_stack_project_list
        else:
            return list() ,list()

    @classmethod
    def _get_nova_aggregate_show(cls, dc_id, id_list, ssh_cee):
        nova_show_list = []
        timestamp = time.time()
        for nova_id in id_list:
            nova_aggregate_id_ret = ssh_cee.execute_cmd(NOVA_AGGREGATE_SHOW.format(id=nova_id))
            command_res = command_to_json()
            response_json_list = json.loads(command_res.test(nova_aggregate_id_ret))
            for every_aggregate in response_json_list:
                ag_id = every_aggregate['Id']
                ag_name = every_aggregate['Name']
                az = every_aggregate['Availability Zone']
                meta_data = str(every_aggregate['Metadata'])                
                hosts = every_aggregate['Hosts'].replace(" ","")
                hosts = hosts.replace("'","")
                hosts = hosts.split(",")
                
                for host  in hosts:
                    nova_show_u = AggregateHostRelation(ag_id=ag_id, aggregate_name=ag_name,
                                                            availability_zone=az, host=host, meta_data=meta_data, dc_id=dc_id,
                                                            timestamp=timestamp)
                    nova_show_list.append(nova_show_u)
                    
        return nova_show_list

    @classmethod
    def _get_nova_list(cls, dc_id, ssh_cee):
        nova_ret = ssh_cee.execute_cmd(NOVA_AGGREGATE_LIST)
        command_res = command_to_json()
        response_json_list = json.loads(command_res.test(nova_ret))
        if response_json_list:
            nova_list = []
            update_time = time.time()
            ID_list = []
            for every_nova in response_json_list:
                nova_dict = {}
                nova_dict['Id'] = every_nova['Id']
                ID = nova_dict['Id']
                ID_list.append(ID)
                nova_dict['Name'] = every_nova['Name']
                Name = nova_dict['Name']
                nova_dict['Availability Zone'] = every_nova['Availability Zone']
                az = nova_dict['Availability Zone']

                nova_list_u = NovaAggregateModel(_id=ID, name=Name, availability_zone=az, dc_id=dc_id,
                                                 timestamp=update_time)
                nova_list.append(nova_list_u)
            # 为了 nova aggregate-show 19
            # print(nova_list)
            return ID_list, nova_list
        else:
            return list(), list()

    @classmethod
    def _get_dc_info(cls, dc_id):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == dc_id).one_or_none()
        finally:
            db_session.close()
        return dc_entity

    @classmethod
    def static_data_insert(cls, dc_id, response_nova_data_list, response_nova_data_show_list,
                           open_stack_project_list_data, volume_list_data, cinder_quota_usage_data, cinda_quota_data,
                           hype_v_list_data, once):
        """


        :return:
        """

        db_session = SESSION()
        try:
            db_session.query(NovaAggregateModel).filter(NovaAggregateModel.dc_id == dc_id).delete()
            db_session.query(AggregateHostRelation).filter(AggregateHostRelation.dc_id == dc_id).delete()
            db_session.query(OpenstackProjectModel).filter(OpenstackProjectModel.dc_id == dc_id).delete()
            db_session.query(OpenstackVolumeTypeModel).filter(OpenstackVolumeTypeModel.dc_id == dc_id).delete()
            db_session.query(OpenstackHypervisorStatsModel).filter(
                OpenstackHypervisorStatsModel.dc_id == dc_id).delete()
            db_session.query(OpenstackQuotaModel).filter(OpenstackQuotaModel.dc_id == dc_id).delete()
            db_session.query(CinderQuotaUsageModel).filter(CinderQuotaUsageModel.dc_id == dc_id).delete()

            db_session.add_all(response_nova_data_list)
            db_session.add_all(response_nova_data_show_list)

            db_session.add_all(open_stack_project_list_data)
            db_session.add_all(volume_list_data)
            db_session.add_all(cinder_quota_usage_data)
            db_session.add_all(cinda_quota_data)
            db_session.add_all(hype_v_list_data)
            if not once:
                task_id = '%s:%s' % (dc_id, STATIC_REFRESH)
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
            BDLog.error(e)
            raise e
        finally:
            db_session.close()
