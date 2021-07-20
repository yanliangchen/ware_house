from sqlalchemy import Column, String, Integer
from backend.Model.connection import BASE


class RefreshTaskHistoryModel(BASE):
    __tablename__ = 'refresh_task_history_table'

    id = Column(String(255), primary_key=True)
    task_name = Column(String(50), )
    dc_id = Column(String(50), )
    dc_name = Column(String(50), )
    status = Column(String(50), )
    error_info = Column(String(50), )
    timestamp = Column(Integer(), nullable=False)
    # version = Column(Integer(), nullable=False, default=0)

    def __init__(self, _id, task_name, dc_id, dc_name, status, error_info, timestamp):
        self.id = _id
        self.task_name = task_name
        self.dc_id = dc_id
        self.dc_name = dc_name
        self.status = status
        self.error_info = error_info
        self.timestamp = timestamp
