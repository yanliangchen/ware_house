from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.recordResultService import RecordResultService


class RecordResultView(APiMethodView):

    def get(self, *args, **kwargs):
        record_id = request.args.get('id')
        res = RecordResultService.download_record(record_id)
        if res.get('error'):
            return make_response(
                dict(status=False, code=400, message=res.get('message'))), 400
        response = make_response(dict(status=True, data=res['data'], code=200))
        return response, 200
