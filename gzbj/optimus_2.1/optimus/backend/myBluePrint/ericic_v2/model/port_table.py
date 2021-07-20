from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer, Text, func


class PortModel(EriCICBase):
    __tablename__ = 'port_table'
    dc_id = Column(String(50), nullable=False)
    id = Column(String(32), primary_key=True)
    port_data = Column(Text(), nullable=False)
    timestamp = Column(Integer(), nullable=False, onupdate=func.now())

    def __init__(self, _id,dc_id, port_data, timestamp):
        self.id = _id
        self.port_data = port_data
        self.timestamp = timestamp
        self.dc_id = dc_id
