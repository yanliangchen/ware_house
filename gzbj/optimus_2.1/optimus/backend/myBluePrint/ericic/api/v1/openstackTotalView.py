from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.paramVerify.openstackTotalVerify import OpenstackTotalViewVerify


class OpenstackTotalView(APiMethodView):
    check_cls = OpenstackTotalViewVerify

    def post(self, *args, **kwargs):
        body = request.get_json()

