#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : SchedulerTaskHistoryDao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 17:20
# @Desc  :
from sqlalchemy import and_
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.refresh_task_history_table import RefreshTaskHistoryModel


class SchedulerTaskHistoryDao:

    @classmethod
    def get_history_by_cid(cls, cid, _filter, limit, offset):
        db_session = SESSION()
        try:
            if _filter:
                _filter = str(_filter).replace('.', ':')
                filter_entity = and_(RefreshTaskHistoryModel.dc_id == cid, RefreshTaskHistoryModel.task_name == _filter)
            else:
                filter_entity = and_(RefreshTaskHistoryModel.dc_id == cid, )
            res = db_session.query(RefreshTaskHistoryModel).filter(filter_entity).order_by(
                RefreshTaskHistoryModel.timestamp.desc()).offset(offset).limit(limit).all()
            total_num = db_session.query(RefreshTaskHistoryModel).filter(filter_entity).count()
        finally:
            db_session.close()
        return dict(res=res, total_num=total_num)
