import os
import base64
from backend.myBluePrint.ericic.model.recordModel import Record

class RecordResultService:

    @classmethod
    def download_record(cls, record_id):
        file_path = 'FilesFolder/ericic/script_output/'
        # file = 'backend/myBluePrint/ericic/excel/%s.xlsx' % record_id
        record_objs = Record.get_one_by_id(record_id)
        ex_excel_file = record_objs.excel_file
        for x in os.listdir(file_path):
            if x.startswith(ex_excel_file) and x.endswith('.xlsx'):
                _file = x
                break
        file = file_path + _file
        if os.path.exists(file):
            with open(file, 'rb') as f:
                fd = f.read()
            base64_str = base64.b64encode(fd)
            data = dict(total_num=1, data=base64_str.decode('utf-8'))
            return data
        else:
            return dict(total_num=0, data=None,
                        error=True,
                        message="excel file not exist")
