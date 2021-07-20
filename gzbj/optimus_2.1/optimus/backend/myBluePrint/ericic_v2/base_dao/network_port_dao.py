#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : network_port_dao.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/24 9:54
# @Desc  :
from backend.Model.connection import SESSION, and_
from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.neutron_port_table import NeutronPortTable

from backend.common.loghandler import BDLog
from backend.myBluePrint.ericic_v2.model.port_table import PortModel
# from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel


class NetworkPortDao:

    @classmethod
    def get_dc_vm_entity(cls, cid, vid):
        db_session = SESSION()
        try:
            dc_entity = db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).one_or_none()
            _filter = and_(NovaModel.dc_id == cid, NovaModel.id == vid)
            vm_entity = db_session.query(NovaModel).filter(_filter).one_or_none()
        finally:
            db_session.close()
        return dict(vm_entity=vm_entity, dc_entity=dc_entity)

    @classmethod
    def get_port_entity(cls, cid, vid):
        db_session = SESSION()
        try:
            _filter = and_(NeutronPortTable.device_id == vid, NeutronPortTable.dc_id == cid)
            port_entities = db_session.query(NeutronPortTable).filter(_filter).all()
        finally:
            db_session.close()
        return port_entities

    @classmethod
    def save_port_data(cls, _id, port_data,dc_id):
        db_session = SESSION()
        try:
            import  time
            timestamp = time.time()
            db_session.query(PortModel).filter(PortModel.id == _id).delete()
            p_m = PortModel(dc_id=dc_id,_id=_id,port_data=port_data,timestamp=timestamp)
            db_session.add(p_m)

            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise e

        finally:
            db_session.close()


    @classmethod
    def select_port_data(cls,_id):
        db_session = SESSION()
        try:

            network_data = db_session.query(PortModel).filter(PortModel.id== _id).all()
            network_data= network_data[0].port_data
            return  network_data

        except Exception as e:
            BDLog.error(e)
            raise e
        finally:
            db_session.close()
