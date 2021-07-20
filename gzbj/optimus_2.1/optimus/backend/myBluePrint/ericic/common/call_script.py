from flask import g
from backend.common.scriptHandler import ScriptHandler


class OpenstackViewScriptHandler(ScriptHandler):
    total_script = 'infocollect-Ericic4ceeNext'

    def call_cee_info_collect(self, lcmrc_dir, openstackrc_dir, system_name, cid):
        try:
            job_id = g.r_id
        except Exception:
            job_id = self.job_id
        self.execute_cmd('mkdir %s' % job_id)
        self.scp_file('FilesFolder/ericic/script/%s.tar' % self.total_script, '%s.tar' % job_id)
        self.execute_cmd('tar -xvf %s.tar -C %s' % (job_id, job_id))
        cmd_path = 'cd  %s/%s' % (job_id, self.total_script)
        cmd = 'python get_node_info.py -l %s -s %s -o %s' % (lcmrc_dir, system_name, openstackrc_dir)
        self.execute_cmd('%s; %s' % (cmd_path, cmd))
        self.execute_cmd('%s; python test_case/test_optimue_001.py -i %s -n %s' % (cmd_path, job_id, cid))
        json_output = self.execute_cmd('%s; cat output/%s.json' % (cmd_path, job_id))
        target = '%s/%s/output/%s_%s.xlsx' % (job_id, self.total_script, cid, job_id)
        aim = 'FilesFolder/ericic/script_output/%s_%s.xlsx' % (cid, job_id)
        self.get_file(target, aim)
        self.execute_cmd('rm -rf %s*' % job_id)
        return json_output
