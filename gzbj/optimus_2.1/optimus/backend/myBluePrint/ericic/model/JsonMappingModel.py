from sqlalchemy import Column, String, Integer
from backend.Model.connection import MyBase


class JsonMappingModel(MyBase):
    __tablename__ = 'json_mapping'

    id = Column(String(50), primary_key=True)
    data = Column(String(), )
    timestamp = Column(Integer(), nullable=False)

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, data,timestamp):
        self.id = _id
        self.data = data
        self.timestamp =timestamp
