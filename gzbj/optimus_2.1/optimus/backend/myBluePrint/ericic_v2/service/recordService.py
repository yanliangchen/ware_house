from flask import make_response
from sqlalchemy.exc import IntegrityError
from backend.myBluePrint.ericic_v2.model.record_table import Record
from backend.myBluePrint.ericic_v2.service.data_center_service import DataCenterService
from backend.myBluePrint.ericic_v2.base_dao.record_dao import RecordDao


class RecordService:

    @classmethod
    def split_data(cls, offset, limit, dc_id):
        res = list()
        record_objs = Record.data_split(dc_id, offset, limit)
        total_num = RecordDao.count_by_cid(dc_id)
        # dc_infos = DataCenterService.select_instance(dc_id)
        for record_obj in record_objs:
            item = dict()
            item['id'] = record_obj.id
            item['name'] = record_obj.name
            item['data_center'] = record_obj.data_center
            item['cid'] = record_obj.cid
            item['cee_version'] = record_obj.cee_version
            item['lcm_ip'] = record_obj.lcm_ip
            item['system_name'] = record_obj.system_name
            item['openrc_path'] = record_obj.openrc_path
            item['status'] = record_obj.status
            item['pid'] = record_obj.pid
            item['timestamp'] = record_obj.timestamp
            item['traceback'] = record_obj.traceback
            res.append(item)
        data = dict(total_num=total_num, data=res)
        return data

    @classmethod
    def add_record(cls, name, dc_id):
        try:
            record_id = RecordDao.add_record(name, dc_id)
        except IntegrityError:
            return make_response(dict(status=False, code=400, message='Duplicate name')), 400
        return make_response(dict(status=True, code=201, id=record_id)), 201

    @classmethod
    def delete_record(cls, record_id):
        RecordDao.delete_record(record_id)
