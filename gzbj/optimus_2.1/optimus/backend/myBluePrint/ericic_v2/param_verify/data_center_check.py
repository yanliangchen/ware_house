from backend.myException.myExecption import MyParamCheckError
from flask import request
from backend.customer.paramCheck import ParamCheckBase
from backend.myException.myExecption import MyKeyError
from backend.myBluePrint.ericic_v2.base_dao.data_center_api_dao import datacenterApiDao


class DataCenterCheck(ParamCheckBase):

    def post(self, *args, **kwargs):
        body = request.get_json()
        dc_name = body["name"]
        mode = body.get('mode')
        country = body["country"]
        province = body["province"]
        city = body["city"]
        system_name = body["system_name"]
        cee_version = body['cee_version']
        lcm_ip = body['lcm_ip']
        lcm_user = body['lcm_user']
        lcm_pwd = body['lcm_pwd']
        openstackrc_dir = body['openstackrc_dir']
        lcmrc_dir = body['lcmrc_dir']

    def put(self, *args, **kwargs):
        body = request.get_json()

