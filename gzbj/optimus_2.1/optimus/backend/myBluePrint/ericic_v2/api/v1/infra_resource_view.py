#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : infra_resource.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 21:20
# @Desc  :
from flask import make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.infra_resource_service import InfraResourceService


class InfraResourceView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = kwargs.get('cid')
        hid = kwargs.get('hid')
        res = InfraResourceService.get_infra_resource(cid, hid)
        return make_response(dict(status=True, data=res, code=200)), 200
