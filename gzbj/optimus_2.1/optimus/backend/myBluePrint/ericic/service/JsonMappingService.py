import time
from backend.myBluePrint.ericic.model.JsonMappingModel import JsonMappingModel as JsonMappingModel
from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic.baseDao.jsonmappingApiDao import jsonmappingApiDao


class JsonMappingService():

    @classmethod
    def add_json_map(cls, _id, data,
                     ):
        """

        :param name:
        :param country:
        :param province:
        :param city:
        :param data_center:
        :param vim:
        :param cee_version:
        :param lcm_ip:
        :param lcm_user:
        :param lcm_pwd:
        :param openrc_dir:
        :return:
        """

        result = JsonMappingModel(_id=_id,
                                  data=data, timestamp=int(time.time()))
        result.add()

        return _id

    @classmethod
    def select_cpu_memory_disk(cls, dc_id):
        _data = jsonmappingApiDao.select_json_mapping(dc_id)
        data = {}
        datas = eval(_data[0].data)
        data["cpu_total"] = datas["dc_info"]["vcpus"]
        data["cpu_used"] = datas["dc_info"]["vcpus_used"]
        data["cpu_free"] = data["cpu_total"] - data["cpu_used"]
        data["cpu_usage_rate"] = '{:.2%}'.format(data["cpu_used"] / data["cpu_total"])
        data["memory_total"] = datas["dc_info"]["memory_mb"]
        data["memory_used"] = datas["dc_info"]["memory_mb_used"]
        data["memory_free"] = data["memory_total"] - data["memory_used"]
        data["memory_usage_rate"] = '{:.2%}'.format(data["memory_used"] / data["memory_total"])
        data["disk_total"] = datas["dc_info"]["local_gb"]
        data["disk_used"] = datas["dc_info"]["local_gb_used"]
        data["disk_free"] = data["disk_total"] - data["disk_used"]
        data["disk_usage_rate"] = '{:.2%}'.format(data["disk_used"] / data["disk_total"])
        return data

    @classmethod
    def select_tenant_cpu(cls, dc_id):
        _data = jsonmappingApiDao.select_json_mapping(dc_id)
        lists = list()
        datas = eval(_data[0].data)
        memory_cpu = datas['usage_compute_quata']
        name = datas['tenants']
        for k in name:
            for j in memory_cpu:
                if j['ID'] == k['ID']:
                    j['Name'] = k['Name']
                    lists.append(j)
        data_lists = list()
        for tenant_cpu in lists:
            data = dict()
            data['tenant_name'] = tenant_cpu['Name']
            data['tenant_cpu_used'] = tenant_cpu['Core In_use']
            data['tenant_cpu_free'] = tenant_cpu['Core Limit']
            data['tenant_cpu_usage'] = data['tenant_cpu_used'] / data['tenant_cpu_free']
            data_lists.append(data)
        return data_lists

    @classmethod
    def select_tenant_memory(cls, dc_id):
        _data = jsonmappingApiDao.select_json_mapping(dc_id)
        lists = list()
        datas = eval(_data[0].data)
        memory_cpu = datas['usage_compute_quata']
        name = datas['tenants']
        for k in name:
            for j in memory_cpu:
                if j['ID'] == k['ID']:
                    j['Name'] = k['Name']
                    lists.append(j)
        data_lists = list()
        for tenant_memory in lists:
            data = dict()
            data['tenant_name'] = tenant_memory['Name']
            data['tenant_memory_used'] = tenant_memory['Ram In_use']
            data['tenant_memory_free'] = tenant_memory['Ram Limit']
            data['tenant_memory_usage'] = data['tenant_memory_used'] / data['tenant_memory_free']
            data_lists.append(data)
        return data_lists

    @classmethod
    def select_tenant_disk(cls, dc_id):
        _data = jsonmappingApiDao.select_json_mapping(dc_id)
        lists = list()
        datas = eval(_data[0].data)
        disk = datas['usage_volume_quata']
        name = datas['tenants']
        for k in name:
            for j in disk:
                if j['ID'] == k['ID']:
                    j['Name'] = k['Name']
                    lists.append(j)
        data_lists = list()
        for tenant_memory in lists:
            data = dict()
            data['tenant_name'] = tenant_memory['Name']
            data['tenant_disk_used'] = tenant_memory['Gigabytes In_use']
            data['tenant_disk_free'] = tenant_memory['Gigabytes Limit']
            data['tenant_disk_usage'] = data['tenant_disk_used'] / data['tenant_disk_free']
            data_lists.append(data)
        return data_lists

    @classmethod
    def select_all_data(cls, dc_id):
        _data = jsonmappingApiDao.select_json_mapping(dc_id)
        fina_lists = list()
        all_dict = {}
        datas = eval(_data[0].data)
        all_dict["cpu_total"] = datas["dc_info"]["vcpus"]
        all_dict["cpu_used"] = datas["dc_info"]["vcpus_used"]
        all_dict["cpu_free"] = all_dict["cpu_total"] - all_dict["cpu_used"]
        all_dict["cpu_usage_rate"] = '{:.2%}'.format(all_dict["cpu_used"] / all_dict["cpu_total"])
        all_dict["memory_total"] = round(datas["dc_info"]["memory_mb"]/1024,1)
        all_dict["memory_used"] = round(datas["dc_info"]["memory_mb_used"]/1024,1)
        all_dict["memory_free"] = round(all_dict["memory_total"] - all_dict["memory_used"],1)
        all_dict["memory_usage_rate"] = '{:.2%}'.format(all_dict["memory_used"] / all_dict["memory_total"])
        all_dict["disk_total"] = round(datas["dc_info"]["local_gb"]/1024,1)
        all_dict["disk_used"] = round(datas["dc_info"]["local_gb_used"]/1024,1)
        all_dict["disk_free"] = round(all_dict["disk_total"] - all_dict["disk_used"],1)
        all_dict["disk_usage_rate"] = '{:.2%}'.format(all_dict["disk_used"] / all_dict["disk_total"])
        fina_lists.append(all_dict)

        # lists = []
        # disk = datas['usage_volume_quata']
        # name = datas['tenants']
        # for k in name:
        #     for j in disk:
        #         if j['ID'] == k['ID']:
        #             j['Name'] = k['Name']
        #             lists.append(j)
        # data_lists = list()
        # for tenant_memory in lists:
        #     data = dict()
        #     data['tenant_name'] = tenant_memory['Name']
        #     data['tenant_disk_used'] = tenant_memory['Gigabytes In_use']
        #     data['tenant_disk_free'] = tenant_memory['Gigabytes Limit']
        #     data['tenant_disk_usage'] = data['tenant_disk_used'] / data['tenant_disk_free']
        #     data_lists.append(data)
        # disk_dict = {}
        # disk_dict['disk'] = data_lists
        # fina_lists.append(disk_dict)

        lists = list()
        memory_cpu = datas['usage_compute_quata']
        name = datas['tenants']
        for k in name:
            for j in memory_cpu:
                if j['ID'] == k['ID']:
                    j['Name'] = k['Name']
                    lists.append(j)
        data_lists = list()
        for tenant_cpu in lists:
            data = dict()
            data['tenant_name'] = tenant_cpu['Name']
            data['tenant_cpu_total'] =datas["dc_info"]["vcpus"]
            data['tenant_cpu_used'] = tenant_cpu['Core In_use']
            data['tenant_cpu_free'] =  data['tenant_cpu_total'] - data['tenant_cpu_used']
            data['tenant_cpu_usage'] = '{:.2%}'.format(data['tenant_cpu_used'] / data['tenant_cpu_total'])
            data_lists.append(data)
        cpu_dict = {}
        cpu_dict['cpu'] = data_lists
        fina_lists.append(cpu_dict)

        lists = list()
        memory_cpu = datas['usage_compute_quata']
        name = datas['tenants']
        for k in name:
            for j in memory_cpu:
                if j['ID'] == k['ID']:
                    j['Name'] = k['Name']
                    lists.append(j)
        data_lists = list()
        for tenant_memory in lists:
            data = dict()
            data['tenant_name'] = tenant_memory['Name']
            data['tenant_memory_total'] =round(datas["dc_info"]["memory_mb"]/1024,1)
            data['tenant_memory_used'] = round(tenant_memory['Ram In_use']/1024,1)
            data['tenant_memory_free'] = round(data['tenant_memory_total'] -data['tenant_memory_used'],1)
            data['tenant_memory_usage'] ='{:.2%}'.format( data['tenant_memory_used'] / data['tenant_memory_total'])
            data_lists.append(data)
        memory_dict = {}
        memory_dict['memory'] = data_lists
        fina_lists.append(memory_dict)

        return fina_lists

    @classmethod
    def delete_json_mapping(cls, dc_id):
        db_session = SESSION()
        try:
            db_session.query(JsonMappingModel).filter(JsonMappingModel.id == dc_id).delete()
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise Exception
        finally:
            db_session.close()
