import os
import base64
from backend.common.redisHandler import CACHE_RDS, JOB_ID_KEY
from backend.common.scriptHandler import call_subprocess
from backend.myBluePrint.ericic.model.dataCenterModel\
    import DataCenterModel

OFFLINE_JSON_PATH = 'FilesFolder/ericic/uploads/json_files/'

class DownloadService:

    @classmethod
    def download(cls, dc_id):
        dc_obj = DataCenterModel.get_one_by_id(dc_id)
        if dc_obj.mode:
            dc_status = "online"
        else:
            dc_status = "offline"

        file_path = 'FilesFolder/ericic/script_output/'
        excel_file = "%s*.xlsx" % dc_id
        json_file = OFFLINE_JSON_PATH + dc_id + ".json"
        job_id = CACHE_RDS.get(JOB_ID_KEY + dc_id)
        if not job_id:
            job_id = ""

        def _search(path, start_str, end_str):
            _file = ""
            flag = False
            for x in os.listdir(path):
                if x.startswith(start_str) and x.endswith(end_str):
                    _file = x
                    flag = True
                    break
            return _file, flag

        if dc_status == "online":
            # file = file_path + "%s_%s" % (dc_id, job_id)
            _file, _ = _search(file_path, "%s_%s" % (dc_id, job_id), '.xlsx')
            file = file_path + _file
        elif dc_status == "offline":
            _file, flag = _search(file_path, dc_id, '.xlsx')
            # test code
            # flag = False
            _json_file = json_file.split(os.sep)[-1]
            if not flag:
                try:
                    infocollect = "infocollect-Ericic4ceeNext"
                    call_subprocess("cp -rf FilesFolder/ericic/script/%s.tar /tmp" % infocollect)
                    call_subprocess("tar -xf /tmp/%s.tar -C /tmp" % infocollect)
                    call_subprocess("cp -rf %s /tmp/%s/" % (json_file, infocollect))
                    call_subprocess("cd /tmp/%s; python test_case/test_optimue_001.py -s %s -f %s -n %s"
                                    % (infocollect, dc_status, _json_file, dc_id))
                    call_subprocess("cp -rf /tmp/%s/output/%s %s" % (infocollect, excel_file, file_path))
                    call_subprocess("rm -rf /tmp/%s" % infocollect)
                    call_subprocess("rm -rf /tmp/%s.tar" % infocollect)
                except Exception as e:
                    print(e)
                    return dict(error=True)
                _file, _ = _search(file_path, dc_id, '.xlsx')
            file = file_path + _file

        if os.path.exists(file):
            with open(file, 'rb') as f:
                fd = f.read()
            base64_str = base64.b64encode(fd)
            data = dict(total_num=1, data=base64_str.decode('utf-8'))
            return data
        else:
            return dict(total_num=0, data=None)
