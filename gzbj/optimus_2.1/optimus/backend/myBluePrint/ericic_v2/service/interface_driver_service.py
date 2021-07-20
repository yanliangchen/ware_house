#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : interface_driver_service.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/22 15:18
# @Desc  :
# from ifcfg.parser import UnixIPParser
from backend.common.loghandler import ServiceLog
from backend.common.scriptHandler import ScriptHandler
from backend.myException.myExecption import MyRuntimeError
from backend.myBluePrint.ericic_v2.common.ifcfg_tool import IpAddressParser
from backend.myBluePrint.ericic_v2.base_dao.interface_driver_dao import InterfaceDriverDao

IP_A = 'ip a'
INTERFACE_NODE_LIST = ['control0', 'control1', 'storage0', 'storage1']
LSPCI = 'sudo lspci'
ETHTOOL_I = 'sudo ethtool -i {node}'
ETHTOOL_S = 'sudo ethtool -S {node}'


class InterfaceDriverService:

    @classmethod
    def get_driver_firmware_info(cls, cid, hid):
        response_data = dict(static=dict(), firmware=dict())
        # this function needs to be adaptive suse centos redhat in the further
        res = InterfaceDriverDao.get_dc_host_info(cid, hid)
        dc_entity, host_entity = res['dc_entity'], res['host_entity']
        if dc_entity and host_entity:
            ssh_tunnel = ScriptHandler(dc_entity.lcm_ip, dc_entity.lcm_user, dc_entity.lcm_pwd)
            host_name = host_entity.host.split('.')[0]
            _ssh_compute = 'ssh %s' % host_name
            try:
                ssh_tunnel.execute_cmd('%s "pwd"' % _ssh_compute)
            except Exception:
                raise MyRuntimeError('can not ssh the verify %s' % host_name, 503)
            # exec "ip a"
            output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, IP_A))
            parsed_ip_info = IpAddressParser(ifconfig=output).interfaces
            res_info = dict()
            # exec "sudo ethtool -i control0"
            for node in INTERFACE_NODE_LIST:
                _ = res_info.setdefault(node, dict(i=dict(), s=dict()))
                output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, ETHTOOL_I.format(node=node)))
                parsed_ethtool_info_i = cls._format_ethtool(output)
                _['i'] = parsed_ethtool_info_i
                # get control0, control1, storage0, storage1  statistics info
                output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, ETHTOOL_S.format(node=node)))
                parsed_ethtool_info_s = cls._format_ethtool(output)
                _['s'] = parsed_ethtool_info_s
            # exec sudo lspci
            pci_output = ssh_tunnel.execute_cmd('%s "%s"' % (_ssh_compute, LSPCI))
            parsed_pci_info = cls._format_pci_ouput(pci_output)

            for node in INTERFACE_NODE_LIST:
                parsed_ethtool_info_i = res_info[node]['i']
                parsed_ethtool_info_s = res_info[node]['s']
                mac = parsed_ip_info[node]['ether']
                pci_number = parsed_ethtool_info_i['bus-info']

                # get static
                rx_errors = int(parsed_ethtool_info_s['rx_errors'])
                rx_dropped = int(parsed_ethtool_info_s['rx_dropped'])
                rx_packets = int(parsed_ethtool_info_s['rx_packets'])
                tx_packets = int(parsed_ethtool_info_s['tx_packets'])
                tx_errors = int(parsed_ethtool_info_s['tx_errors'])
                tx_dropped = int(parsed_ethtool_info_s['tx_dropped'])
                static_info = dict(interface=node, mac=mac, pci_number=pci_number, rx_errors=rx_errors,
                                   rx_dropped=rx_dropped, tx_packets=tx_packets, tx_errors=tx_errors,
                                   tx_dropped=tx_dropped, rx_packets=rx_packets)
                response_data['static'][node] = static_info

                # firmware
                driver = parsed_ethtool_info_i['driver']
                firmware_version = parsed_ethtool_info_i['firmware-version']
                driver_info = parsed_ethtool_info_i['version']

                desc = parsed_pci_info[pci_number.split(':', 1)[1]]
                firmware_info = dict(interface=node, mac=mac, pci_number=pci_number, driver=driver,
                                     driver_info=driver_info, firmware_version=firmware_version, desc=desc)
                response_data['firmware'][node] = firmware_info
        return response_data

    @classmethod
    def _format_pci_ouput(cls, lspci_output):
        res = dict()
        line_list = lspci_output.split('\n')
        for line in line_list:
            if line:
                k, v = line.split(' ', 1)
                k, v = k.strip(), v.strip()
                res[k] = v
        return res

    @classmethod
    def _format_ethtool(cls, output):
        # pci、driver、version、firmware
        info = dict()
        line_list = output.split('\n')
        for line in line_list:
            if line:
                # ServiceLog.info(line)
                k, v = line.split(':', 1)
                k, v = k.strip(), v.strip()
                info[k] = v
        return info
