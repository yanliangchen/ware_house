#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : tenant_quota_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/28 16:46
# @Desc  :
from sqlalchemy import and_
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel
from backend.myBluePrint.ericic_v2.model.openstack_quota_table import OpenstackQuotaModel
# from backend.myBluePrint.ericic_v2.model.cinder_quota_usage_table import CinderQuotaUsageModel
from backend.myBluePrint.ericic_v2.model.openstack_hypervisor_stats_table import OpenstackHypervisorStatsModel
from backend.myBluePrint.ericic_v2.model.openstack_volume_type_table import OpenstackVolumeTypeModel


class TenantQuotaDao:

    @classmethod
    def get_dc_tenant_hpyer_entity(cls, cid, tid):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).one_or_none()
            tenant_entity = db_session.query(OpenstackProjectModel).filter(
                and_(OpenstackProjectModel.id == tid, OpenstackProjectModel.dc_id == cid)).one_or_none()
            hyper_res = db_session.query(OpenstackHypervisorStatsModel).filter(
                OpenstackHypervisorStatsModel.dc_id == cid).one_or_none()
        finally:
            db_session.close()
        return dict(dc_entity=dc_entity, tenant_entity=tenant_entity, hyper=hyper_res)

    @classmethod
    def get_volume_quota_info(cls, cid, tid):
        db_session = SESSION()
        try:
            u_filter = and_(OpenstackQuotaModel.project_id == tid, OpenstackQuotaModel.dc_id == cid)
            usage_quota = db_session.query(OpenstackQuotaModel).filter(u_filter).one_or_none()
            # v_filter = and_(CinderQuotaUsageModel.project_id == tid, CinderQuotaUsageModel.dc_id == cid)
            # volume_quota = db_session.query(CinderQuotaUsageModel).filter(v_filter).one_or_none()
            pool_entities = db_session.query(OpenstackVolumeTypeModel).filter(
                OpenstackVolumeTypeModel.dc_id == cid).all()
        finally:
            db_session.close()
        return dict(usage_quota=usage_quota, pool_entities=pool_entities)
