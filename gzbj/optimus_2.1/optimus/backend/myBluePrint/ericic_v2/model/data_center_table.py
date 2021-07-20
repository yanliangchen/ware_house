from sqlalchemy import Column, String, Integer, BOOLEAN
from backend.Model.connection import MyBase, SESSION


class DataCenterModel(MyBase):
    __tablename__ = 'data_center_bak'

    id = Column(String(50), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    mode = Column(BOOLEAN(), nullable=False, default=True)
    country = Column(String(50))
    province = Column(String(50))
    city = Column(String(50))
    system_name = Column(String(50), )
    cee_version = Column(String(50), )
    lcm_ip = Column(String(30), )
    lcm_user = Column(String(20), )
    lcm_pwd = Column(String(20), )
    openstackrc_dir = Column(String(100), )
    lcmrc_dir = Column(String(100), )
    timestamp = Column(Integer(), nullable=False)

    # version = Column(Integer(), nullable=False, default=0)
    def __init__(self, _id, name, mode, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                 lcm_pwd, openstackrc_dir, lcmrc_dir, timestamp):
        self.id = _id
        self.name = name
        self.mode = mode
        self.country = country
        self.province = province
        self.city = city
        self.system_name = system_name
        self.cee_version = cee_version
        self.lcm_ip = lcm_ip
        self.lcm_user = lcm_user
        self.lcm_pwd = lcm_pwd
        self.openstackrc_dir = openstackrc_dir
        self.lcmrc_dir = lcmrc_dir
        self.timestamp = timestamp

    @classmethod
    def get_one_by_name(cls, name):
        db_session = SESSION()
        try:
            res = db_session.query(cls).filter(cls.name == name).one_or_none()
        finally:
            db_session.close()
        return res
