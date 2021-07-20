from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.hostDataService import HostDataService
from flask import make_response, request


class HostData(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        # resp = HostDataService.select_host_data(dc_id=dc_id, query=query, filter=filter, limit=limit, offset=offset,
        #                                         )  # order=order, sort=sort)
        limit = request.args.get('limit', 10)
        offset = request.args.get('offset', 0)
        query = request.args.get('query','')
        filter = request.args.get('filter','')
        order = request.args.get('order', 'asc')
        sort = request.args.get('sort', 'vm_amount')
        dc_id = request.args.get('dc_id')

        if limit or offset is not int:
            try:
                limit = int(limit)
                offset = int(offset)
            except Exception as e:
                limit = 10
                offset = 0
        resp, count = HostDataService.select_host_data(dc_id=dc_id, query=query, filter=filter, limit=limit,
                                                       offset=offset,
                                                       order=order, sort=sort)  # order=order, sort=sort)

        response = make_response(dict(status=True, total=count, data=resp, code=200))
        return response
        # return 'ok'
