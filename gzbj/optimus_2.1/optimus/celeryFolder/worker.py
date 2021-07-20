import sys
# import time
# # sys.path.append('..')
# from celery import Task
# from celery_app import celery_app
# from backend.Model.UserModel import User
# from backend.Model.connection import SESSION
#
#
# @celery_app.task
# def test():
#     db_session = SESSION()
#     res = db_session.query(User).all()[0]
#     _id = res.id
#     name = res.name
#     print(_id, name)
#     return name
#
# class _TestTask(Task):
#     name = 'test_task'
#
#     def run(self, a, b):
#         time.sleep(3)
#         return a * b
#
# # gaofzhan = _TestTask()
#
# # gaofzhan2 = celery_app.tasks[_TestTask.name]
#
# celery_app.tasks.register(_TestTask())

import sys
sys.path.append('../')
from taskModel.db_fresh.job.dynamic_job import DynamicRefresh
from taskModel.db_fresh.job.static_job import StaticRefresh
# StaticRefresh.run('gaofzhan', )
if __name__ == '__main__':
    func, cid = sys.argv[1],sys.argv[2]
    if func == 'static':
        StaticRefresh.run(cid, once=True)
    else:
        DynamicRefresh.run(cid, once=True)