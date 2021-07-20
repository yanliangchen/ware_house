#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : host_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/19 15:04
# @Desc  :
from backend.Model.connection import SESSION, and_
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.nova_service_view import NovaServiceView
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel


class HostDao:

    @classmethod
    def get_dc_entity_by_id(cls, cid):
        db_session = SESSION()
        try:
            res = db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).one_or_none()
        finally:
            db_session.close()
        return res

    @classmethod
    def get_vm_by_hids(cls, cid, host_list):
        res = dict()
        db_session = SESSION()
        try:
            for host in host_list:
                _ = and_(NovaModel.dc_id == cid, NovaModel.host == host, OpenstackProjectModel.dc_id == cid,
                         OpenstackProjectModel.id == NovaModel.tenant_id)
                vm_tenant_entities = db_session.query(NovaModel, OpenstackProjectModel).filter(_).all()
                # for item in vm_tenant_entities:
                #     vm_entity, tenant_entity = item
                res[host] = vm_tenant_entities
        finally:
            db_session.close()
        return res

    @classmethod
    def query_nova_service(cls, cid, query, filter, limit, offset, sort, order):
        db_session = SESSION()
        try:
            filter_list = [(NovaServiceView.dc_id == cid), ]
            if query and filter:
                filter_attr = getattr(NovaServiceView, query, None)
                _ = (filter_attr.like('%{query}%'.format(query=filter))) if query == 'host' else (filter_attr == filter)
                filter_list.append(_)
            sort_entity = getattr(NovaServiceView, sort) if getattr(NovaServiceView, sort,
                                                                    None) else NovaServiceView.update_at

            order_entities = [sort_entity.desc(), NovaServiceView.id.desc()] if order == 'desc' else [sort_entity.asc(),
                                                                                                      NovaServiceView.id.asc()]
            res = db_session.query(NovaServiceView).filter(and_(*filter_list)).order_by(*order_entities).offset(
                offset).limit(limit).all()
            count = db_session.query(NovaServiceView).filter(and_(*filter_list)).count()
        finally:
            db_session.close()
        return dict(res=res, count=count)
