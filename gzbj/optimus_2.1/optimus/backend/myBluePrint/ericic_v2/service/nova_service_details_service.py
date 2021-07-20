#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : novaServiceDetailsService.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/4 10:23
# @Desc  :
from backend.myBluePrint.ericic_v2.base_dao.nova_service_details_dao import NovaServiceDetailsDao


class NovaServiceDetailsService:

    @classmethod
    def filter_nova_service_with_status(cls, cid, status):
        res = list()
        service_entities = NovaServiceDetailsDao.filter_nova_service_with_status(cid, status)
        for item in service_entities:
            info = dict(
                id=item.id,
                host=item.host,
                availability_zone=item.zone,
                status=item.status,
                state=item.state,
                cid=item.dc_id
            )
            res.append(info)
        return res
