from backend.myBluePrint.ericic_v2.base_dao.configdataApiDao import ConfigDataApiDao
from backend.myBluePrint.ericic_v2.common.model_to_dict import Model_To_Dict
from backend.myBluePrint.ericic_v2.common import dup_dict_in_list
import logging


class HostConfigDataService():
    @classmethod
    def select_host_config(cls, dc_id):
        # host_state_result = ConfigDataApiDao.select_host_state(dc_id)
        host_ha_result = ConfigDataApiDao.select_host_ha(dc_id)
        dup_removal_host_ha = dup_dict_in_list.list_dict_duplicate_removal(host_ha_result)

        host_az_result = ConfigDataApiDao.select_host_az(dc_id)
        dup_removal_host_az = dup_dict_in_list.list_dict_duplicate_removal(host_az_result)

        config_list = []
        config_dict = {}
        # config_dict['host_state'] = host_state_result
        config_dict['host_ha'] = dup_removal_host_ha
        config_dict['host_az'] = dup_removal_host_az
        config_list.append(config_dict)

        return config_list
