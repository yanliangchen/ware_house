import os
import base64
from flask import make_response
# from flask import send_file


class ResultService:

    @classmethod
    def get_result(cls, job_id):
        path = 'FilesFolder/yaml_gen/%s.zip' % job_id
        if os.path.exists(path):
            with open(path, 'rb') as f:
                content = f.read()
            b64_content = base64.b64encode(content)
            res = make_response(dict(status=True, code=200, data=b64_content.decode('utf-8'))), 200
        else:
            res = make_response(dict(status=False, code=200, data=None)), 200
        return res
