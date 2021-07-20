#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : host_detail_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 18:46
# @Desc  :
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.conn_status_service import ConnStatusService
from backend.myBluePrint.ericic_v2.param_verify.connect_status_verify import ConnStatusVerify


class HostDetailView(APiMethodView):

    def get(self, *args, **kwargs):
        pass
