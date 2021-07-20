#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : network_port_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/24 9:50
# @Desc  :
from flask import make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.network_port_service import NetworkPortService
from backend.common.loghandler import ServiceLog

import json


class NetworkPortView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = kwargs.get('cid')
        vid = kwargs.get('vid')
        uid = kwargs.get('uid')

        if uid == 'uuuiiiddd':
            ing_res = NetworkPortService.get_vm_port_list(cid, vid)

            database_res = json.loads(NetworkPortService.select_port(_id=uid))

            increase_data = []

            for i in ing_res:
                for k in database_res:
                    if i['id'] == k['id']:
                        i['tx_packets_increase'] = int(i['tx_packets']) - int(k['tx_packets'])
                        i['tx_dropped_increase'] = int(i['tx_dropped']) - int(k['tx_dropped'])
                        i['rx_packets_increase'] = int(i['rx_packets']) - int(k['rx_packets'])
                        i['rx_dropped_increase'] = int(i['rx_dropped']) - int(k['rx_dropped'])
                        if i['tx_errors'] == k['tx_errors']:
                            i['tx_errors_increase'] = k['tx_errors']
                        if i['rx_errors'] == k['rx_errors']:
                            i['rx_errors_increase'] = k['rx_errors']
                        increase_data.append(i)

            return make_response(dict(status=True, code=200, data=increase_data)), 200
        else:

            res = NetworkPortService.get_vm_port_list(cid, vid)

            uid = 'uuuiiiddd'

            uuid = NetworkPortService.dynamic_port(port_res=res, dc_id=cid, uid=uid)

            return make_response(dict(status=True, code=200, data=res)), 200
