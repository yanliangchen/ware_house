from backend.Model.connection import BaseView
from sqlalchemy import Column, String, Integer


class VmModelView(BaseView):
    __tablename__ = 'vm_view'

    id = Column(String(50), primary_key=True, )
    uuid = Column(String(50), )
    name = Column(String(50), )
    status = Column(String(50), )
    power_state = Column(String(50), )
    create_time = Column(String(50), )
    networks = Column(String(50), )
    vcpu = Column(Integer(), )
    memory = Column(Integer(), )
    disk = Column(Integer(), )
    host_id = Column(Integer(), )
    tenant = Column(String(50), )
    data_center_id = Column(String(50), )
    timestamp = Column(Integer(), )
