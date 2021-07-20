import traceback
from flask import g
from backend.common.loghandler import BDLog
from backend.Model.connection import MyBase, SESSION
from sqlalchemy import Column, String, Integer
from backend.myBluePrint.ericic.model.vmModel import VmInfo


class HostInfo(MyBase):
    __tablename__ = 'host_info2'

    id = Column(String(50), primary_key=True, )
    name = Column(String(50), unique=True, )
    host_aggregate = Column(String(50), )
    availability_zone = Column(String(50), )
    compute_state = Column(String(50), )
    total_cpu = Column(Integer(), )
    free_cpu = Column(Integer(), )
    total_memory = Column(Integer(), )
    free_memory = Column(Integer(), )
    total_disk = Column(Integer(), )
    free_disk = Column(Integer(), )
    data_center_id = Column(String(50), )
    timestamp = Column(Integer(), )

    def __init__(self, _id, name, host_aggregate, availability_zone, compute_state, total_cpu, free_cpu, total_memory,
                 free_memory, total_disk, free_disk, data_center_id, timestamp):
        self.id = _id
        self.name = name,
        self.host_aggregate = host_aggregate
        self.availability_zone = availability_zone
        self.compute_state = compute_state
        self.total_cpu = total_cpu
        self.free_cpu = free_cpu
        self.total_memory = total_memory
        self.free_memory = free_memory
        self.total_disk = total_disk
        self.free_disk = free_disk
        self.data_center_id = data_center_id
        self.timestamp = timestamp

    @classmethod
    def refresh_infos(cls, host_info_dict, vm_info_dict, cid):
        db_session = SESSION()
        try:
            # delete the related data in db
            host_entities = db_session.query(cls).filter(cls.data_center_id == cid).all()
            for host_entity in host_entities:
                host_id = host_entity.id
                db_session.query(VmInfo).filter(VmInfo.host_id == host_id).delete()
            db_session.query(cls).filter(cls.data_center_id == cid).delete()
            # gen related data by the input the insert all the generated db entity
            gen_vm_list = list()
            gen_host_list = list()
            for k, v in host_info_dict.items():
                gen_host_list.append(HostInfo(**v))
            db_session.add_all(gen_host_list)
            for k, v in vm_info_dict.items():
                gen_vm_list.append(VmInfo(**v))
            db_session.add_all(gen_vm_list)
            db_session.commit()
        except Exception:
            db_session.rollback()
            e = traceback.format_exc()
            BDLog.info('%s - %s' % (g.r_id, e))
            raise Exception('DB error')
        finally:
            db_session.close()

    @classmethod
    def count_by_cid(cls, cid):
        db_session = SESSION()
        try:
            res = db_session.query(cls).filter(cls.data_center_id == cid).count()
        finally:
            db_session.close()
        return res
    #
    # @classmethod
    # def get_one_by_id(cls, _id):
    #     db_session = SESSION()
    #     try:
    #         res = db_session.query(cls).filter(cls.id == _id).one_or_none()
    #     finally:
    #         db_session.close()
    #     return res

# @classmethod
# def split_data_by_query(cls, column_list, query_dict, offset, limit, sort, order):
#     column_args = list()
#     for column in column_list:
#         entity = getattr(cls, column, None)
#         if not entity:
#             continue
#         column_args.append(entity)
#     and_entity_list = list()
#     for k, v in query_dict.items():
#         filter_attr = getattr(cls, k, None)
#         if not filter_attr:
#             continue
#         or_entity_list = list()
#         for query in v:
#             filter_entity = filter_attr.like('%{query}%'.format(query=query))
#             or_entity_list.append(filter_entity)
#         or_entity = or_(*or_entity_list)
#         and_entity_list.append(or_entity)
#     filter_args = and_(*and_entity_list)
#     sort_entity = getattr(cls, sort) if getattr(cls, sort, None) else cls.timestamp
#     order_entity = sort_entity.asc() if order == 'asc' else sort_entity.desc()
#     res = db_session.query(cls).with_entities(*column_args).filter(filter_args).order_by(order_entity).offset(
#         offset).limit(limit).all()
#     return res
