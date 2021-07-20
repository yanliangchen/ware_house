from backend.myBluePrint.ericic.paramVerify.UploadCheck import UploadCheck
from backend.myBluePrint.ericic.service.uploadService import uploadService
from backend.myException.myExecption import MyParamCheckError
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.JsonMappingService import JsonMappingService
from werkzeug.utils import secure_filename
from flask import make_response
from flask import request
import json
import time
import os


class Upload(APiMethodView):
    check_cls = UploadCheck

    def post(self, *args, **kwargs):
        ALLOWED_EXTENSIONS = set(['json'])
        pre_times = int(time.time())
        dc_id = request.form.get('id')
        f = request.files['json_file']
        file_name = f.filename.replace(f.filename, '{}.json'.format(dc_id))

        json_read =  json.loads(f.stream.read().decode('utf-8'))

        str_json = str(json_read)
        JsonMappingService.delete_json_mapping(dc_id=dc_id)
        JsonMappingService.add_json_map(_id=dc_id, data=str_json)
        if '.' in f.filename and f.filename.rsplit('.', 1)[1] not in ALLOWED_EXTENSIONS:
            raise MyParamCheckError('The file format supports JSON only')
        else:
            uploads_path = os.getcwd() + '/FilesFolder/ericic/'
            if not os.path.exists(uploads_path + 'uploads'):
                os.mkdir(uploads_path + 'uploads')
            if not os.path.exists(uploads_path + 'uploads/json_files'):
                os.mkdir(uploads_path + 'uploads/json_files')
            upload_path = os.path.join(uploads_path, 'uploads/json_files', secure_filename(file_name))

            with open(upload_path, 'w', encoding='utf8') as f:
                f.write(json.dumps(json_read))
        try:
            json_read['flavor']
            json_read['compute_info']
            json_read['aggregate']
            json_read['vm_info']
            json_read['tenants']
            json_read['volume']

        except Exception as e:
            raise MyParamCheckError('The Json file content format is incorrect')

        flavor_info = json_read['flavor']
        hosts_info = json_read['compute_info']
        az_ha_info = json_read['aggregate']
        vm_info = json_read['vm_info']
        tenants = json_read['tenants']
        volume_info = json_read['volume']
        uploadService.upload(pre_times=pre_times, dc_id=dc_id, flavor_info=flavor_info, hosts_info=hosts_info,
                             az_ha_info=az_ha_info, vm_info=vm_info,
                             tenants=tenants, volume_info=volume_info)



        response = make_response(dict(status=True, message='upload json file success', code=200))
        return response

