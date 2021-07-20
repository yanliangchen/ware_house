#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : mongo_tes t.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/2/4 11:15
# @Desc  :
from mongoengine import Document, StringField, BinaryField


class Record(Document):
    id = StringField(primary_key=True)
    test = BinaryField(required=True)


from celery_app import celery_app
from backend.customer.myCustomer import APiMethodView


class MongoTest(APiMethodView):

    def get(self, *args, **kwargs):
        res = Record.objects(id='gaofzhan')
        print(res[0].id)
        celery_app.send_task('taskModel.method_view.record_gen_task', args=('1', '1'))
        celery_app.send_task('taskModel.method_view.record_gen_task', args=('2', '2'))
        return dict(j='1')
