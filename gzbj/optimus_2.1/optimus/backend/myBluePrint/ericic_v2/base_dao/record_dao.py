#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : record_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/2/25 10:26
# @Desc  :
import time
import uuid
from celery_app import celery_app
from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION, and_
from backend.myBluePrint.ericic_v2.model.record_table import Record
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myException.myExecption import MyDataConsistencyError, MyRuntimeError
from backend.myBluePrint.ericic_v2.mongo_post.record_post import RecordPost


class RecordDao:

    @classmethod
    def add_record(cls, name, dc_id):
        db_session = SESSION()
        _id = uuid.uuid4().hex
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == dc_id).one_or_none()
            if dc_entity:
                record = Record(_id, name, dc_entity.name, dc_id, dc_entity.cee_version, dc_entity.lcm_ip,
                                dc_entity.system_name, dc_entity.openstackrc_dir, 'waiting', int(time.time()))
                db_session.add(record)
                if db_session.query(DataCenterModel).filter(
                        and_(DataCenterModel.id == dc_id, DataCenterModel.version == dc_entity.version)).update(
                    {'version': dc_entity.version + 1}):
                    celery_app.send_task('optimus_executor.method_view.gen_excel', task_id=_id, args=(_id, dc_id))
                    db_session.commit()
                else:
                    raise MyDataConsistencyError('the specified dc has been deleted')
            else:
                raise MyRuntimeError('can not find the specified dc', 400)
        except Exception as e:
            db_session.rollback()
            BDLog.info(e)
            raise e
        finally:
            db_session.close()
        return _id

    @classmethod
    def delete_record(cls, record_id):
        db_session = SESSION()
        try:
            if db_session.query(Record).filter(and_(Record.id == record_id, Record.status == 'running')).one_or_none():
                raise MyRuntimeError('the running can not be deleted', 400)
            db_session.query(Record).filter(Record.id == record_id).delete()
            RecordPost.objects(id=record_id).delete()
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.info(e)
            raise e
        finally:
            db_session.close()

    @classmethod
    def count_by_cid(cls, cid):
        db_session = SESSION()
        try:
            res = db_session.query(Record).filter(Record.cid == cid).count()
        finally:
            db_session.close()
        return res
