#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : interface_driver_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/22 15:31
# @Desc  :
from sqlalchemy import and_
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel


class InterfaceDriverDao:

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
