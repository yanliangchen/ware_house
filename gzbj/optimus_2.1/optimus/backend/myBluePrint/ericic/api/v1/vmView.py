import json
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.vmService2 import VmService


class VmView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = request.args.get('cid', None)
        sort = request.args.get('sort', 'timestamp')
        order = request.args.get('order', 'desc')
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 50)
        column_list = request.args.getlist('column')
        # refresh = request.args.get('refresh', 'false')
        query = request.args.get('query', '{}')
        try:
            query = json.loads(query)
        except:
            query = dict()
        # refresh = True if refresh.lower() == 'true' else False
        res = VmService.service_switch(offset, limit, column_list, query, sort, order, cid)
        return make_response(dict(code=200, data=res['res'], status=True, total=res['total_num'])), 200
