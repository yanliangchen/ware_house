from flask import request
from backend.customer.myCustomer import APiMethodView
from backend.common.authentication import dec_auth
from backend.myBluePrint.yaml_generator.service.YamlGenService import *
from backend.myBluePrint.yaml_generator.service.HistoryService import *
from backend.myBluePrint.yaml_generator.service.ResultService import *


class YamlGen(APiMethodView):

    # @dec_auth
    def post(self, *args, **kwargs):
        site = request.args.get('site')
        cee_ver = request.args.get('cee_ver')
        pjt_name = request.args.get('pjt_name')
        yaml_list = request.files.getlist('yaml')
        excel = request.files.get('excel')
        # name = g.name
        name = 'demo_name'
        res = YamlGenService.yaml_gen(site, cee_ver, pjt_name, yaml_list, excel, name)
        response = make_response(dict(status=True, data=dict(id=res), code=200))
        return response, 200


class History(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        res = HistoryService.get_all_task()
        response = make_response(dict(status=True, data=res, code=200))
        return response, 200

    # @dec_auth
    def delete(self, *args, **kwargs):
        body = self.request.get_json()
        id_list = body.get('id')
        HistoryService.delete_history(id_list)
        response = make_response(dict(status=True, code=200))
        return response, 200


class Result(APiMethodView):

    # @dec_auth
    def get(self, *args, **kwargs):
        job_id = request.args.get('id')
        res = ResultService.get_result(job_id)
        return res
