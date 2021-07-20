#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : interface_driver.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/22 15:11
# @Desc  :
from flask import make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.interface_driver_service import InterfaceDriverService


class InterfaceDriverView(APiMethodView):

    def get(self, *args, **kwargs):
        hid = kwargs.get('hid')
        cid = kwargs.get('cid')
        res = InterfaceDriverService.get_driver_firmware_info(cid, hid)
        return make_response(dict(status=True, data=res, code=200)), 200
