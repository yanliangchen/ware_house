#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : sheduler_task_verify.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/11 11:15
# @Desc  :
import logging
from flask import request
from backend.myException.myExecption import MyKeyError, MyParamCheckError, MyTypeError
from backend.customer.paramCheck import ParamCheckBase


class SchedulerTaskVerify(ParamCheckBase):

    def post(self, *args, **kwargs):
        body = request.get_json()
        logging.info(body)
        if not body:
            raise MyParamCheckError('body is a must')
        try:
            body['cid']
            action = body['action']
            task = body['task']
        except KeyError as e:
            raise MyKeyError(e)
        if action not in ['pause', 'resume']:
            raise MyParamCheckError('action must be pause or resume')
        if task not in ['static', 'dynamic']:
            raise MyParamCheckError('task must be static or dynamic')

    def put(self, *args, **kwargs):
        body = request.get_json()
        if not body:
            raise MyParamCheckError('body is a must')
        try:
            body['cid']
            interval = body['interval']
            task = body['task']
        except KeyError as e:
            raise MyKeyError(e)
        try:
            int(interval)
        except TypeError as e:
            raise MyTypeError(e)
        if task not in ['static', 'dynamic']:
            raise MyParamCheckError('task must be static or dynamic')
