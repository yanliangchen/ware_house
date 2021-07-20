#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : tenant_quota.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/28 16:20
# @Desc  : test
from flask import make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.tenant_quota_service import TenantQuotaService


class TenantQuotaView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = kwargs.get('cid')
        tid = kwargs.get('tid')
        res = TenantQuotaService.get_tenant_quota_info(cid, tid)
        return make_response(dict(data=res, code=200, status=True)), 200
