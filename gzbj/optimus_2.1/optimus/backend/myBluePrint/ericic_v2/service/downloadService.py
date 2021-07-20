import base64
from backend.myBluePrint.ericic_v2.model.record_table import Record
from backend.myBluePrint.ericic_v2.mongo_post.record_post import RecordPost


class DownloadService:

    @classmethod
    def download(cls, rid):
        record = Record.get_one_by_id(rid)
        if record:
            pid = record.pid
            # get data from mongo db
            ojb = RecordPost.objects(id=pid).first()
            content = ojb.content
            base64_str = base64.b64encode(content).decode('utf-8')
            if content:
                data = dict(total_num=1, data=base64_str)
                return data
            else:
                return dict(total_num=0, data=None)
        else:
            return dict(data=None)
