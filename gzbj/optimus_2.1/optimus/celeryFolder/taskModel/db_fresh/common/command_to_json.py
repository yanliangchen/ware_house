#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : command_to_json.py
# @Author: yanliang
# @Email: yanliang.li@ericssoin.com
# @Date  : 2020/12/3 14:59
# @Desc  : 

import logging
import json


class command_to_json:

    def str2json(self, content):
        """

        例：
        +--------------------------------------+---------+--------+
        | ID                                   | Name    | Flavor |
        +--------------------------------------+---------+--------+
        | fb172b8f-104c-4770-a71f-83cdf3d1d7be | RZ_test | 1      |
        | cd68ced3-d1b4-490a-8aaa-0f3368a56355 | sjx     | 2      |
        | 671768c1-02cc-4207-932a-6809ef320e03 | test4   | test   |
        +--------------------------------------+---------+--------+

        :return: json
        """

        index_list = []
        record = []
        result = []

        strs = content.split("\n")
        for index in range(len(strs)):
            line = strs[index]
            if index == 0:
                header = line
                index_list = [i for i in range(len(header)) if header[i] == "+"]
                if header is None or len(header.strip()) == 0:
                    return "[]"
                if len(index_list) == 0:
                    logging.error("字符串格式错误，请检查！")
                    return
            elif index == 1:
                # 提取列名
                for i in range(len(index_list) - 1):
                    key = line[index_list[i] + 1:index_list[i + 1]].strip()
                    record.append(key)
            else:
                if line.count("+") == len(index_list) or len(line) == 0:
                    continue
                else:
                    # 提取数据
                    record_dic = {}
                    for i in range(len(index_list) - 1):
                        key = record[i]
                        value = line[index_list[i] + 1:index_list[i + 1]].strip()
                        record_dic[key] = self.get_value(value)

                    result.append(record_dic)

        result = json.dumps(result)
        logging.info(result)
        return result

    def get_value(self, value):
        try:
            va_dic = {}
            if value is None or value == '':
                return ''
            elif (value[0] == '{' and value[-1] == '}') or (value[0] == '[' and value[-1] == ']'):
                return json.loads(json.dumps(eval(value)))
            elif 0 < (value.count(",") + 1) == value.count("="):

                sp = value.split(",")
                for s in sp:
                    kv = s.split("=")
                    k = kv[0].strip()
                    v = kv[1]
                    if v[0] == "'" and v[-1] == "'":
                        v = v[1:-1]
                    if 0 < (v.count(",") + 1) == v.count("="):
                        return self.get_value(v)
                    else:
                        va_dic[k] = v
                return va_dic

            else:
                return value
        except BaseException as e:
            logging.error("转换数据错误:%s", value)
            raise e

    def test(self, ret):
        # 打开文件
        # file_handle = open("./demo.txt", "r")
        # content = file_handle.read()
        result = self.str2json(ret)
        return result
        # print(type(result))
        # print(json.loads(result))
        # print(type(json.loads(result)))

        # 以json格式写入文件
        # with open("demo.json", "w") as fp:
        #     fp.truncate()
        #     fp.write(json.dumps(result, indent=2))
