from sqlalchemy import Column, String, Integer
from backend.Model.connection import MyBase, SESSION


class Record(MyBase):
    __tablename__ = 'record'

    id = Column(String(50), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    data_center = Column(String(255), )
    cid = Column(String(255), nullable=False)
    cee_version = Column(String(255), )
    lcm_ip = Column(String(255), )
    system_name = Column(String(255), )
    openrc_path = Column(String(255), )
    status = Column(String(255))
    pid = Column(String(255))
    timestamp = Column(Integer(), nullable=False)
    traceback = Column(String(255))
    version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, name, data_center, cid, cee_version, lcm_ip, system_name, openrc_path, status, timestamp):
        self.id = _id
        self.name = name
        self.data_center = data_center
        self.cid = cid
        self.cee_version = cee_version
        self.lcm_ip = lcm_ip
        self.system_name = system_name
        self.openrc_path = openrc_path
        self.status = status
        # self.pid = pid
        self.timestamp = timestamp
        # self.traceback = traceback

    @classmethod
    def data_split(cls, cid, offset, limit):
        db_session = SESSION()
        try:
            # offset = (offset - 1) * limit
            res = db_session.query(cls).filter(cls.cid == cid).order_by(cls.timestamp.desc()).limit(limit).offset(
                offset).all()
        finally:
            db_session.close()
        return res
