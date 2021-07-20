from backend.myBluePrint.ericic_v2.base_dao.novadataApiDao import novadataApiDao
from backend.myBluePrint.ericic_v2.common.model_to_dict import Model_To_Dict


class NovaDataService():
    @classmethod
    def select_nova_data(cls, dc_id, limit, offset, sort, order, query, filter):
        _data = novadataApiDao.select_nova_data(dc_id=dc_id, query=query, limit=limit, offset=offset, sort=sort,
                                                order=order, filter=filter
                                                )
        resp = Model_To_Dict.dict_handle(_data=_data, )
        return resp, _data[3]

    @classmethod
    def select_nova_stack_data(cls, dc_id, filter, limit, offset, sort, order, ):
        resource_id_list = novadataApiDao.query_stack_resource_id(dc_id, filter)
        _data = novadataApiDao.query_nova_in_resource_id(dc_id=dc_id, limit=limit, offset=offset, sort=sort,
                                                         order=order, resource_id_list=resource_id_list)
        resp = Model_To_Dict.dict_handle(_data=_data)
        return resp, _data[3]
