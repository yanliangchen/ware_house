from sqlalchemy import Column, String, Integer
from backend.Model.connection import MyBase, SESSION


class Record(MyBase):
    __tablename__ = 'snapshot'

    id = Column(String(50), primary_key=True, )
    name = Column(String(50), nullable=False, unique=True)
    data_center = Column(String(20), nullable=False)
    cee_version = Column(String(40), nullable=False)
    create_time = Column(Integer(), nullable=False)
    data_load_time = Column(Integer(), nullable=False)
    timestamp = Column(Integer(), nullable=False)
    version = Column(Integer(), nullable=False, default=0)
    excel_file = Column(String(100), nullable=False)

    def __init__(self, _id, name, data_center, cee_version, create_time, data_load_time, timestamp, excel_file):
        self.id = _id
        self.name = name
        self.data_center = data_center
        self.cee_version = cee_version
        self.create_time = create_time
        self.data_load_time = data_load_time
        self.timestamp = timestamp
        self.excel_file = excel_file

    @classmethod
    def data_split(cls, offset, limit):
        db_session = SESSION()
        try:
        # offset = (offset - 1) * limit
            res = db_session.query(cls).order_by(cls.timestamp.desc()).limit(limit).offset(offset).all()
        finally:
            db_session.close()
        return res

    @classmethod
    def get_one_by_id(cls, _id):
        db_session = SESSION()
        try:
            res = db_session.query(cls).filter(cls.id == _id).one_or_none()
        finally:
            db_session.close()
        return res
