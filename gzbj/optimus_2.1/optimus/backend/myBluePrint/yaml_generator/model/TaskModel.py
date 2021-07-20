import traceback
from flask import g
from backend.common.loghandler import BDLog
from sqlalchemy import and_, or_
from sqlalchemy import Column, String, Integer, BOOLEAN
from backend.Model.connection import BASE, SESSION


class Task(BASE):
    __tablename__ = 'task'

    id = Column(String(40), primary_key=True, )
    user = Column(String(20), nullable=False)
    project_name = Column(String(20), nullable=False)
    site_name = Column(String(20), nullable=False, )
    cee_version = Column(String(20), nullable=False, )
    input = Column(String(40), )
    output = Column(String(40), )
    status = Column(String(40), nullable=False, default='running')
    timestamp = Column(Integer(), nullable=False)
    version = Column(Integer(), nullable=False, default=0)
    visible = Column(BOOLEAN(), nullable=False, default=True)

    def __init__(self, _id, user, project_name, site_name, cee_version, status, timestamp):
        self.id = _id
        self.user = user
        self.project_name = project_name
        self.site_name = site_name
        self.cee_version = cee_version
        self.status = status
        self.timestamp = timestamp
        self.input = 'FilesFolder/yaml_gen/%s/upload' % _id
        self.output = 'FilesFolder/yaml_gen/%s/download' % _id

    def add(self):
        db_session = SESSION()
        try:
            db_session.add(self)
            db_session.commit()
        except Exception:
            db_session.rollback()
            e = traceback.format_exc()
            BDLog.info('%s - %s' % (g.r_id, e))
            raise Exception('DB error')
        finally:
            db_session.close()

    @classmethod
    def get_all_task(cls):
        db_session = SESSION()
        try:
            # db_session = SESSION()
            # res = db_session.query(Task).filter(Task.visible is True).order_by(Task.timestamp.desc()).all()
            res = db_session.query(Task).filter(Task.visible == 1).order_by(Task.timestamp.desc()).all()
            print(res)
        finally:
            db_session.close()
        return res

    @classmethod
    def update_status_by_id(cls, _id, status):
        db_session = SESSION()
        task = db_session.query(Task).filter(Task.id == _id).one_or_none()
        _update = {Task.status: status, Task.version: Task.version + 1}
        _query = and_(Task.id == _id, Task.version == task.version)
        try:
            res = db_session.query(Task).filter(_query).update(_update)
            db_session.commit()
            if not res:
                cls.update_status_by_id(_id, status)
        except Exception:
            db_session.rollback()
            e = traceback.format_exc()
            BDLog.info('%s - %s' % (g.r_id, e))
            raise Exception('DB error')
        finally:
            db_session.close()

    @classmethod
    def invisible_history_items(cls, id_list):
        db_session = SESSION()
        args = tuple()
        for _id in id_list:
            args += (Task.id == _id,)
        _update = {Task.visible: False}
        try:
            db_session.query(Task).filter(or_(*args)).update(_update)
            db_session.commit()
        except Exception:
            db_session.rollback()
            e = traceback.format_exc()
            BDLog.info('%s - %s' % (g.r_id, e))
            raise Exception('DB error')
        finally:
            db_session.close()

# update