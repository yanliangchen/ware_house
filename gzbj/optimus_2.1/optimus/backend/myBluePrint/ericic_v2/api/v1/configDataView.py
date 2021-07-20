from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.configDataService import ConfigDataService
from flask import make_response, request


class ConfigData(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        dc_id = request.args.get('dc_id')
        tenants_resp = ConfigDataService.select_config(dc_id=dc_id)
        response = make_response(dict(status=True, data=tenants_resp, code=200))
        return response
