from backend.Model.connection import MyBase, SESSION
from sqlalchemy import Column, String, Integer, UniqueConstraint


class VmInfo(MyBase):
    __tablename__ = 'vm_info2'

    id = Column(String(50), primary_key=True, )
    uuid = Column(String(50), )
    name = Column(String(100), )
    status = Column(String(10), )
    power_state = Column(String(10), )
    create_time = Column(String(50), )
    networks = Column(String(50), )
    flavor_id = Column(String(50), )
    tenant_id = Column(String(50), )
    host_id = Column(String(50), )
    data_center_id = Column(String(50), )
    instance_name = Column(String(50))
    timestamp = Column(Integer(), )

    __table_args__ = (
        UniqueConstraint('uuid', 'host_id'),
    )

    def __init__(self, _id, uuid, name, status, power_state, create_time, networks, flavor_id, tenant_id, host_id,
                 data_center_id, instance_name, timestamp):
        self.id = _id
        self.uuid = uuid
        self.name = name
        self.status = status
        self.power_state = power_state
        self.create_time = create_time
        self.networks = networks
        self.flavor_id = flavor_id
        self.tenant_id = tenant_id
        self.host_id = host_id
        self.data_center_id = data_center_id
        self.instance_name = instance_name
        self.timestamp = timestamp

    @classmethod
    def get_entities_with_host_id(cls, host_id):
        db_session = SESSION()
        try:
            res = db_session.query(cls).filter(cls.host_id == host_id).all()
        finally:
            db_session.close()
        return res
