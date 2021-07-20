#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cpu_layout_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/21 11:04
# @Desc  :
from sqlalchemy import and_
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel


class CpuLayoutDao:

    @classmethod
    def get_dc_host_info(cls, cid, host_id):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).one_or_none()
            host_entity = db_session.query(NovaServiceModel).filter(
                and_(NovaServiceModel.dc_id == cid, NovaServiceModel.id == host_id)).one_or_none()
        finally:
            db_session.close()
        return dict(dc_entity=dc_entity, host_entity=host_entity)

    @classmethod
    def get_vm_info(cls, cid, instance_name_list):
        res = dict()
        db_session = SESSION()
        try:
            for name in instance_name_list:
                _filter_entity = and_(NovaModel.dc_id==cid, NovaModel.instance_name == name)
                nova_entity = db_session.query(NovaModel).filter(_filter_entity).one_or_none()
                res[name] = nova_entity
        finally:
            db_session.close()
        return res
