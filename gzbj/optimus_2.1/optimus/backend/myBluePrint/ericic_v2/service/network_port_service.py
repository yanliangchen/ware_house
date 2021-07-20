#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : network_port_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/24 9:54
# @Desc  :
import re
from backend.myException.myExecption import MyDataConsistencyError
from backend.common.scriptHandler import ScriptHandler
from backend.myBluePrint.ericic_v2.base_dao.network_port_dao import NetworkPortDao
import json
import uuid

OVS_APPCTL = 'sudo ovs-appctl dpctl/show -s'


class NetworkPortService:

    @classmethod
    def get_vm_port_list(cls, cid, vid):
        res = list()
        entity_res = NetworkPortDao.get_dc_vm_entity(cid, vid)
        vm_entity, dc_entity = entity_res['vm_entity'], entity_res['dc_entity']
        if vm_entity and dc_entity:
            port_entities = NetworkPortDao.get_port_entity(cid, vid)
            for port_entity in port_entities:
                binding_vif_type = port_entity.binding_vif_type
                _id = port_entity.id
                name = port_entity.name
                ip_address = port_entity.ip_address
                vif_details = port_entity.vif_details['vhostuser_socket'].split('/')[-1]
                mac_address = port_entity.mac_address
                info = dict(id=_id, name=name, ip_address=ip_address,
                            vif_type=binding_vif_type, vhostuser=vif_details, mac=mac_address)
                res.append(info)
            host_name = vm_entity.host.split('.')[0]
            _ssh_compute = 'ssh %s' % host_name
            ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
            output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, OVS_APPCTL))
            appctl_parsed = cls._appctl_parse(output)
            for item in res:
                vhostuser = item['vhostuser']
                appctl_info = appctl_parsed.get(vhostuser)
                if appctl_info:
                    item['tx_packets'] = appctl_info['tx_packets']
                    item['tx_errors'] = appctl_info['tx_errors']
                    item['tx_dropped'] = appctl_info['tx_dropped']
                    item['rx_packets'] = appctl_info['rx_packets']
                    item['rx_errors'] = appctl_info['rx_errors']
                    item['rx_dropped'] = appctl_info['rx_dropped']
                else:
                    raise MyDataConsistencyError(
                        'Data Consist Error: Maybe the env of the specified data center has been changed, and the changes has not been  synced yet')
        return res

    @classmethod
    def _appctl_parse(cls, output):
        pattern = r'port ([0-9])*: (.*) [(](.*)[)]'
        # t_p = r'TX packets:([0-9]|[?])* errors:([0-9]|[?])* dropped:([0-9]|[?])* aborted:([0-9]|[?])* carrier:([0-9]|[?])*'
        # r_p = r'RX packets:([0-9]|[?])* errors:([0-9]|[?])* dropped:([0-9]|[?])* overruns:([0-9]|[?])* frame:([0-9]|[?])*'
        t_p = r'TX packets:(\d+) errors:([0-9]|[?])* dropped:([0-9]|[?])* aborted:([0-9]|[?])* carrier:([0-9]|[?])*'
        r_p = r'RX packets:(\d+) errors:([0-9]|[?])* dropped:([0-9]|[?])* overruns:([0-9]|[?])* frame:([0-9]|[?])*'
        line_list = output.split('\n')
        info_dict = dict()
        index = 0
        while index < len(line_list):
            line = line_list[index]
            _line = str(line).strip()
            _ = re.match(pattern, _line, )
            if _:
                # info_dict[_.group(2)] = line_list[index:index + 5]
                default_dict = dict(tx_packets=None, tx_errors=None, tx_dropped=None,
                                    rx_packets=None, rx_errors=None, rx_dropped=None)
                _info = info_dict.setdefault(_.group(2), default_dict)
                tx_line = line_list[index + 2].strip()
                rx_line = line_list[index + 1].strip()
                _tx = re.match(t_p, tx_line)
                if _tx:
                    _info['tx_packets'] = _tx.group(1)
                    _info['tx_errors'] = _tx.group(2)
                    _info['tx_dropped'] = _tx.group(3)
                _rx = re.match(r_p, rx_line)
                if _rx:
                    _info['rx_packets'] = _rx.group(1)
                    _info['rx_errors'] = _rx.group(2)
                    _info['rx_dropped'] = _rx.group(3)
                index = index + 5
            else:
                index += 1
        return info_dict

    @classmethod
    def dynamic_port(cls, port_res,dc_id,uid):
        port_ress = json.dumps(port_res)


        NetworkPortDao.save_port_data(_id=uid, port_data=port_ress,dc_id=dc_id)
        return uid

    @classmethod
    def select_port(cls, _id):
        res = NetworkPortDao.select_port_data(_id=_id)
        return  res
