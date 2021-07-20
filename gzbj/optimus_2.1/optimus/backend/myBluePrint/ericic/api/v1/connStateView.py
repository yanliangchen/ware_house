from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.connStatusService import ConnStatusService
from backend.myBluePrint.ericic.paramVerify.connectStatusVerify import ConnStatusVerify


class ConnectStatusView(APiMethodView):
    check_cls = ConnStatusVerify

    def get(self, *args, **kwargs):
        cid = request.args.get('cid')
        res = ConnStatusService.check_by_cid(cid)
        return make_response(dict(code=200, status=True, message=res['msg'], data=res['status'])), 200

    def post(self, *args, **kwargs):
        body = request.get_json()
        lcm_ip = body['lcm_ip']
        lcm_user = body['lcm_user']
        lcm_pwd = body['lcm_pwd']
        res = ConnStatusService.check_by_ip(lcm_ip, lcm_user, lcm_pwd)
        return make_response(dict(code=200, status=True, message=res['msg'], data=res['status'])), 200
