from backend.myBluePrint.ericic_v2.base_dao.hostdataApiDao import hostdataApiDao
from backend.myBluePrint.ericic_v2.common.model_to_dict import Model_To_Dict
from copy import deepcopy


class HostDataService():
    @classmethod
    def select_host_data(cls, dc_id, query, filter, limit, offset,order,sort):


        service_data, hz_data, nova_data,count = hostdataApiDao.select_host_data(
            dc_id=dc_id, query=query, filter=filter, limit=limit, offset=offset,order=order,sort=sort
        )
        hz_data = Model_To_Dict.model_to_dict(hz_data)
        nova_data = Model_To_Dict.model_to_dict(nova_data)

        service_data_handle = cls.service_data_handle(service_data)
        hz_data_handle = cls.hz_data_handle(hz_data)
        nova_data_handle = cls.nova_data_handle(nova_data)

        data = list()
        for key, value in service_data_handle.items():
            _hz = hz_data_handle.get(key, list())
            _nova_data = nova_data_handle.get(key, list())
            if query == 'ha' and not _hz:
                continue
            elif query == 'az' and not _hz:
                continue
            value["hz"] = _hz
            value["nova_data"] = _nova_data
            data.append(value)
        # print(data)
        # if sort == 'vm_amount':
        #     if order == 'desc':
        #         data.sort(key=lambda x: len(x.get('nova_data')), reverse=True)
        #         return data
        #     elif order == 'asc':
        #         data.sort(key=lambda x: len(x.get('nova_data')), reverse=False)
        #         return data
        return data,count

    @classmethod
    def service_data_handle(cls, service_data):
        return {i.get('host'): i for i in service_data}

    @classmethod
    def hz_data_handle(cls, hz_data):
        hz = dict()
        for i in hz_data:
            hosts = i.get("host").split(",")
            for every_host in hosts:
                host_res = every_host.replace("'", "").strip()
                hz_data_c = deepcopy(i)
                hz_data_c['host'] = host_res
                if host_res in hz:
                    hz[host_res].append(hz_data_c)
                else:
                    hz[host_res] = list()
                    hz[host_res].append(hz_data_c)

        return hz

    @classmethod
    def nova_data_handle(cls, nova_datas):
        nova_data = dict()
        for i in nova_datas:
            host = i.get("n_host").strip()
            if host in nova_data:
                nova_data[host].append(i)
            else:
                nova_data[host] = list()
                nova_data[host].append(i)
        return nova_data
