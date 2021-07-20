#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/10 10:06
# @Desc  :
from flask import g
import traceback
from backend.common.loghandler import BDLog
from config import RETRY_TIME
from backend.scheduler_handler.task_mapping import STATIC_REFRESH, DYNAMIC_REFRESH
from backend.myException.myExecption import MyRuntimeError
from backend.Model.connection import SESSION, and_
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.db_refresh_task import DBRefreshTaskModel


class SchedulerDao:

    @classmethod
    def get_dc_by_id(cls, cid):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).one_or_none()
        finally:
            db_session.close()
        return dc_entity

    @classmethod
    def get_refresh_task_entities(cls, cid):
        db_session = SESSION()
        try:
            dynamic_entity = db_session.query(DBRefreshTaskModel).filter(
                DBRefreshTaskModel.id == '%s:%s' % (cid, DYNAMIC_REFRESH)).one_or_none()
            static_entity = db_session.query(DBRefreshTaskModel).filter(
                DBRefreshTaskModel.id == '%s:%s' % (cid, STATIC_REFRESH)).one_or_none()
        finally:
            db_session.close()
        return dict(static=static_entity, dynamic=dynamic_entity)

    @classmethod
    def reschedule_task(cls, task_id, **kwargs):
        _update = {}
        db_session = SESSION()
        try:
            this = db_session.query(DBRefreshTaskModel).filter(DBRefreshTaskModel.id == task_id).one_or_none()
            if this:
                for k, v in kwargs.items():
                    if k == 'id' or k == 'version':
                        continue
                    _update[getattr(DBRefreshTaskModel, k)] = v
                _update[DBRefreshTaskModel.version] = this.version + 1
                # _update[DBRefreshTaskModel.timestamp] = int(time.time())
                _query = and_(DBRefreshTaskModel.id == task_id, DBRefreshTaskModel.version == this.version)
                try:
                    res = db_session.query(DBRefreshTaskModel).filter(_query).update(_update)
                    db_session.commit()
                    if not res:
                        cls.reschedule_task(task_id, **kwargs)
                except Exception:
                    db_session.rollback()
                    e = traceback.format_exc()
                    BDLog.info('%s - %s' % (g.r_id, e))
                    raise MyRuntimeError('service error', 503)
                return True
            else:
                return False
        finally:
            db_session.close()

    # @classmethod
    # def reschedule_task(cls, task_id, start, end, interval):
    #     update_loop = 0
    #     while True:
    #         db_session = SESSION()
    #         try:
    #             this = db_session.query(DBRefreshTaskModel).filter(DBRefreshTaskModel.id == task_id).one_or_none()
    #             if this:
    #                 _update = dict()
    #                 _update[DBRefreshTaskModel.version] = this.version + 1
    #                 _update[DBRefreshTaskModel.start] = start
    #                 _update[DBRefreshTaskModel.end] = end
    #                 _update[DBRefreshTaskModel.interval] = interval
    #                 _query = and_(DBRefreshTaskModel.id == task_id, DBRefreshTaskModel.version == this.version)
    #                 if db_session.query(DBRefreshTaskModel).filter(_query).update(_update):
    #                     db_session.commit()
    #                     break
    #                 update_loop += 1
    #                 if update_loop > RETRY_TIME:
    #                     raise MyRuntimeError('server is busy, out of the retry time', 503)
    #         finally:
    #             db_session.close()
    #     return True

    # @classmethod
    # def data_consist_keep(cls, cid):
    #     db_session = SESSION()
    #     try:
    #         db_session.add_all([])
    #     except Exception as e:
    #         pass
    #     finally:
    #         pass
    #     pass
