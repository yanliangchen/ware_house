from flask import request
from backend.customer.paramCheck import ParamCheckBase
from backend.myException.myExecption import MyKeyError


class OpenstackTotalViewVerify(ParamCheckBase):

    pass
    # def get(self, *args, **kwargs):
    #     print('xxxx')

    # def post(self, *args, **kwargs):
    #     body = request.get_json()
    #     try:
    #         lcm_ip = body['data_center_id']
    #         lcm_user = body['lcm_user']
    #         lcm_pwd = body['lcm_pwd']
    #     except KeyError as e:
    #         raise MyKeyError(e)
