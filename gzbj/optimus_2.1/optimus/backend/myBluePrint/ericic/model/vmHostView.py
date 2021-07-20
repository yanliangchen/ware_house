from backend.Model.connection import BaseView, SESSION
from sqlalchemy import Column, String, Integer, BOOLEAN
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel


class VmHostView(BaseView):
    # this cls is orm for view, so can not use this cls to insert , update , delete, only select
    __tablename__ = 'vm_host_view'

    vm_id = Column(String(50), primary_key=True)
    uuid = Column(String(50), )
    name = Column(String(50), )
    status = Column(String(10), )
    power_state = Column(String(10), )
    create_time = Column(String(50), )
    networks = Column(String(50), )
    vcpu = Column(Integer(), )
    memory = Column(Integer(), )
    disk = Column(Integer(), )
    tenant = Column(String(50), )
    host_id = Column(String(50), primary_key=True)
    host = Column(String(50), )
    host_aggregate = Column(String(50), )
    availability_zone = Column(String(50), )
    compute_state = Column(BOOLEAN(), )
    cpu_percent = Column(String(50), )
    memory_percent = Column(String(50), )
    disk_percent = Column(String(50), )
    data_center_id = Column(String(50), )
    timestamp = Column(Integer(), )

    # __table_args__ = (
    #     PrimaryKeyConstraint('vm_id', 'host_id'),
    # )

    @classmethod
    def query_by_cname(cls, cname):
        db_session = SESSION()
        try:
            # dc_obj = DataCenterModel.get_one_by_name(cname).filter(cls.name == cname).one_or_none()
            dc_obj = db_session.query(DataCenterModel).filter(DataCenterModel.name == cname).one_or_none()
            if dc_obj:
                res = db_session.query(cls).filter(cls.data_center_id == dc_obj.id).all()
            else:
                raise Exception('wrong name')
        finally:
            db_session.close()
        return res

    @classmethod
    def count_by_cid(cls, cid):
        db_session = SESSION()
        try:
            res = db_session.query(cls).filter(cls.data_center_id == cid).count()
        finally:
            db_session.close()
        return res

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
