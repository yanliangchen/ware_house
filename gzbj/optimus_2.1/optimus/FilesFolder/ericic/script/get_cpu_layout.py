#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Author: fan.a.wang@ericsson.com
import sys
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
    return result, flag


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(
        'get cpu core useage. hypervisor host or virtual machine'))
    parser.add_argument('-t', '--type', required=True,
                        choices=['vm', 'host'],
                        help='args must in "vm" or "host" ')
    parser.add_argument('-s', '--server', required=True,
                        help='hypervisor host ipaddress or hostname.'
                             'if hostname is giving, the value must '
                             'be resolved')

    parser.add_argument('-i', '--instance', required=False,
                        help='VM instance id is required')
    args = parser.parse_args()

    if args.type == 'vm':
        if not args.instance:
            print("usage: get_cpu.py [-h] -t {vm,host} -s SERVER [-i INSTANCE] \n"
                  "if type is 'vm' -i/--instance arguments are required \n"
                  "get_cpu.py: error: the following arguments are required: "
                  "-t/--type, -s/--server, -i/--instance"
                  )
            sys.exit(1)
        else:
            ret, _ = call_subprocess(CMD[args.type] % args.instance, host=args.server)
            # print(ret)

    elif args.type == 'host':
        ret, _ = call_subprocess(CMD[args.type], host=args.server)
        # print(ret)

    if isinstance(ret, bytes):
        ret = ret.decode()
    print(ret)
