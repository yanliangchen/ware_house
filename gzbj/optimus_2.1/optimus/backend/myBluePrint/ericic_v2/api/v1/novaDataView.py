from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.novaDataService import NovaDataService
from flask import make_response, request


class NovaData(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        dc_id = request.args.get('dc_id')

        query = request.args.get('query')
        filter = request.args.get('filter')
        sort = request.args.get('sort', 'time')
        order = request.args.get('order', 'desc')

        limit = request.args.get('limit', 10)
        offset = request.args.get("offset", 0)

        if limit or offset is not int:
            try:
                limit = int(limit)
                offset = int(offset)
            except Exception as e:
                limit = 10
                offset = 0

        if query == 'stack_id':
            filter = request.args.get('filter')
            if filter:
                nova_stack_resp = NovaDataService.select_nova_stack_data(dc_id=dc_id, limit=int(limit),
                                                                         offset=int(offset),
                                                                         order=order, filter=filter, sort=sort)
                total = nova_stack_resp[1]
                response = make_response(dict(status=True, data=nova_stack_resp[0], total=total, code=200))
                return response

        nova_h_f_t_dict = NovaDataService.select_nova_data(dc_id=dc_id, limit=int(limit), offset=int(offset),
                                                           order=order, filter=filter, query=query, sort=sort)
        total = nova_h_f_t_dict[1]
        response = make_response(dict(status=True, data=nova_h_f_t_dict[0], total=total, code=200))

        return response
