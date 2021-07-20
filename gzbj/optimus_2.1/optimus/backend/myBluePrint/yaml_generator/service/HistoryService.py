import pytz
from datetime import datetime
from backend.myBluePrint.yaml_generator.model.TaskModel import Task


class HistoryService:

    @classmethod
    def get_all_task(cls):
        res = list()
        tz = pytz.timezone('Asia/Shanghai')
        for task in Task.get_all_task():
            info_dict = dict()
            info_dict['id'] = task.id
            # info_dict['user'] = task.user
            info_dict['project_name'] = '%s_%s' % (task.site_name, task.project_name)
            # info_dict['site_name'] = task.site_name
            info_dict['cee_version'] = task.cee_version
            info_dict['status'] = task.status
            # info_dict['input'] = task.input
            # info_dict['output'] = task.output
            # info_dict['timestamp'] = datetime.datetime.fromtimestamp(task.timestamp)
            # info_dict['timestamp'] = time.strftime("%Y-%m-%d %H:%M", time.localtime(task.timestamp))
            info_dict['timestamp'] = datetime.fromtimestamp((task.timestamp), tz).strftime('%Y-%m-%d %H:%M:%S')

            res.append(info_dict)
        return res

    @classmethod
    def delete_history(cls, id_list):
        Task.invisible_history_items(id_list)
