from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.cpuLayoutService import CPULayoutService


class CPULayoutView(APiMethodView):

    def get(self, *args, **kwargs):
        host_id = request.args.get('host_id')
        res = CPULayoutService.execute(host_id)
        if res.get('error'):
            return make_response(
                dict(status=False, code=400, message=res.get('message'))), 400
        response = make_response(dict(status=True, data=res['data'], code=200))
        return response, 200
