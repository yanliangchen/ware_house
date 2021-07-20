#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : cpu_layout_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/17 21:05
# @Desc  :
import re
import json
from backend.myException.myExecption import MyRuntimeError
from backend.common.scriptHandler import ScriptHandler
# from taskModel.db_fresh.cmd_mapping import EXEC_LIBVIRT
# from backend.common.loghandler import ServiceLog
from backend.myBluePrint.ericic_v2.base_dao.cpu_layout_dao import CpuLayoutDao

VIRSH_LIST = 'docker exec -i nova_libvirt virsh list'
VCPU_PIN = 'docker exec -i nova_libvirt virsh vcpupin {name}'
OVS_CPU = 'sudo cat /proc/cmdline '
CPU_PIN_SET = "sudo cat /etc/kolla/nova-compute/nova.conf | grep -E '(cpu_pin_set|cpu_shared_set|cpu_dedicated_set)'"
DUMPXML = 'docker exec -i nova_libvirt virsh dumpxml {name} '

class CpuLayoutService:

    @classmethod
    def get_cpu_layout_info(cls, cid, hid):
        data = {
            "socket_info": {},
            "instance_info": [],
            "cpu_free_info": {},
            "ovs_info": {}
            
        }
        res = CpuLayoutDao.get_dc_host_info(cid, hid)
        dc_entity, host_entity = res['dc_entity'], res['host_entity']
        if dc_entity and host_entity:
            ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
            # ssh_tunnel.source_file(dc_entity.openstackrc_dir)
            host_name = host_entity.host.split('.')[0]
            _ssh_compute = 'ssh %s' % host_name
            try:
                ssh_tunnel.execute_cmd('%s "pwd"' % _ssh_compute)
            except Exception:
                raise MyRuntimeError('can not ssh the verify %s' % host_name, 503)
            output = ssh_tunnel.execute_cmd('%s "cpu_layout.py"' % _ssh_compute)
            ret,socket = cls._handel_host_data(output)
            data['socket_info'] = ret
            # ServiceLog.info('++++++++++++++++++')
            # ServiceLog.info(ret)
            # ServiceLog.info('++++++++++++++++++')
            output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, VIRSH_LIST))
            # ServiceLog.info('****************')
            # ServiceLog.info(output)
            # ServiceLog.info('****************')
            instance_info_list = cls._format_virsh_list(output)
            ins_name_list = list()
            for instance_info in instance_info_list:
                instance_name = instance_info['name']
                i_output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, VCPU_PIN.format(name=instance_name)))
                i_output = cls._handel_vm_data(i_output, instance_name)
                # ServiceLog.info(i_output)
                # ServiceLog.info('&&&&&&&&&&&&&&&&')
                data['instance_info'].append(i_output)
                ins_name_list.append(instance_name)
            # vm_entity_info = CpuLayoutDao.get_vm_info(cid, ins_name_list)

            # get vm reserved cpu data        
            cpu_pin_set = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, CPU_PIN_SET))            
            vm_reserved_cpu_list = cls.__handel_reserved_cpu_data(cpu_pin_set)
            
            for item in data['instance_info']:
                instance_name = item['instance']
                # item['vm'] = vm_entity_info[instance_name].name
                dumpxml_output = ssh_tunnel.execute_cmd('%s "%s"'%(_ssh_compute,DUMPXML.format(name=instance_name)))
                item['vm'] = cls._get_name_from_dumpxml(dumpxml_output)
                vm_reserved_cpu_list = list(set(vm_reserved_cpu_list) - set(item['vcpu']))
                        
            #get ovs cpu list 
            ovs_output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, OVS_CPU))
            ovs_cpu_list = re.search(r"nohz_full=(?P<ovs_cpu>[,|\d]*\d\s)", ovs_output)
            ovs_cpu_list = ovs_cpu_list.group('ovs_cpu')
            ovs_cpu_list = ovs_cpu_list.strip().split(",")
            
            #get socket info for ovs and free vm cpu
            vm_cpu_free_info = {}
            ovs_info = {}
            for key,value in socket.items():
                vm_cpu_free_info[key] = list(set(value) & set(vm_reserved_cpu_list))
                ovs_info[key] = list(set(value) & set(ovs_cpu_list))
            data["ovs_info"] = ovs_info
            data["cpu_free_info"] = vm_cpu_free_info
        else:
            pass
        return data

    @classmethod
    def _handel_host_data(cls, content):
        # this func is to format the cpu_layout.py's output, and the code cames from fan wang
        ret = {}
        conts = content.split('\n')
        index = 0
        for cont in conts:
            if cont and re.search(' --------', cont):
                index = conts.index(cont)
                break
        
        socket_nums = re.search("Core\s\d.*\[.*\]",content).group(0)
        socket_nums = socket_nums.count("[")
        socket = {}
        for socket_num in range(socket_nums):
            socket_num_key = "socket %s"%socket_num
            ret[socket_num_key] = {}     
            socket[socket_num_key] = []     
            
        for d in range(index + 1, len(conts)):
            key = conts[d].strip().split('[')[0].replace(' ', '')
            values = conts[d].strip().split('[')[1:]
            if key:
                # ret[key] = {}
                i = 0
                for v in values:
                    _v = '[' + v
                    ret["socket %d" % i][key] = json.loads(_v.replace(' ', ''))
                    cpu_id = v.replace(' ','').replace(']','')
                    cpu_id = cpu_id.split(',')
                    socket["socket %d" % i].extend(cpu_id)
                    i += 1  
        return ret,socket

    @classmethod
    def _handel_vm_data(cls, content, instance):
        # this func is to format the vm's output, and the code cames from fan wang
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

    @classmethod
    def _format_virsh_list(cls, info):
        res_list = info.split('\n')
        _ = 0
        for i in res_list:
            if i.startswith('------'):
                break
            _ += 1
        res_list = res_list[_ + 1:]
        response = list()
        for i in res_list:
            if i:
                info_list = i.split(' ')
                info_list = [i for i in info_list if i != '']
                response.append(dict(id=info_list[0], name=info_list[1], status=info_list[2]))
        return response

    @classmethod
    def __handel_reserved_cpu_data(cls,cpu_sets):
        vm_reserved_cpu_list = []
        cpu_sets = cpu_sets.split("\n")
        for cpu_set in cpu_sets:
            if cpu_set == "":
                continue
            vm_core_list = []
            except_list = []
            cpu_set = cpu_set.split('=')[-1]
            cpu_set = cpu_set.split(',')
            for vcpu in cpu_set:
                if "-" in vcpu:
                    vm_cpu = vcpu.split("-")
                    vm_core = [str(i) for i in range(int(vm_cpu[0]), int(vm_cpu[-1])+1)]
                    vm_core_list.extend(vm_core)
                elif "^" in vcpu:
                    vm_cpu = vcpu.strip("^")
                    except_list.append(vm_cpu)
                else:
                    vm_core_list.append(str(vcpu))

            if len(vm_reserved_cpu_list):
                vm_reserved_cpu_list = list(set(vm_core_list) & set(vm_reserved_cpu_list))
                vm_reserved_cpu_list = list(set(vm_reserved_cpu_list) - set(except_list))
            else:
                vm_reserved_cpu_list.extend(vm_core_list)
                vm_reserved_cpu_list = list(set(vm_reserved_cpu_list) - set(except_list))
        return vm_reserved_cpu_list
    
    @classmethod
    def _get_name_from_dumpxml(cls,dumpxml_output):
        res = re.search(r"<nova:name>(.*)</nova:name>",dumpxml_output)
        res = res.group(1)
        return res