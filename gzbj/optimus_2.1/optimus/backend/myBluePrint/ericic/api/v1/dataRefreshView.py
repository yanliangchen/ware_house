from flask import make_response
from backend.myBluePrint.ericic.service.dataRefreshService import DataRefreshService
from backend.customer.myCustomer import APiMethodView


class DataRefreshView(APiMethodView):

    def post(self, *args, **kwargs):
        DataRefreshService.update_openstack_host()
        return make_response(dict(code=200, status=True))
