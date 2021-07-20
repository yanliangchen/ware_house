#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : RecordPost.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/2/4 15:56
# @Desc  : 
from mongoengine import Document, StringField, BinaryField, IntField


class RecordPost(Document):
    meta = {'collection': 'record'}

    id = StringField(primary_key=True)
    content = BinaryField(required=True)
    cid = StringField()
    timestamp = IntField()
