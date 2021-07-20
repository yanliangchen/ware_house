from flask import request
from backend.customer.paramCheck import ParamCheckBase
from backend.myException.myExecption import MyParamCheckError, MyKeyError
from backend.myBluePrint.ericic.service import dataCenterSercice


class UploadCheck(ParamCheckBase):

    def post(self, *args, **kwargs):
        ALLOWED_EXTENSIONS = set(['json'])
        id_res = request.form.get("id")
        f = request.files['json_file']
        if '.' in f.filename and f.filename.rsplit('.', 1)[1] not in ALLOWED_EXTENSIONS:
            raise MyParamCheckError('The file format supports JSON only')
        if id_res is None or len(id_res.strip()) == 0:
            raise MyParamCheckError('The Data Center ID field cannot be empty')
        try:
            request.files['json_file']
            request.form['id']
        except KeyError as key:
            raise MyKeyError(key)
        res = dataCenterSercice.DataCenterService.select_instance(id_res)
        if not res:
            raise MyParamCheckError('The Data Center ID field is incorrectness')