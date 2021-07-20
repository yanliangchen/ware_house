from sqlalchemy import Column, String, Integer
from backend.Model.connection import MyBase


class TenantModel(MyBase):
    __tablename__ = 'tenant_info'

    id = Column(String(40), primary_key=True, )
    uuid = Column(String(40), )
    name = Column(String(100), )
    data_center_id = Column(String(40), )
    timestamp = Column(Integer(), nullable=False)
    version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, uuid, name, data_center_id, timestamp):
        self.id = _id
        self.uuid = uuid
        self.name = name
        self.data_center_id = data_center_id
        self.timestamp = timestamp
