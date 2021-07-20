#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : format_table.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2020/12/4 10:35
# @Desc  :
import time
import datetime

TABLE_BORDER_TAG = '+-', '-+'
ROW_TAG = '|'


def table_format(output):
    result = list()
    output_line_list = output.split("\n")
    border_tags = list()
    for index in range(len(output_line_list)):
        output_line = output_line_list[index]
        if output_line.startswith(TABLE_BORDER_TAG[0]) and output_line.endswith(TABLE_BORDER_TAG[1]):
            border_tags.append(index)
    if len(border_tags) != 0 and output:
        if len(border_tags) != 3 and border_tags[1] - border_tags[0] != 2:
            raise RuntimeError('unexpeted output format')

        title_line = output_line_list[border_tags[0] + 1]
        title_list = [i.strip() for i in title_line.split(ROW_TAG) if i != '']

        body_lines = output_line_list[border_tags[1] + 1:border_tags[2]]

        for body_line in body_lines:
            item_info_dict = dict()
            body_info = [i.strip() for i in body_line.split(ROW_TAG) if i != '']
            for index in range(len(title_list)):
                item_key = title_list[index]
                item_value = body_info[index]
                item_info_dict[item_key] = item_value
            result.append(item_info_dict)
    return result


def time_format(item):
    if 'T' in item and 'Z' in item:
        temp = "%Y-%m-%dT%H:%M:%SZ"
    elif '.' in item and 'T' in item:
        temp = "%Y-%m-%dT%H:%M:%S.%f"
    else:
        raise Exception('unknown time template')
    d = datetime.datetime.strptime(item, temp)
    t = d.timetuple()
    time_stamp = int(time.mktime(t))
    return time_stamp

import json
json.loads('{"ovs_hybrid_plug": "False", "vhostuser_socket": "/var/run/openvswitch/vhu0c3c8403-6f", "datapath_type": "netdev", "vhostuser_mode": "server", "port_filter": "False", "vhostuser_ovs_plug": "True"}')
#

# json.loads("{'id':'id'}".replace("'", '"'))