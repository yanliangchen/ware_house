#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : host_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/19 13:50
# @Desc  :
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.host_service import HostService


class HostView(APiMethodView):

    def get(self, *args, **kwargs):
        limit = request.args.get('limit', 10)
        offset = request.args.get('offset', 0)
        query = request.args.get('query')
        filter = request.args.get('filter')
        order = request.args.get('order', 'desc')
        sort = request.args.get('sort', 'update_time')
        dc_id = request.args.get('dc_id')
        try:
            limit = int(limit)
            offset = int(offset)
        except TypeError:
            limit = 50
            offset = 0
        query = query if query in ['host', 'host_aggregate', 'availability_zone', 'state'] else None
        sort = sort if sort in ['vm_num', ] else 'update_time'
        order = 'asc' if order == 'asc' else 'desc'
        res = HostService.get_nova_service(dc_id, query, filter, limit, offset, sort, order)
        return make_response(dict(data=res['res'], status=True, code=200, total=res['total'])), 200
