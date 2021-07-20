import json
from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.hostService import HostService


class HostView(APiMethodView):

    def get(self, *args, **kwargs):
        cid = request.args.get('cid', None)
        sort = request.args.get('sort', 'timestamp')
        order = request.args.get('order', 'desc')
        query = request.args.get('query', '{}')
        column = request.args.getlist('column')
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 50)
        query = json.loads(query)
        sort = 'timestamp'
        res = HostService.get_host_info(cid, sort, order, query, column, offset, limit)
        return make_response(dict(status=True, data=res['res'], code=200, total=res['total_num'])), 200
