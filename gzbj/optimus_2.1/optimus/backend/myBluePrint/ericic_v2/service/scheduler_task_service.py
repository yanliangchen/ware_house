#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/10 10:06
# @Desc  :
from apscheduler.jobstores.base import JobLookupError
from backend.scheduler_handler.scheduler_handler import SCHEDULER
from backend.myException.myExecption import MyRuntimeError, MyDataConsistencyError
from backend.scheduler_handler.task_mapping import STATIC_REFRESH, DYNAMIC_REFRESH
from backend.myBluePrint.ericic_v2.base_dao.scheduler_dao import SchedulerDao
from backend.scheduler_handler.scheduler_task import SchedulerTask


class SchedulerService:

    @classmethod
    def get_dc_refresh_task_by_id(cls, dc_id):
        res = list()
        dc_entity = SchedulerDao.get_dc_by_id(dc_id)
        if dc_entity and dc_entity.mode:
            res_info = dict()
            static_job_id = '%s:%s' % (dc_id, STATIC_REFRESH)
            dynamic_job_id = '%s:%s' % (dc_id, DYNAMIC_REFRESH)
            static_job = SCHEDULER.scheduler.get_job(static_job_id)
            dynamic_job = SCHEDULER.scheduler.get_job(dynamic_job_id)
            res_info['cid'] = dc_entity.id

            refresh_task_entities = SchedulerDao.get_refresh_task_entities(dc_id)
            static_entity, dynamic_entity = refresh_task_entities['static'], refresh_task_entities['dynamic']
            if not static_entity or not dynamic_entity:
                # todo: consider if the service needs to keep the data's consist when find the consist error
                raise MyDataConsistencyError('data consistency error, about dc entity and db refresh entity')
            res_info['dynamic_task'] = dict(
                job_id=dynamic_job_id,
                next_run_time=str(dynamic_job.next_run_time) if dynamic_job and dynamic_job.next_run_time else None,
                interval=dynamic_entity.interval,
                start=dynamic_entity.start,
                end=dynamic_entity.end,
            )
            res_info['static_task'] = dict(
                job_id=static_job_id,
                next_run_time=str(static_job.next_run_time) if static_job and static_job.next_run_time else None,
                interval=static_entity.interval,
                start=static_entity.start,
                end=static_entity.end,
            )
            res.append(res_info)
        return res

    # @classmethod
    # def get_all_dc_refresh_task(cls):
    #     res = dict()
    #     job_list = SCHEDULER.scheduler.get_jobs(jobstore='default')
    #     for job in job_list:
    #         job_id = job.id
    #         next_run_time = job.next_run_time
    #         dc_id = job_id.split(':')[0]
    #         info_dict = res.setdefault(dc_id, dict(dynamic_task=None, static_task=None, cid=dc_id))
    #         task_info = dict(job_id=job_id, next_run_time=next_run_time)
    #         inner_key = 'dynamic_task' if job_id.endswith(DYNAMIC_REFRESH) else 'static_task'
    #         info_dict[inner_key] = task_info
    #
    #
    #
    #     return [res[key] for key in res]

    @classmethod
    def pause_job(cls, dc_id, task_name):
        task = STATIC_REFRESH if task_name == 'static' else DYNAMIC_REFRESH
        job_id = '%s:%s' % (dc_id, task)
        try:
            SCHEDULER.scheduler.pause_job(job_id)
        except JobLookupError:
            raise MyRuntimeError('can not find the specified job, pls check your input', 400)

    @classmethod
    def resume_job(cls, dc_id, task_name):
        task = STATIC_REFRESH if task_name == 'static' else DYNAMIC_REFRESH
        job_id = '%s:%s' % (dc_id, task)
        try:
            SCHEDULER.scheduler.resume_job(job_id)
        except JobLookupError:
            dc_entity = SchedulerDao.get_dc_by_id(dc_id)
            if not dc_entity:
                raise MyRuntimeError('can not find the specified data center, pls check your input', 400)
            mode = dc_entity.mode
            if not mode:
                raise MyRuntimeError('the offline mode data center can not be added into scheduler task model', 400)
            interval = 60 * 30 if task == DYNAMIC_REFRESH else 30 * 30
            SCHEDULER.scheduler.add_job(func=SchedulerTask.db_refresh_job, trigger='interval',
                                        seconds=interval, id='%s:%s' % (dc_id, task), args=(dc_id, task),
                                        replace_existing=True)
            # raise MyRuntimeError('can not find the specified job, pls check your input', 500)

    @classmethod
    def reschedule_job(cls, dc_id, task, interval, start, end):
        # todo: this funciton need to recheck to avoid the dead loop
        task = STATIC_REFRESH if task == 'static' else DYNAMIC_REFRESH
        job_id = '%s:%s' % (dc_id, task)
        try:
            task_id = '%s:%s' % (dc_id, task)
            job = SCHEDULER.scheduler.reschedule_job(job_id=job_id, trigger='interval', seconds=int(interval))
            SchedulerDao.reschedule_task(task_id, start=start, end=end, interval=int(interval))

        except JobLookupError:
            raise MyRuntimeError('can not find the specified job, pls check your input', 400)
        return dict(next_run_time=str(job.next_run_time) if job.next_run_time else None)

    # todo: this function just a temporary implement
    @classmethod
    def reschedule_v2(cls, dc_id, task, interval, start, end, action):
        cls.reschedule_job(dc_id, task, interval, start, end)
        if action == 'pause':
            cls.pause_job(dc_id, task)
        else:
            cls.resume_job(dc_id, task)
        try:
            task = STATIC_REFRESH if task == 'static' else DYNAMIC_REFRESH
            job_id = '%s:%s' % (dc_id, task)
            job = SCHEDULER.scheduler.get_job(job_id)
        except JobLookupError:
            raise MyRuntimeError('can not find the specified job, pls check your input', 400)
        return dict(next_run_time=str(job.next_run_time) if job.next_run_time else None)
