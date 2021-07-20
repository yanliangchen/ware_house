import os
import time
import uuid
from flask import make_response
from sqlalchemy.exc import IntegrityError
from backend.myBluePrint.ericic.model.recordModel import Record
from backend.myBluePrint.ericic.model.vmHostView import VmHostView
from backend.myBluePrint.ericic.model.excelModel import InitWorkbook, BaseWrokbook
from backend.common.redisHandler import CACHE_RDS, JOB_ID_KEY
from backend.myBluePrint.ericic.service.dataCenterSercice import DataCenterService


class RecordService:

    @classmethod
    def split_data(cls, offset, limit):
        res = list()
        record_objs = Record.data_split(offset, limit)
        total_num = Record.count()
        for record_obj in record_objs:
            item = dict()
            item['id'] = record_obj.id
            item['name'] = record_obj.name
            item['data_center'] = record_obj.data_center
            item['cee_version'] = record_obj.cee_version
            item['create_time'] = record_obj.create_time
            item['data_load_time'] = record_obj.data_load_time
            res.append(item)
        data = dict(total_num=total_num, data=res)
        return data

    @classmethod
    def add_record(cls, name, data_center, cee_version):
        record_id = str(uuid.uuid4().hex)
        _time = int(time.time())
        create_time = data_load_time = timestamp = _time
        dc_infos, _ = DataCenterService.select_instances(50, 0)
        dc_id = ""
        if dc_infos:
            for dc_info in dc_infos:
                if dc_info.get("name") == data_center:
                    dc_id = dc_info.get('id')
                    break
        job_id = CACHE_RDS.get(JOB_ID_KEY + dc_id)
        if not job_id:
            job_id = ""
        excel_id = "%s_%s" % (dc_id, job_id)
        try:
            file_path = 'FilesFolder/ericic/script_output'
            for x in os.listdir(file_path):
                if excel_id in x and x.endswith('.xlsx'):
                    flag = True
                    break
            else:
                flag = False

            if not flag:
                return make_response(dict(status=False, code=400, message='excel not exist')), 400

            record_obj = Record(record_id, name, data_center, cee_version, create_time, data_load_time, timestamp, excel_id)
            record_obj.add()
        except IntegrityError:
            return make_response(dict(status=False, code=400, message='Duplicate name')), 400

        # # write vm info to excel
        # vm_infos = VmHostView.query_by_cname(data_center)
        # file = 'backend/myBluePrint/ericic/excel/%s.xlsx' % record_id
        # workbook = InitWorkbook(file).wb
        # wb = BaseWrokbook(file, workbook)
        #
        # sheet_infos = {
        #         'sheet': 'vm_info',
        #         'data': []
        #     }
        #
        # header = (
        #     'uuid', 'name', 'vcpu', 'memory', 'disk',
        #     'networks', 'create_time', 'status', 'power_state',
        #     'compute_state', 'host', 'availability_zone',
        #     'high_availability'
        # )
        # sheet_infos['data'].append(header)
        # if vm_infos:
        #     for vm_info in vm_infos:
        #         _tmp = []
        #         for k in header:
        #             _tmp.append(getattr(vm_info, k))
        #         sheet_infos['data'].append(_tmp)
        #
        #     _sheet = sheet_infos.get('sheet', None)
        #     data = sheet_infos.get('data', None)
        #     if _sheet and len(_sheet) >= 31:
        #         sheet = _sheet[-30:]
        #     else:
        #         sheet = _sheet
        #     if sheet:
        #         wb.init_sheet(titles=[sheet])
        #     if data and sheet:
        #         wb.write(input=data, sheet=sheet)

        return make_response(dict(status=True, code=201, data=record_id)), 201

    @classmethod
    def delete_record(cls, record_id):
        Record.delete_by_id(record_id)
