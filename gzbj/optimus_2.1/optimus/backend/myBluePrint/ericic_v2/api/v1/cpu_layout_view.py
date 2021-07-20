#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cpu_layout_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 20:51
# @Desc  : 
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.cpu_layout_service import CpuLayoutService


class CpuLayoutView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = kwargs.get('cid')
        hid = kwargs.get('hid')
        res = CpuLayoutService.get_cpu_layout_info(cid, hid)
        return make_response(dict(data=res, status=True, code=200))
