import time
from apscheduler.jobstores.base import JobLookupError
from backend.common.loghandler import ServiceLog
from backend.scheduler_handler.scheduler_handler import SCHEDULER
from backend.scheduler_handler.task_mapping import STATIC_REFRESH, DYNAMIC_REFRESH
from backend.scheduler_handler.scheduler_task import SchedulerTask
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel as DataCenter
from backend.myBluePrint.ericic_v2.base_dao.data_center_api_dao import datacenterApiDao


class DataCenterService():

    @classmethod
    def update_instance(cls, _id, mode, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                        lcm_pwd, openstackrc_dir, lcmrc_dir):

        DataCenter.update_by_id(_id, mode=int(mode), country=country, province=province, city=city,
                                system_name=system_name, cee_version=cee_version, lcm_ip=lcm_ip, lcm_user=lcm_user,
                                lcm_pwd=lcm_pwd, openstackrc_dir=openstackrc_dir, lcmrc_dir=lcmrc_dir)

    @classmethod
    def update_mof_instance(cls, _id, mode, country, province, city, system_name, cee_version, ):

        # todo : data center's mode can not be update
        DataCenter.update_by_id(_id=_id, mode=mode, country=country, province=province, city=city,
                                system_name=system_name,
                                cee_version=cee_version)

    @classmethod
    def get_mode(cls, cid):
        res = 0
        dc_entity = DataCenter.get_one_by_id(cid)
        if dc_entity and dc_entity.mode:
            res = 1
        elif dc_entity and not dc_entity.mode:
            res = -1
        elif not dc_entity:
            res = 0
        return res

    @classmethod
    def offline_update(cls, cid, country, province, city, system_name, cee_version):
        kw = dict(country=country, province=province, city=city, system_name=system_name, cee_version=cee_version)
        res = DataCenter.update_by_id(cid, **kw)
        return res

    @classmethod
    def online_update(cls, cid, country, province, city, system_name, cee_version, lcm_ip, lcm_user, lcm_pwd,
                      openstackrc_dir, lcmrc_dir):
        kw = dict(country=country, province=province, city=city, system_name=system_name, cee_version=cee_version,
                  lcm_ip=lcm_ip, lcm_user=lcm_user, lcm_pwd=lcm_pwd, openstackrc_dir=openstackrc_dir,
                  lcmrc_dir=lcmrc_dir)
        res = DataCenter.update_by_id(cid, **kw)
        return res

    @classmethod
    def add_instance(cls, _id, name, mode, country, province, city, system_name, cee_version, lcm_ip, lcm_user,
                     lcm_pwd, openstackrc_dir, lcmrc_dir):
        result = DataCenter(_id=_id, name=name, mode=mode, country=country, province=province, city=city,
                            system_name=system_name, cee_version=cee_version, lcm_ip=lcm_ip, lcm_user=lcm_user,
                            lcm_pwd=lcm_pwd, openstackrc_dir=openstackrc_dir, lcmrc_dir=lcmrc_dir,
                            timestamp=int(time.time()))
        # the following code was updated by gaofzhan at 2020/12/11, to gen the cache data in db by a async task
        datacenterApiDao.add_data_center(result)
        dynamic_job, static_job = None, None
        if mode:
            try:
                SchedulerTask.db_refresh_job(_id, DYNAMIC_REFRESH, data_init=True)
                SchedulerTask.db_refresh_job(_id, STATIC_REFRESH, data_init=True)
            except Exception as e:
                ServiceLog.error(str(e))
                raise e
            try:
                dynamic_job = SCHEDULER.scheduler.add_job(func=SchedulerTask.db_refresh_job, trigger='interval',
                                                          seconds=60 * 30, id='%s:%s' % (_id, DYNAMIC_REFRESH),
                                                          args=(_id, DYNAMIC_REFRESH))
                static_job = SCHEDULER.scheduler.add_job(func=SchedulerTask.db_refresh_job, trigger='interval',
                                                         seconds=60 * 60, id='%s:%s' % (_id, STATIC_REFRESH),
                                                         args=(_id, STATIC_REFRESH))
            except Exception as e:
                ServiceLog.error(str(e))
                raise e

        res = dict(
            id=_id,
            dynamic_job=str(dynamic_job.next_run_time) if dynamic_job else None,
            static_job=str(static_job.next_run_time) if static_job else None,
        )
        # end the following

        return res

    @classmethod
    def delete_instance(cls, dc_id):

        datacenterApiDao.delete_all_relate_info(dc_id)
        dc_dict = {}
        dc_dict['id'] = dc_id

        # todo: delete the scheduler job, and also need to judge whether the job is running,
        # the following code was updated by gaofzhan at 2020/12/14, to gen the cache data in db by a async task
        try:
            SCHEDULER.scheduler.remove_job('%s:%s' % (dc_id, DYNAMIC_REFRESH))
        except JobLookupError:
            pass
        try:
            SCHEDULER.scheduler.remove_job('%s:%s' % (dc_id, STATIC_REFRESH))
        except JobLookupError:
            pass
        # end the following

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
