from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic_v2.service.downloadService import DownloadService


class DownloadView(APiMethodView):

    def get(self, *args, **kwargs):
        record_id = request.args.get('id')
        res = DownloadService.download(record_id)
        if res.get('error'):
            return make_response(
                dict(status=False, code=400, message='genarate excel error')), 400
        else:
            response = make_response(dict(status=True, data=res['data'], code=200))
            return response, 200