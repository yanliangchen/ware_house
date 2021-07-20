#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : ifcfg_tool.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/23 16:40
# @Desc  : 
from ifcfg.parser import UnixIPParser


class IpAddressParser(UnixIPParser):

    @classmethod
    def get_patterns(cls):
        return [
            r'\s*[0-9]+:\s+(?P<device>[^@:]+)[^:]*:.*mtu (?P<mtu>\d+)',
            # r'.*(inet\s)(?P<inet4>[\d\.]+)',
            r'.*(inet6 )(?P<inet6>[^/]*).*',
            r'.*(ether )(?P<ether>[^\s]*).*',
            r'.*inet\s.*(brd )(?P<broadcast>[^\s]*).*',
            r'.*(inet )[^/]+(?P<netmask>[/][0-9]+).*',
        ]
