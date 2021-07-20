#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : nova_service_detail_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/4 10:18
# @Desc  :
from flask import make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.nova_service_details_service import NovaServiceDetailsService


class NovaServiceDetailsView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = kwargs.get('cid')
        status = kwargs.get('status')
        res = NovaServiceDetailsService.filter_nova_service_with_status(cid, status)
        return make_response(dict(status=True, data=res, code=200)), 200
