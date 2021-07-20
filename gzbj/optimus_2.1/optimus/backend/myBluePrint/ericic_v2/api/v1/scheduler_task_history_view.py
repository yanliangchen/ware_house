#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_task_history.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 14:49
# @Desc  :
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.scheduler_task_history_service import SchedulerTaskHistoryService


class SchedulerTaskHistoryView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = request.args.get('cid')
        _filter = request.args.get('filter')
        _filter = _filter if _filter in ['static', 'dynamic'] else None
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 50)
        try:
            limit = int(limit)
            offset = int(offset)
        except Exception:
            limit = 50
            offset = 0
        res = SchedulerTaskHistoryService.get_history_by_cid(cid, _filter, limit, offset)
        return make_response(dict(status=True, code=200, data=res['data'], total_num=res['total_num'])), 200
