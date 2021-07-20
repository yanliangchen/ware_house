from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.recordService import RecordService


class RecordView(APiMethodView):

    def get(self, *args, **kwargs):
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 50)
        res = RecordService.split_data(offset, limit)
        response = make_response(dict(status=True, data=res['data'], total=res['total_num'], code=200))
        return response, 200

    def post(self, *args, **kwargs):
        body = request.get_json()
        name = body.get('name')
        data_center = body.get('data_center')
        cee_version = body.get('cee_version')
        res = RecordService.add_record(name, data_center, cee_version)
        return res

    def delete(self, *args, **kwargs):
        body = self.request.get_json()
        record_id = body.get('id')
        RecordService.delete_record(record_id)
        response = make_response(dict(status=True, code=200))
        return response, 200
