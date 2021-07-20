#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : infrastructure_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/15 15:29
# @Desc  :
from sqlalchemy import and_
from backend.Model.connection import SESSION
# from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.openstack_quota_table import OpenstackQuotaModel
from backend.myBluePrint.ericic_v2.model.openstack_volume_type_table import OpenstackVolumeTypeModel
from backend.myBluePrint.ericic_v2.model.openstack_hypervisor_stats_table import OpenstackHypervisorStatsModel
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel


class InfrastructureDao:

    @classmethod
    def get_over_view_info(cls, cid):
        db_session = SESSION()
        try:
            hyper_res = db_session.query(OpenstackHypervisorStatsModel).filter(
                OpenstackHypervisorStatsModel.dc_id == cid).one_or_none()
            # tenant_res = db_session.query(OpenstackQuotaModel).filter(OpenstackQuotaModel.dc_id == cid).all()
            host_res = db_session.query(NovaServiceModel).filter(NovaServiceModel.dc_id == cid).all()
            volume_res = db_session.query(OpenstackVolumeTypeModel).filter(OpenstackVolumeTypeModel.dc_id == cid).all()
            _and = and_(OpenstackQuotaModel.project_id == OpenstackProjectModel.id,
                        OpenstackQuotaModel.dc_id == OpenstackProjectModel.dc_id)
            tenant_detail_res = db_session.query(OpenstackQuotaModel, OpenstackProjectModel).join(OpenstackProjectModel,
                                                                                                  _and).filter(
                OpenstackProjectModel.dc_id == cid).all()
            res = dict(hyper=hyper_res, tenant=tenant_detail_res, host=host_res, volume=volume_res)
        finally:
            db_session.close()
        return res
