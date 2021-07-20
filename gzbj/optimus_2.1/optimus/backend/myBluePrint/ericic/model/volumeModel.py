from sqlalchemy import Column, String, Integer, BOOLEAN
from backend.Model.connection import MyBase


class VolumeModel(MyBase):
    __tablename__ = 'volume_info'

    id = Column(String(40), primary_key=True, )
    uuid = Column(String(40), nullable=False)

    name = Column(String(40), nullable=False)
    status = Column(String(40), nullable=False)
    size = Column(Integer(), nullable=False)
    type = Column(Integer(), nullable=False)
    bootable = Column(BOOLEAN(), nullable=False)
    vm_id = Column(String(40), )
    data_center_id = Column(String(40), )
    timestamp = Column(Integer(), nullable=False)
    version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, uuid, name, status, size, type, bootable, vm_id, data_center_id, timestamp):
        self.id = _id
        self.uuid = uuid
        self.name = name
        self.status = status
        self.size = size
        self.type = type
        self.bootable = bootable
        self.vm_id = vm_id
        self.data_center_id = data_center_id
        self.timestamp = timestamp
