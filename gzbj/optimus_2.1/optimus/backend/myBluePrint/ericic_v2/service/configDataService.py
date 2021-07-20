from backend.myBluePrint.ericic_v2.base_dao.configdataApiDao import ConfigDataApiDao
from backend.myBluePrint.ericic_v2.common.model_to_dict import Model_To_Dict


class ConfigDataService():
    @classmethod
    def select_config(cls, dc_id):
        tenants_result = ConfigDataApiDao.select_tenants(dc_id)
        config_list = []
        config_dict = {}
        stacks_result = ConfigDataApiDao.select_stacks(dc_id)
        config_dict['stack'] = stacks_result
        config_dict['tenant'] = tenants_result
        config_list.append(config_dict)
        return config_list
