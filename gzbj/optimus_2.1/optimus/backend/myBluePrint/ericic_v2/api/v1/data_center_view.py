from backend.myBluePrint.ericic_v2.param_verify.data_center_check import DataCenterCheck
from backend.myBluePrint.ericic_v2.service.data_center_service import DataCenterService
from backend.customer.myCustomer import APiMethodView
from flask import request, make_response
import uuid


class DataCenterView(APiMethodView):
    # check_cls = DataCenterCheck

    # @dec_auth
    def get(self, *args, **kwargs):
        dc_id = request.args.get('id')
        if dc_id:
            data = DataCenterService.select_instance(dc_id)
            if data:
                response = make_response(dict(status=True, data=data, code=200))

            else:
                response = make_response(dict(status=False, message="The data doesn't exist", code=400))
            return response

        limit = request.args.get('limit', 10)
        offset = request.args.get("offset", 0)
        if limit or offset is not int:
            try:
                limit = int(limit)
                offset = int(offset)
            except Exception as e:
                limit = 10
                offset = 0

        data = DataCenterService.select_instances(limit=int(limit), offset=int(offset))
        total = data[1]
        response = make_response(dict(status=True, data=data[0], total=total, code=200))
        return response

    # @dec_auth
    def post(self, *args, **kwargs):
        dc_info = request.get_json()
        # first_id = ''.join(str(uuid.uuid1()).split('-'))
        first_id = uuid.uuid4().hex
        dc_name = dc_info["name"]
        mode = dc_info['mode']
        country = dc_info["country"]
        province = dc_info["province"]
        city = dc_info["city"]
        system_name = dc_info["system_name"]
        cee_version = dc_info['cee_version']
        lcm_ip = dc_info['lcm_ip']
        lcm_user = dc_info['lcm_user']
        lcm_pwd = dc_info['lcm_pwd']
        openstackrc_dir = dc_info['openstackrc_dir']
        lcmrc_dir = dc_info['lcmrc_dir']
        data = DataCenterService.add_instance(first_id, dc_name, mode, country, province, city, system_name,
                                              cee_version, lcm_ip, lcm_user, lcm_pwd, openstackrc_dir, lcmrc_dir)
        response = make_response(dict(status=True, message='Success add', data=data, code=200))
        return response


    # @dec_auth
    def delete(self, *args, **kwargs):
        dc_info = request.get_json()
        dc_id = dc_info["id"]
        dc_del_id = DataCenterService.delete_instance(dc_id)

        if dc_del_id:
            response = make_response(dict(status=True, message="Deletion succeeded by id", data=dc_del_id, code=200))
            return response
        else:
            return make_response(dict(status=False, message="Data does not exist"))

    def put(self, *args, **kwargs):
        body = request.get_json()
        cid = body['id']
        # mode = body["mode"]
        country = body["country"]
        province = body["province"]
        city = body["city"]
        system_name = body["system_name"]
        cee_version = body['cee_version']
        switch = DataCenterService.get_mode(cid)
        if switch == 1:
            lcm_ip = body['lcm_ip']
            lcm_user = body['lcm_user']
            lcm_pwd = body['lcm_pwd']
            openstackrc_dir = body['openstackrc_dir']
            lcmrc_dir = body['lcmrc_dir']
            DataCenterService.online_update(cid, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                                            lcm_pwd, openstackrc_dir, lcmrc_dir)
        elif switch == 0:
            DataCenterService.offline_update(cid, country, province, city, system_name, cee_version)
        return make_response(dict(status=True, code=200)), 200
