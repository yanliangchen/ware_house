#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: fan.a.wang@ericsson.com
import re
import json
import argparse
from subprocess import check_output, CalledProcessError
import warnings
warnings.filterwarnings("ignore")
"""
ssh compute1 "docker exec -i nova_libvirt virsh vcpupin instance-0000000a"
ssh compute1 "cpu_layout.py"
"""

CMD = {
        'host': "cpu_layout.py 2>/dev/null",
        "vm": "docker exec -i nova_libvirt virsh vcpupin %s 2>/dev/null"
}


def call_subprocess(cmd, host=False):
    flag = True
    try:
        if host:
            cmd = 'ssh %s "%s"' % (host, cmd)
        # print("run command :%s" % cmd)
        # print('\n')
        result = check_output(cmd, shell=True)
    except CalledProcessError as e:
        result = e
        flag = False
    if isinstance(result, bytes):
        result = result.decode()
    return result, flag


def handel_vm_data(content, instance):
    vcpu = []
    conts = content.split('\n')
    index = 0
    for cont in conts:
        if cont and re.search('----------------------', cont):
            index = conts.index(cont)
            break
    for d in range(index + 1, len(conts)):
        if conts[d] and conts[d].strip():
            vcpu.append(conts[d].strip().split()[-1])

    return {
        "vcpu": vcpu,
        "instance": instance
    }


def handel_host_data(content):
    ret = {}
    conts = content.split('\n')
    index = 0
    for cont in conts:
        if cont and re.search(' --------', cont):
            index = conts.index(cont)
            break
    for d in range(index+1, len(conts)):
        key = conts[d].strip().split('[')[0].replace(' ', '')
        values = conts[d].strip().split('[')[1:]
        if key:
            ret[key] = {}
            i = 0
            for v in values:
                _v = '[' + v
                ret[key]["socket %d" % i] = json.loads(_v.replace(' ', ''))
                i += 1
    return ret


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(
        'get cpu core useage. hypervisor host or virtual machine'))
    parser.add_argument('-s', '--server', required=True,
                        help='hypervisor host ipaddress or hostname.'
                             'if hostname is giving, the value must '
                             'be resolved')

    parser.add_argument('-i', '--instance', required=True,
                        help='VM instance id is required')
    args = parser.parse_args()
    hosts = args.server
    instances = args.instance
    data = {
        "socket_info": {},
        "instance_info": []
    }
    if instances:
        for instance in instances.split(','):
            if instance:
                vm_ret, _ = call_subprocess(CMD['vm'] % instance, host=args.server)
                # vm_ret = """
                #  VCPU   CPU Affinity\n----------------------\n 0      5\n 1      29\n 2      10\n 3      34\n\n
                # """
                if not _:
                    continue
                data["instance_info"].append(handel_vm_data(vm_ret, instance))

    host_ret, _ = call_subprocess(CMD['host'], host=args.server)
    # host_ret = """
    # ======================================================================\nCore and Socket Information (as reported by '/sys/devices/system/cpu')\n======================================================================\n\ncores =  [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13]\nsockets =  [0, 1]\n\n        Socket 0        Socket 1    \n        --------        --------       \nCore 0  [0, 24]         [12, 36]       \nCore 1  [1, 25]         [13, 37]       \nCore 2  [2, 26]         [14, 38]       \nCore 3  [3, 27]         [15, 39]       \nCore 4  [4, 28]         [16, 40]       \nCore 5  [5, 29]         [17, 41]       \nCore 8  [6, 30]         [18, 42]       \nCore 9[7, 31]         [19, 43]       \nCore 10 [8, 32]         [20, 44]       \nCore 11 [9, 33]         [21, 45]       \nCore 12 [10, 34]        [22, 46]       \nCore 13 [11, 35]        [23, 47]       \n
    # """
    data["socket_info"] = handel_host_data(host_ret)
    print(json.dumps(data))

