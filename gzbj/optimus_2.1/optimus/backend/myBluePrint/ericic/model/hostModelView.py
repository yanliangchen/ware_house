from backend.Model.connection import BaseView
from sqlalchemy import Column, String, Integer


class HostModelView(BaseView):
    __tablename__ = 'host_view'

    host_id = Column(String(50), primary_key=True, )
    host = Column(String(50), )
    host_aggregate = Column(String(50), )
    availability_zone = Column(String(50), )
    compute_state = Column(String(50), )
    cpu_percent = Column(String(50), )
    memory_percent = Column(String(50), )
    disk_percent = Column(String(50), )
    data_center_id = Column(String(50), )
    cee_version = Column(String(50), )
    timestamp = Column(Integer(), )
