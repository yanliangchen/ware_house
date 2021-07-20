#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_view.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/8 16:23
# @Desc  :
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.scheduler_task_service import SchedulerService
from backend.myBluePrint.ericic_v2.param_verify.scheduler_task_verify import SchedulerTaskVerify


class SchedulerTaskView(APiMethodView):
    check_cls = SchedulerTaskVerify

    def get(self, *args, **kwargs):
        cid = request.args.get('cid')
        if cid:
            res = SchedulerService.get_dc_refresh_task_by_id(cid)
        else:
            res = None
        return make_response(dict(code=200, data=res, status=True)), 200

    # def post(self, *args, **kwargs):
    #     body = request.get_json()
    #     cid = body['cid']
    #     action = body['action']
    #     task = body['task']
    #     if action == 'pause':
    #         SchedulerService.pause_job(cid, task)
    #     else:
    #         SchedulerService.resume_job(cid, task)
    #     return make_response(dict(code=201, status=True)), 201

    def put(self, *args, **kwargs):
        body = request.get_json()
        cid = body['cid']
        interval = body['interval']
        task = body['task']
        start = body['start']
        end = body['end']
        action = body['action']
        res = SchedulerService.reschedule_v2(cid, task, interval, start, end, action)
        return make_response(dict(code=201, data=res, status=True)), 201
