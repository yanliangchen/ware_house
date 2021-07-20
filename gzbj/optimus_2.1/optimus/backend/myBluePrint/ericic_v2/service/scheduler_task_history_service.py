#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : scheduler_task_history_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 17:19
# @Desc  :
from backend.scheduler_handler.task_mapping import STATIC_REFRESH, DYNAMIC_REFRESH
from backend.myBluePrint.ericic_v2.base_dao.scheduler_task_history_dao import SchedulerTaskHistoryDao


class SchedulerTaskHistoryService:

    @classmethod
    def get_history_by_cid(cls, cid, _filter, limit, offset):

        if cid:
            if _filter == 'static':
                _filter = STATIC_REFRESH
            elif _filter == 'dynamic':
                _filter = DYNAMIC_REFRESH
            result = SchedulerTaskHistoryDao.get_history_by_cid(cid, _filter, limit, offset)
            res = result['res']
            total_num = result['total_num']
            response_info = list()
            for item in res:
                info = dict()
                info['id'] = item.id
                info['task_name'] = item.task_name
                info['dc_id'] = item.dc_id
                info['dc_name'] = item.dc_name
                info['status'] = item.status
                info['error_info'] = item.error_info
                info['timestamp'] = item.timestamp
                response_info.append(info)
            response = dict(data=response_info, total_num=total_num)
        else:
            response = dict(data=[], total_num=0)
        return response
