from sqlalchemy import Column, String, Integer
from backend.Model.connection import MyBase


class FlavorModel(MyBase):
    __tablename__ = 'flavor'

    id = Column(String(40), primary_key=True, )
    uuid = Column(String(40), nullable=False)
    vcpu = Column(Integer(), nullable=False)
    memory = Column(Integer(), nullable=False)
    disk = Column(Integer(), nullable=False)
    data_center_id = Column(String(40), )
    timestamp = Column(Integer(), nullable=False)
    version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, uuid, vcpu, memory, disk, data_center_id, timestamp):
        self.id = _id
        self.uuid = uuid
        self.vcpu = vcpu
        self.memory = memory
        self.disk = disk
        self.data_center_id = data_center_id
        self.timestamp = timestamp
