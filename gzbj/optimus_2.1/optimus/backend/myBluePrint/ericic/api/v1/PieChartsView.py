from backend.myBluePrint.ericic.paramVerify.dataCenterCheck import DataCenterCheck
from backend.myBluePrint.ericic.service.dataCenterSercice import DataCenterService
from backend.customer.myCustomer import APiMethodView
from flask import request, make_response
from backend.myBluePrint.ericic.service.JsonMappingService import JsonMappingService
import uuid


class PieChartsView(APiMethodView):


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
        # cpu = request.args.get('tcpu')
        # memory =request.args.get('tmemory')
        # disk =request.args.get('tdisk')
        if dc_id:
            data = JsonMappingService.select_all_data(dc_id)
        # if dc_id:
        #     data = JsonMappingService.select_cpu_memory_disk(dc_id)
        #
        # if dc_id and cpu:
        #     data = JsonMappingService.select_tenant_cpu(dc_id)
        #
        # if dc_id and memory:
        #     data = JsonMappingService.select_tenant_memory(dc_id)
        #
        # if dc_id and disk:
        #     data = JsonMappingService.select_tenant_disk(dc_id)

        response = make_response(dict(status=True, data=data, code=200))
        return response
