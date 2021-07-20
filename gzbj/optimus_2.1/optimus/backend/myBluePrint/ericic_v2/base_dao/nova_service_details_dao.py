#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_service_details_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/4 10:25
# @Desc  : 
from backend.Model.connection import SESSION, and_
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel


class NovaServiceDetailsDao:

    @classmethod
    def filter_nova_service_with_status(cls, cid, status):
        db_session = SESSION()
        try:
            filter_entity = and_(NovaServiceModel.dc_id == cid, NovaServiceModel.state == status)
            service_entities = db_session.query(NovaServiceModel).filter(filter_entity).all()
        finally:
            db_session.close()
        return service_entities
