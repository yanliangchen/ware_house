from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.hostconfigDataService import HostConfigDataService
from flask import make_response, request


class HostConfigData(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        dc_id = request.args.get('dc_id')
        resp = HostConfigDataService.select_host_config(dc_id=dc_id)
        response = make_response(dict(status=True, data=resp, code=200))
        return response

