from flask import request, make_response
from backend.customer.myCustomer import APiMethodView
from backend.myBluePrint.ericic.service.downloadService import DownloadService


class DownloadView(APiMethodView):

    def get(self, *args, **kwargs):
        dc_id = request.args.get('id')
        # dc_status = request.args.get('status', default="online")
        # res = DownloadService.download(dc_id, dc_status)
        res = DownloadService.download(dc_id)
        if res.get('error'):
            return make_response(
                dict(status=False, code=400, message='genarate excel error')), 400
        else:
            response = make_response(dict(status=True, data=res['data'], code=200))
            return response, 200