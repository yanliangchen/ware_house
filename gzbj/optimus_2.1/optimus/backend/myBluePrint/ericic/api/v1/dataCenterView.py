from backend.myBluePrint.ericic.paramVerify.dataCenterCheck import DataCenterCheck
from backend.myBluePrint.ericic.service.dataCenterSercice import DataCenterService
from backend.customer.myCustomer import APiMethodView
from flask import request, make_response
import uuid


class DataCenter(APiMethodView):
    check_cls = DataCenterCheck

    # @dec_auth
    def get(self, *args, **kwargs):
        """
        this function is to get the information about the instance of cee,
        this function has 2 scenes , the param in url has id or the has no id.

        when there is id in param:
            get the details of instance from db with id

        when there is no id in param:
            get all basic info of instances from db


        : param id --> request.args.get('id') // the specified id of the instance to query info from db

        :return: return json type with structure with following

            {
                code: int,
                data: [
                    {
                        id:
                        name:
                        country:
                        province:
                        city:
                        data_center:
                        vim:
                        cee_version:
                        lcm_ip:
                        lcm_user:
                        lcm_pwd:
                        openrc_dir:
                    },
                ],
                status: bool
            }

        """

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
        """
        this function is to add a instance into the db,

        the request from client will use request body to transfer the param,
        and this function only allow to add one item as one time.

        : param name: name of the instance--> request.body.get('name')
        : param country: pass
        : param province: pass
        : param city: pass
        : param data_center: pass
        : param vim: pass
        : param cee_version: pass
        : param lcm_ip: pass
        : param lcm_user: pass
        : param lcm_pwd: pass
        : param openrc_dir: pass

        :return: when successfully insert a item , return with the following structure

            {
                code: int, //the code should be 201
                data:{
                    id: str, // the newly generated id by the service
                }
                status: true
            }
        """

        dc_info = request.get_json()
        first_id = ''.join(str(uuid.uuid1()).split('-'))
        dc_name = dc_info["name"]
        mode = dc_info.get('mode')
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

        data = DataCenterService.add_instance(first_id, dc_name, mode,
                                              country, province, city, system_name,
                                              cee_version,
                                              lcm_ip,
                                              lcm_user, lcm_pwd,
                                              openstackrc_dir, lcmrc_dir)

        if data:

            response = make_response(dict(status=True, message='Success add', data=data, code=200))
            return response
        else:
            response = make_response(dict(status=False, message='Name duplication', code=400)), 400
            return response

    # @dec_auth
    def delete(self, *args, **kwargs):
        """
        this function is to delete instance from db by the id.
        and this function can not do multi op, so one request can only has one id in the request body

        : param id --> request.body.get('id')

        :return: when the item has been deleted successfully , return the following

            {
                code: 200,
                status: true,
            }
        """

        dc_info = request.get_json()
        dc_id = dc_info["id"]
        dc_del_id = DataCenterService.delete_instance(dc_id)

        if dc_del_id:
            response = make_response(dict(status=True, message="Deletion succeeded by id", data=dc_del_id, code=200))
            return response
        else:
            return make_response(dict(status=False, message="Data does not exist"))

    # @dec_auth
    def put(self, *args, **kwargs):
        """
        this function is to update the info of instance by id,

        : param id:
        : param name: name of the instance--> request.body.get('name')
        : param country: pass
        : param province: pass
        : param city: pass
        : param data_center: pass
        : param vim: pass
        : param cee_version: pass
        : param lcm_ip: pass
        : param lcm_user: pass
        : param lcm_pwd: pass
        : param openrc_dir: pass

        :return:

            {
                code: 200,
                status: true
            }
        """

        dc_info = request.get_json()
        first_id = dc_info["id"]
        mode = dc_info["mode"]
        if bool(mode) == False:
            country = dc_info["country"]
            province = dc_info["province"]
            city = dc_info["city"]
            system_name = dc_info["system_name"]
            cee_version = dc_info['cee_version']
            DataCenterService.update_mof_instance(first_id, mode, country, province, city, system_name, cee_version)
            data = DataCenterService.select_instance(first_id)
            if data:
                response = make_response(dict(status=True, message="modified  success", code=200))

            else:
                response = make_response(dict(status=False, message="The data you modified does not exist", code=400))
            return response
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
        DataCenterService.update_instance(first_id, mode, country, province, city, system_name,
                                          cee_version,
                                          lcm_ip,
                                          lcm_user, lcm_pwd,
                                          openstackrc_dir, lcmrc_dir)
        data = DataCenterService.select_instance(first_id)

        if data:
            response = make_response(dict(status=True, message="modified  success", code=200))

        else:
            response = make_response(dict(status=False, message="The data you modified does not exist", code=400))
        return response
