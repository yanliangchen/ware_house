from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.recordService import RecordService


class RecordView(APiMethodView):

    def get(self, *args, **kwargs):
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 20)
        dc_id = request.args.get('cid')
        if not isinstance(offset, int):
            offset = 0
        if not isinstance(limit, int):
            limit = 20
        res = RecordService.split_data(offset, limit, dc_id)
        response = make_response(dict(status=True, data=res['data'], total=res['total_num'], code=200))
        return response, 200

    def post(self, *args, **kwargs):
        body = request.get_json()
        name = body.get('name')
        dc_id = body.get('cid')
        res = RecordService.add_record(name, dc_id)
        return res

    def delete(self, *args, **kwargs):
        body = self.request.get_json()
        record_id = body.get('id')
        dc_id = body.get('cid', None)
        RecordService.delete_record(record_id)
        response = make_response(dict(status=True, code=200))
        return response, 200
