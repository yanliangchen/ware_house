import json
from backend.common.scriptHandler import ScriptHandler
from backend.myBluePrint.ericic.model.dataCenterModel\
    import DataCenterModel
from backend.myBluePrint.ericic.model.hostModel \
    import HostInfo
from backend.myBluePrint.ericic.model.vmModel \
    import VmInfo


class CPULayoutService:

    @classmethod
    def execute(cls, host_id):
        # get host info
        host_obj = HostInfo.get_one_by_id(host_id)
        dc_id = host_obj.data_center_id
        server = host_obj.name
        # get instance info
        instances = ""
        vm_objs = VmInfo.get_entities_with_host_id(host_id)
        name_instance = {}
        if vm_objs:
            for vm in vm_objs:
                if vm:
                    _instance_name = vm.instance_name
                    instance_name = _instance_name.strip() + ','
                    instances += instance_name
                    name_instance[_instance_name.strip()] = vm.name
        # get DC info
        dc_obj = DataCenterModel.get_one_by_id(dc_id)
        if not dc_obj.mode:
            return dict(error=True, message="datacenter is offline")

        SSH = ScriptHandler(
            dc_obj.lcm_ip, dc_obj.lcm_user, dc_obj.lcm_pwd
        )
        get_cpulayout = "get_cpulayout.py"
        SSH.scp_file('FilesFolder/ericic/script/%s' % get_cpulayout, '/tmp/%s' % get_cpulayout)
        if instances == "":
            instances = "''"
        cmd = "python /tmp/%s -s %s -i %s 2>/dev/null" % (get_cpulayout, server, instances)
        ret = SSH.execute_cmd(cmd)
        # ret= """
        # {"socket_info": {"Core0": {"socket 0": [0, 24], "socket 1": [12, 36]}, "Core1": {"socket 0": [1, 25], "socket 1": [13, 37]}, "Core2": {"socket 0": [2, 26], "socket 1": [14, 38]}, "Core3": {"socket 0": [3, 27], "socket 1": [15, 39]}, "Core4": {"socket 0": [4, 28], "socket 1": [16, 40]}, "Core5": {"socket 0": [5, 29], "socket 1": [17, 41]}, "Core8": {"socket 0": [6, 30], "socket 1": [18, 42]}, "Core9": {"socket 0": [7, 31], "socket 1": [19, 43]}, "Core10": {"socket 0": [8, 32], "socket 1": [20, 44]}, "Core11": {"socket 0": [9, 33], "socket 1": [21, 45]}, "Core12": {"socket 0": [10, 34], "socket 1": [22, 46]}, "Core13": {"socket 0": [11, 35], "socket 1": [23, 47]}}, "instance_info": [{"vcpu": [28, 4, 1, 25], "instance": "instance-00000001"}, {"vcpu": [0, 24, 9, 33], "instance": "instance-00000007"}, {"vcpu": [5, 29, 10, 34], "instance": "instance-0000000a"}, {"vcpu": [8, 32, 7, 31], "instance": "instance-0000000d"}]}
        # """
        if isinstance(ret, bytes):
            ret = ret.decode()
        ret = json.loads(ret)
        if vm_objs and ret["instance_info"]:
            for _ in ret["instance_info"]:
                _['vm'] = name_instance.get(_.get("instance"))
        data = dict(data=ret)
        return data
