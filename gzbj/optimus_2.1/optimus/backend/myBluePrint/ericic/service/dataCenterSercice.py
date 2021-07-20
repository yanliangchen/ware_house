import time
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel as DataCenter
from backend.myBluePrint.ericic.baseDao.uploadApiDao import uploadApiDao
from backend.myBluePrint.ericic.baseDao.datacenterApiDao import datacenterApiDao


class DataCenterService():

    @classmethod
    def update_instance(cls, _id, mode, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                        lcm_pwd, openstackrc_dir, lcmrc_dir):

        """

        :param _id:
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

        DataCenter.update_by_id(_id, mode=int(mode), country=country, province=province, city=city,
                                system_name=system_name, cee_version=cee_version, lcm_ip=lcm_ip, lcm_user=lcm_user,
                                lcm_pwd=lcm_pwd, openstackrc_dir=openstackrc_dir, lcmrc_dir=lcmrc_dir)

    @classmethod
    def update_mof_instance(cls, _id, mode, country, province, city, system_name, cee_version, ):

        DataCenter.update_by_id(_id=_id, mode=mode, country=country, province=province, city=city,
                                system_name=system_name,
                                cee_version=cee_version)

    @classmethod
    def add_instance(cls, _id, name, mode, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                     lcm_pwd, openstackrc_dir, lcmrc_dir
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

        result = DataCenter(_id=_id,
                            name=name, mode=mode, country=country, province=province, city=city,
                            system_name=system_name,
                            cee_version=cee_version, lcm_ip=lcm_ip, lcm_user=lcm_user, lcm_pwd=lcm_pwd,
                            openstackrc_dir=openstackrc_dir, lcmrc_dir=lcmrc_dir, timestamp=int(time.time()))
        result.add()

        return _id

    @classmethod
    def delete_instance(cls, dc_id):

        uploadApiDao.delete_all_relate_info(dc_id)
        dc_dict = {}
        dc_dict['id'] = dc_id

        return dc_dict['id']

    @classmethod
    def select_instances(cls, limit, offset):
        _data, count = datacenterApiDao.select_instances(limit, offset)
        result = list()
        for i in _data:
            data = dict()
            data["id"] = i.id
            data["name"] = i.name
            data["mode"] = i.mode
            data["country"] = i.country
            data["province"] = i.province
            data["city"] = i.city
            data["system_name"] = i.system_name
            data["cee_version"] = i.cee_version
            data["lcm_ip"] = i.lcm_ip
            data["lcm_user"] = i.lcm_user
            data["lcm_pwd"] = i.lcm_pwd
            data["openstackrc_dir"] = i.openstackrc_dir
            data["lcmrc_dir"] = i.lcmrc_dir
            result.append(data)
        return result, count

    @classmethod
    def select_instance(cls, dc_id):

        _data = datacenterApiDao.select_instance(dc_id)
        data = {}
        for i in _data:
            data["id"] = i.id
            data["name"] = i.name
            data["mode"] = i.mode
            data["country"] = i.country
            data["province"] = i.province
            data["city"] = i.city
            data["system_name"] = i.system_name
            data["cee_version"] = i.cee_version
            data["lcm_ip"] = i.lcm_ip
            data["lcm_user"] = i.lcm_user
            data["lcm_pwd"] = i.lcm_pwd
            data["openstackrc_dir"] = i.openstackrc_dir
            data["lcmrc_dir"] = i.lcmrc_dir

        return data
