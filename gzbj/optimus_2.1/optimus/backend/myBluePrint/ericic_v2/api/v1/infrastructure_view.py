#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : infrastructure_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/15 15:22
# @Desc  : 
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.infrastructure_service import InfrastructureService


class InfrastructureView(APiMethodView):
    # check_cls = ConnStatusVerify

    def get(self, *args, **kwargs):
        cid = request.args.get('cid')
        res = InfrastructureService.get_over_view(cid)
        # res = InfrastructureService.check_by_cid(cid)
        return make_response(dict(code=200, status=True, data=res)), 200
