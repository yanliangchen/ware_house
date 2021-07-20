import re
import os
import time
import uuid
import shutil
import copy
import zipfile
import sqlite3
import traceback
from flask import g
from collections import OrderedDict
from backend.myBluePrint.yaml_generator.model.TaskModel import Task
from backend.myBluePrint.yaml_generator.com.yamlHandler import YamlOp
from backend.myBluePrint.yaml_generator.com.excelHandler import ExcelOp


class YamlGenService:

    @staticmethod
    def yaml_gen(site, cee_ver, pjt_name, yaml_list, excel, user):
        job_id = uuid.uuid4().hex
        yaml_info_dict = dict()
        task = Task(job_id, user, pjt_name, site, cee_ver, 'running', int(time.time()))
        task.add()
        g.cee_ver = cee_ver
        status = 'success'
        try:
            for yaml_item in yaml_list:
                name = yaml_item.filename
                yaml_op = YamlOp(stream=copy.deepcopy(yaml_item.stream), file=None)
                yaml_input = yaml_op.info
                yaml_info_dict[name] = yaml_input
            yaml_names = yaml_info_dict.keys()

            excel_op_host = ExcelOp(file=copy.deepcopy(excel.stream._file), sheet='hosts')
            excel_op_net = ExcelOp(file=copy.deepcopy(excel.stream._file), sheet='networks')
            YamlGenService.save_input(job_id, excel, yaml_list)

            con = sqlite3.connect('localDatabase/yaml_gen/%s_SERVER.db' % site, check_same_thread=False)
            deploy_models = YamlGenService.get_deploy_models(con=con, excel_op_host=excel_op_host)
            db_info_list = YamlGenService.get_db_info_list(con)
            con.close()

            yaml_res_dict = dict()
            if 'hosts.yaml' in yaml_names:
                yaml_input = yaml_info_dict['hosts.yaml']
                kwargs = dict(excel_op=excel_op_host, db_info_list=db_info_list, yaml_input=yaml_input)
                yaml_res_dict['hosts.yaml'] = HostGenService.run(**kwargs)
            if 'networks.yaml' in yaml_names:
                yaml_input = yaml_info_dict['networks.yaml']
                kwargs = dict(excel_op_net=excel_op_net, yaml_input=yaml_input, excel_op_host=excel_op_host, )
                yaml_res_dict['networks.yaml'] = NetworkGenService.run(**kwargs)
            if 'interface_assignment.yaml' in yaml_names:
                yaml_input = yaml_info_dict['interface_assignment.yaml']
                kwargs = dict(deploy_models=deploy_models, yaml_input=yaml_input, excel_op=excel_op_net, )
                yaml_res_dict['interface_assignment.yaml'] = InterfaceGenService.run(**kwargs)
            if 'host_profile.yaml' in yaml_names:
                yaml_input = yaml_info_dict['host_profile.yaml']
                kwargs = dict(deploy_models=deploy_models, yaml_input=yaml_input)
                yaml_res_dict['host_profile.yaml'] = HostProfileGenService.run(**kwargs)
            YamlGenService.check_id(yaml_res_dict)
            YamlGenService.save_output(job_id, yaml_res_dict)
        except Exception:
            if os.path.exists('FilesFolder/yaml_gen/%s.zip' % job_id):
                shutil.rmtree('FilesFolder/yaml_gen/%s.zip' % job_id)
            status = 'failed'
            e = traceback.format_exc()
            raise e
        finally:
            Task.update_status_by_id(job_id, status)
            if os.path.exists('FilesFolder/yaml_gen/%s' % job_id):
                shutil.rmtree('FilesFolder/yaml_gen/%s' % job_id)
        return job_id

    @classmethod
    def check_id(cls, yaml_res_dict):
        res_host = yaml_res_dict.get('hosts.yaml')
        if res_host:
            physical_list = res_host['physicalHosts']
            for item in physical_list:
                item['id'] = item['id'] if item['id'] else str(uuid.uuid4())

    @staticmethod
    def get_deploy_models(**kwargs):
        cee_ver = g.cee_ver
        result = list()
        p = re.compile(r'[\u4e00-\u9fa5]')
        want_dict = dict()
        if cee_ver == 'drop26':
            con = kwargs.get('con')
            result = list()
            cur = con.cursor()
            res = cur.execute("select distinct(deploy_module) from table_device")
            for item in res:
                try:
                    istr = item[0].decode('utf-8')
                except UnicodeEncodeError and AttributeError:
                    istr = item[0]
                _ = p.split(istr)
                _site = _[0].lower()
                _num = int(_[-1])
                _l = want_dict.setdefault(_site, list())
                _l.append(_num)
        elif cee_ver == 'drop28':
            excel_op_host = kwargs.get('excel_op_host')
            models = list()
            for i in excel_op_host.get_col_value(16)[1:]:
                if i is not None:
                    models.append(i)
            models = set(models)
            for i in models:
                _ = p.split(i)
                _site = _[0].lower()
                _num = int(_[-1])
                _l = want_dict.setdefault(_site, list())
                _l.append(_num)
        sites = sorted(want_dict.keys())
        for site in sites:
            nums = sorted(want_dict[site])
            for num in nums:
                result.append('%s%s' % (site, num))
        return result

    @staticmethod
    def get_db_info_list(con):
        cur = con.cursor()
        column_info = cur.execute("PRAGMA table_info(table_device)")
        column_list = [i[1] for i in column_info]
        db_info_list = list()
        db_infos = cur.execute("select * from table_device")

        for item in db_infos:
            _dict = dict()
            for i in range(len(item)):
                column_name = column_list[i]
                value = item[i]
                _dict[column_name] = value
            db_info_list.append(_dict)

        return db_info_list

    @staticmethod
    def save_input(job_id, excel, yaml_list):
        os.mkdir('FilesFolder/yaml_gen/%s' % job_id)
        os.mkdir('FilesFolder/yaml_gen/%s/upload' % job_id)
        for yaml_item in yaml_list:
            yaml_item.save('FilesFolder/yaml_gen/%s/upload/%s' % (job_id, yaml_item.filename))
        excel.save('FilesFolder/yaml_gen/%s/upload/%s' % (job_id, excel.filename))

    @staticmethod
    def save_output(job_id, yaml_res_dict):
        os.mkdir('FilesFolder/yaml_gen/%s/download' % job_id)
        for name, info in yaml_res_dict.items():
            YamlOp.ordered_yaml_dump(data=info, file='FilesFolder/yaml_gen/%s/download/%s' % (job_id, name))
        startdir = 'FilesFolder/yaml_gen/%s' % job_id

        file_news = startdir + '.zip'  # 压缩后文件夹的名字
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
                # print('压缩成功')
        z.close()


class BaseGenService:

    @classmethod
    def run(cls, *args, **kwargs):
        pass

    @classmethod
    def format_db_info(cls, *args, **kwargs):
        pass

    @classmethod
    def list_set_key(cls, info_list, dest_key):
        info_dict = OrderedDict()
        for item in info_list:
            key = item[dest_key]
            info_dict[key] = item
        return info_dict

    @classmethod
    def get_excel_info_list(cls, excel_op):
        info_list = list()
        row, clo = excel_op.get_row_clo_num()
        title = excel_op.get_row_value(1)
        for i in range(2, row + 1, 1):
            row_values = excel_op.get_row_value(i)
            _info_dict = dict()
            for _i in range(len(row_values)):
                key = title[_i]
                value = row_values[_i]
                _info_dict[key] = value
            info_list.append(_info_dict)
        return info_list

    @classmethod
    def format_excel_info(cls, excel_op, dest_key):
        info_dict = OrderedDict()
        row, clo = excel_op.get_row_clo_num()
        title = excel_op.get_row_value(1)
        for i in range(2, row + 1, 1):
            row_values = excel_op.get_row_value(i)
            _info_dict = dict()
            dict_key = None
            for _i in range(len(row_values)):
                key = title[_i]
                value = row_values[_i]
                _info_dict[key] = value
                if key == dest_key:
                    dict_key = row_values[_i]
            info_dict[dict_key] = _info_dict
        return info_dict

    @classmethod
    def get_temp(cls, *args, **kwargs):
        pass


class HostGenService(BaseGenService):
    OOBMTYPE = 'ipmi'
    TEMP_CACHE = dict()

    @classmethod
    def get_temp(cls, _type, yaml_input):
        cache = cls.TEMP_CACHE.get(_type, None)
        if not cache:
            for key, value in yaml_input.items():
                if key not in ['physicalHosts', 'virtualHosts']:
                    continue
                for _item in value:
                    _item_type = _item['hostProfile']
                    if _type == _item_type:
                        cls.TEMP_CACHE[_type] = copy.deepcopy(_item)
                        return copy.deepcopy(cls.TEMP_CACHE[_type])
        return copy.deepcopy(cache)

    @classmethod
    def run(cls, *args, **kwargs):
        cee_ver = g.cee_ver
        excel_op = kwargs.get('excel_op')
        db_info_list = kwargs.get('db_info_list')
        yaml_input = kwargs.get('yaml_input')
        if cee_ver == 'drop26' or cee_ver == 'drop28':
            excel_info_list = cls.get_excel_info_list(excel_op)
            excel_info_dict = cls.list_set_key(excel_info_list, 'hostname')
            db_info_dict = cls.list_set_key(db_info_list, 'device_name')
            cls.update_yaml_item(yaml_input, excel_info_dict, db_info_dict)
            yaml_insert_info = cls.get_yaml_insert_item(excel_info_dict, yaml_input, db_info_dict)
            phy_ins = yaml_insert_info['phy']
            vir_ins = yaml_insert_info['vir']
            yaml_input['physicalHosts'].extend(phy_ins)
            yaml_input['virtualHosts'].extend(vir_ins)
        return yaml_input

    @classmethod
    def update_yaml_item(cls, yaml_input, excel_info_dict, db_info_dict):
        for key, value in yaml_input.items():
            if key not in ['physicalHosts', 'virtualHosts']:
                continue
            for _item in value:
                yaml_host = _item['hostname']
                _item_type = _item['hostProfile']
                input_info = excel_info_dict.pop(yaml_host, None)
                if _item_type != 'compute' or not input_info:
                    continue
                cls.update_inner_item(_item, db_info_dict, excel_info_dict)

    @classmethod
    # TODO: this func is to dynamic generate the oobmExtra item
    def dynamic_gen(cls, name):
        return 'todo:func -- %s' % name

    @classmethod
    def get_yaml_insert_item(cls, excel_info_dict, yaml_input, db_info_dict):
        vir_insert_list = list()
        phy_insert_list = list()
        none_list = list()
        p = re.compile(r'[\u4e00-\u9fa5]')
        for hostname, value in excel_info_dict.items():
            host_type = value['physicalHosts or virtualHosts']
            this_insert_list = phy_insert_list if host_type == 'physicalHosts' else vir_insert_list
            _type = value.get('type(controller/compute/lcm/monitor)')
            temp = cls.get_temp(_type, yaml_input)
            if temp:
                temp['hostname'] = hostname
                cls.update_inner_item(temp, db_info_dict, excel_info_dict)
                temp.pop('ipAddr') if 'ipAddr' in temp else None
                _id = value.get('id')
                temp['id'] = _id if (_id and _id is not None) else str(uuid.uuid4())
                _ = p.split(value['deploy_module'])
                _site = _[0].lower()
                _num = int(_[-1])
                temp['hostProfile'] = '%s_%s%s' % (temp['hostProfile'], _site, _num)
                this_insert_list.append(temp)
            else:
                none_list.append(hostname)
        return dict(vir=vir_insert_list, phy=phy_insert_list, non=none_list)

    @classmethod
    def update_inner_item(cls, _item, db_info_dict, excel_input_info):
        cee_ver = g.cee_ver
        _excel_info = excel_input_info.get(_item['hostname'])
        for _key, _value in _item.items():
            if _key == 'oobm':
                _db_info = db_info_dict.get(_item['hostname'].upper(), None)
                if not _db_info:
                    raise Exception('can not find the matched item in db file, the hostname is %s' % _item['hostname'])
                for _key_ in _value:
                    update_value = None
                    if _key_ == 'oobmAddress':
                        if _excel_info.get('bmc_ipv6', None):
                            update_value = _excel_info.get('bmc_ipv6', None)
                        else:
                            update_value = _db_info.get('bmc_ipv6', None)
                    elif _key_ == 'oobmPassword':
                        _value_ = _excel_info.get('bmc_passwd', None) if _excel_info.get('bmc_passwd',
                                                                                         None) else _db_info.get(
                            'bmc_passwd', None)
                        update_value = _value_
                    elif _key_ == 'oobmUser':
                        _value_ = _excel_info.get('bmc_username', None) if _excel_info.get('bmc_username',
                                                                                           None) else _db_info.get(
                            'bmc_username', None)
                        update_value = _value_
                    elif _key_ == 'oobmType':
                        update_value = cls.OOBMTYPE
                    elif _key_ == 'oobmExtra':
                        for k, v in _value[_key_].items():
                            _update_value = None
                            if k == 'certVerify':
                                continue
                            else:
                                if cee_ver == 'drop26':
                                    _update_value = cls.dynamic_gen(k)
                                elif cee_ver == 'drop28':
                                    _update_value = _excel_info.get(k, None)
                            if _update_value:
                                _item[_key][_key_][k] = _update_value
                    if update_value:
                        _item[_key][_key_] = update_value
            else:
                update_value = _excel_info.get(_key, None)
                if update_value:
                    _item[_key] = update_value


class HostProfileGenService(BaseGenService):

    @classmethod
    def run(cls, *args, **kwargs):
        deploy_models = kwargs.get('deploy_models')
        cee_ver = g.cee_ver
        yaml_input = kwargs.get('yaml_input')
        if cee_ver == 'drop26' or cee_ver == 'drop28':
            index_temp = cls.get_index_and_temp(yaml_input)
            temp = index_temp['temp']
            index = index_temp['index'] + 1

            insert_list = cls.get_insert_list(deploy_models, temp)
            first_list = yaml_input['hostProfiles'][:index]
            end_list = yaml_input['hostProfiles'][index:]

            new_profile_list = first_list + insert_list + end_list
            yaml_input['hostProfiles'] = new_profile_list
        return yaml_input

    @classmethod
    def get_index_and_temp(cls, yaml_input):
        cee_ver = g.cee_ver
        temp_name = 'compute'
        if cee_ver == 'drop28':
            temp_name = 'compute_module'
        host_profile = yaml_input['hostProfiles']
        for index in range(len(host_profile)):
            item = host_profile[index]
            name = item['name']
            if name == temp_name:
                return dict(temp=copy.deepcopy(item), index=index)
        raise Exception('can not find the item named compute')

    @classmethod
    def get_insert_list(cls, deploy_modules, temp):
        cee_ver = g.cee_ver
        insert_list = list()
        for module in deploy_modules:
            _item = copy.deepcopy(temp)
            if cee_ver == 'drop26':
                _item['name'] = '%s_%s' % (_item['name'], module)
                _item['interfaceAssignment'] = '%s_%s' % (_item['interfaceAssignment'], module)
            elif cee_ver == 'drop28':
                _item['name'] = '%s_%s' % ('compute', module)
                _item['interfaceAssignment'] = '%s_%s' % ('compute', module)
            insert_list.append(_item)
        return insert_list


class NetworkGenService(BaseGenService):

    @classmethod
    def run(cls, *args, **kwargs):
        yaml_input = kwargs.get('yaml_input')
        excel_op_net = kwargs.get('excel_op_net')

        excel_info_list = cls.get_excel_info_list(excel_op_net)
        update_dict, insert_list = cls.get_item_insert_update(excel_info_list)
        sdnc_vtep_sp_temp, sdnc_index = cls.update_yaml_item(yaml_input, update_dict)

        insert_gen_list = cls.get_insert_item(insert_list, sdnc_vtep_sp_temp)
        yaml_network = yaml_input['networks']
        yaml_input['networks'] = yaml_network[:sdnc_index + 1] + insert_gen_list + yaml_network[sdnc_index + 1:]

        excel_op_host = kwargs.get('excel_op_host')
        excel_host_list = cls.get_excel_info_list(excel_op_host)
        host_info_dict = cls.list_set_key(excel_host_list, 'hostname')
        network_info_list = cls.get_network_info_list(host_info_dict)
        lcm_ctrl_sp_index = cls.get_lcm_ctrl_sp_index(yaml_input)
        lcm_ipv6_index = cls.get_lcm_ipv6_index(yaml_input, lcm_ctrl_sp_index)
        cls.gen_lcm_ipv6(network_info_list, yaml_input, lcm_ctrl_sp_index, lcm_ipv6_index)

        return yaml_input

    @classmethod
    def gen_lcm_ipv6(cls, network_info_list, yaml_input, lcm_ctrl_sp_index, lcm_ipv6_index):
        if g.cee_ver == 'drop26':
            lcm_ctrl_sp_subnets = yaml_input['networks'][lcm_ctrl_sp_index]['subnets']
            lcm_ipv6_temp = copy.deepcopy(lcm_ctrl_sp_subnets[lcm_ipv6_index])
            gen_lcm_ipv6 = OrderedDict()
            keys = list(lcm_ipv6_temp.keys())
            ip_allocations_index = None
            for key_index in range(len(keys)):
                key = keys[key_index]
                if key == 'ipAllocationPools':
                    ip_allocations_index = key_index + 1
                    break
            keys.insert(ip_allocations_index, 'ipAllocations')

            for key in keys:
                if key == 'ipAllocations':
                    gen_lcm_ipv6[key] = network_info_list
                else:
                    gen_lcm_ipv6[key] = lcm_ipv6_temp[key]
            yaml_input['networks'][lcm_ctrl_sp_index]['subnets'][lcm_ipv6_index] = gen_lcm_ipv6
        elif g.cee_ver == 'drop28':
            yaml_input['networks'][lcm_ctrl_sp_index]['subnets'][lcm_ipv6_index]['ipAllocations'] += network_info_list

    @classmethod
    def get_lcm_ipv6_index(cls, yaml_input, lcm_ctrl_sp_index):
        lcm_ipv6_index = None
        lcm_ctrl_sp_subnets = yaml_input['networks'][lcm_ctrl_sp_index]['subnets']
        for item_index in range(len(lcm_ctrl_sp_subnets)):
            if lcm_ctrl_sp_subnets[item_index]['name'] == 'lcm-ipv6':
                lcm_ipv6_index = item_index
        return lcm_ipv6_index

    @classmethod
    def get_lcm_ctrl_sp_index(cls, yaml_input):
        lcm_ctrl_sp_index = None
        for item_index in range(len(yaml_input['networks'])):
            item = yaml_input['networks'][item_index]
            if item['name'] == 'lcm_ctrl_sp':
                lcm_ctrl_sp_index = item_index
        return lcm_ctrl_sp_index

    @classmethod
    def get_network_info_list(cls, host_info_dict):
        network_info_list = list()
        for name, item in host_info_dict.items():
            if name:
                network_dict = dict()
                network_dict['hostname'] = name
                network_dict['ipAddress'] = item['ipAddr']
                network_info_list.append(network_dict)
        return network_info_list

    @classmethod
    def get_insert_item(cls, insert_list, sdnc_vtep_sp_temp):
        insert_gen_list = list()
        for item in insert_list:
            _temp = copy.deepcopy(sdnc_vtep_sp_temp)
            for key in _temp:
                if key == 'subnets':
                    for subnet_item_index in range(len(_temp[key])):
                        subnet_item = _temp[key][subnet_item_index]
                        for subnets_key in subnet_item:
                            want_v = item.get(subnets_key, None)
                            if subnets_key == 'ipAllocationPools':
                                if want_v and want_v != '-':
                                    _temp[key][subnet_item_index][subnets_key] = [want_v, ]
                            elif subnets_key == 'name':
                                network_name = item.get('network name')
                                if not network_name:
                                    continue
                                deploy = network_name.split('_')[-1]
                                _temp[key][subnet_item_index]['name'] = _temp[key][subnet_item_index][
                                                                            'name'] + '-' + deploy
                            else:
                                if want_v and want_v != '-':
                                    _temp[key][subnet_item_index][subnets_key] = want_v
                elif key == 'taggedVlan':
                    _want_v = item.get(u'tagged vlan\uff08yes/no\uff09', None)
                    if _want_v and _want_v != '-':
                        if _want_v == 'yes':
                            _temp[key] = True
                        elif _want_v == 'no':
                            _temp[key] = False
                else:
                    if key == 'name':
                        want_v = item.get('network name', None)
                    else:
                        want_v = item.get(key, None)
                    if want_v and want_v != '-':
                        _temp[key] = want_v
            insert_gen_list.append(_temp)
        return insert_gen_list

    @classmethod
    def get_item_insert_update(cls, excel_info_list):
        update_dict = dict()
        insert_list = list()
        for item in excel_info_list:
            name = item['network name']
            if not str(name).startswith('sdnc_vtep_sp'):
                update_dict[name] = item
            else:
                insert_list.append(item)
        return update_dict, insert_list

    @classmethod
    def update_yaml_item(cls, yaml_input, update_dict):
        sdnc_vtep_sp_temp = None
        sdnc_vtep_sp_index = None
        network_list = yaml_input['networks']
        for index in range(len(network_list)):
            item = network_list[index]
            name = item['name']
            if name.startswith('sdnc_vtep_sp'):
                sdnc_vtep_sp_index = index
                sdnc_vtep_sp_temp = copy.deepcopy(item)
                continue
            excel_item = update_dict[name]
            for key in item:
                if key == 'subnets':
                    for subnet_item_index in range(len(item[key])):
                        subnet_item = item[key][subnet_item_index]
                        for subnet_item_key in subnet_item:
                            if subnet_item_key == 'vips':
                                _value = item[key][subnet_item_index][subnet_item_key]
                                for _i in range(len(_value)):
                                    vip_dict = _value[_i]
                                    for vip_dict_k in vip_dict:
                                        _want_v = excel_item.get('vip%s %s' % (_i + 1, vip_dict_k), None)
                                        if _want_v and _want_v != '-':
                                            item[key][subnet_item_index][subnet_item_key][_i][vip_dict_k] = _want_v
                            else:
                                _want_v = excel_item.get(subnet_item_key, None)
                                if _want_v and _want_v != '-':
                                    if subnet_item_key == 'ipAllocationPools':
                                        item[key][subnet_item_index][subnet_item_key] = [_want_v, ]
                                    else:
                                        item[key][subnet_item_index][subnet_item_key] = _want_v
                elif key == 'taggedVlan':
                    _want_v = excel_item.get(u'tagged vlan\uff08yes/no\uff09', None)
                    if _want_v and _want_v != '-':
                        if _want_v == 'yes':
                            item[key] = True
                        elif _want_v == 'no':
                            item[key] = False
                else:
                    _want_v = excel_item.get(key, None)
                    if _want_v and _want_v != '-':
                        item[key] = _want_v

        if g.cee_ver == 'drop28':
            sdnc_vtep_sp_temp = OrderedDict(
                name='sdnc_vtep_sp_',
                segmentationId=384,
                taggedVlan=True,
                subnets=[
                    OrderedDict(
                        name='sdnc-vtep-ipv6',
                        cidr='2409: 8086:8617: 180:: / 64',
                        ipAllocationPools=['2409:8086:8617:180::20-2409:8086:8617:180::fffe', ]
                    )
                ]
            )
        return sdnc_vtep_sp_temp, sdnc_vtep_sp_index


class InterfaceGenService(BaseGenService):
    TEMP_CACHE = dict()

    @classmethod
    def run(cls, *args, **kwargs):
        deploy_models = kwargs.get('deploy_models')
        yaml_input = kwargs.get('yaml_input')
        excel_op = kwargs.get('excel_op')
        excel_info_list = cls.get_excel_info_list(excel_op)
        excel_info_dict = cls.list_set_key(excel_info_list, 'network name')

        route_info = cls.get_route_info(excel_info_dict)
        network_scheme_list = yaml_input['networkSchemes']
        interface_assignment_list = yaml_input['interfaceAssignments']

        dpdk_index = cls.get_dpdk_index(network_scheme_list)
        assignment_index = cls.get_assignment_index(interface_assignment_list)
        dpdk_insert_list, assignment_insert_list = cls.get_insert_items(deploy_models, yaml_input, route_info)

        interface_yaml = yaml_input['interfaceAssignments']
        schemes_yaml = yaml_input['networkSchemes']

        yaml_input['interfaceAssignments'] = interface_yaml[
                                             :assignment_index + 1] + assignment_insert_list + interface_yaml[
                                                                                               assignment_index + 1:]
        yaml_input['networkSchemes'] = schemes_yaml[:dpdk_index + 1] + dpdk_insert_list + schemes_yaml[dpdk_index + 1:]

        return yaml_input

    @classmethod
    def get_temp(cls, temp_name, yaml_input):
        cee_ver = g.cee_ver
        cache = cls.TEMP_CACHE.get(temp_name, None)
        if not cache:
            if cee_ver == 'drop26':
                for interface_key in yaml_input:
                    item_list = yaml_input[interface_key]
                    for item in item_list:
                        item_name = item['name']
                        if item_name.startswith(temp_name):
                            return copy.deepcopy(cls.TEMP_CACHE.setdefault(temp_name, item))
            elif cee_ver == 'drop28':
                if temp_name == 'sdnc_vtep_sp_':
                    # temp = {
                    #     'name': 'sdnc_vtep_sp_',
                    #     'interfaceList': [
                    #         {
                    #             'name': 'br_prv',
                    #             'type': 'bridge',
                    #             'firewallZone': 'cee',
                    #             'mtu': 1500,
                    #             'provider': 'ovsdpdk',
                    #             'network': 'sdnc_vtep_sp_'
                    #         }
                    #     ]
                    # }
                    temp = OrderedDict(
                        name='sdnc_vtep_sp_',
                        interfaceList=[
                            OrderedDict(
                                name='br_prv',
                                type='bridge',
                                firewallZone='cee',
                                mtu=1500,
                                provider='ovsdpdk',
                                network='sdnc_vtep_sp_',
                            )
                        ],
                    )
                    return copy.deepcopy(cls.TEMP_CACHE.setdefault(temp_name, temp))
                elif temp_name == 'compute-':
                    # temp = {
                    #     'name':'compute_',
                    #     'networkScheme': [
                    #         'control',
                    #         'storage',
                    #         'compute_storage',
                    #         'ceph_san_sp_1',
                    #         'ceph_san_sp_2',
                    #         'sdnc_sbi_on_control',
                    #         'data_dpdk_compute_tor',
                    #         'int_bridge',
                    #     ],
                    #     'routes': []
                    # }
                    temp = OrderedDict(
                        name='compute_',
                        networkScheme=[
                            'control',
                            'storage',
                            'compute_storage',
                            'ceph_san_sp_1',
                            'ceph_san_sp_2',
                            'sdnc_sbi_on_control',
                            'data_dpdk_compute_tor',
                            'int_bridge',
                        ],
                        routes=list()
                    )
                    return copy.deepcopy(cls.TEMP_CACHE.setdefault(temp_name, temp))
                else:
                    raise Exception()
        return copy.deepcopy(cache)

    @classmethod
    def get_insert_items(cls, deploy_list, yaml_input, route_info):
        cee_ver = g.cee_ver
        scheme_temp_name = 'data_dpdk_compute_tor'
        interface_name = 'vtep'
        # assignment_temp_name = 'compute'
        if cee_ver == 'drop28':
            scheme_temp_name = 'sdnc_vtep_sp_'
            interface_name = 'br_prv'
        dpdk_insert_list = list()
        assignment_insert_list = list()
        for deploy in deploy_list:
            scheme_temp = cls.get_temp(scheme_temp_name, yaml_input)
            for interface in scheme_temp['interfaceList']:
                if interface['name'] == interface_name:
                    interface['network'] = 'sdnc_vtep_sp_' + deploy
            if cee_ver == 'drop28':
                scheme_temp['name'] = 'sdnc_vtep_sp_' + deploy
            else:
                scheme_temp['name'] = 'data_dpdk_compute_' + deploy

            dpdk_insert_list.append(scheme_temp)
            assignment_temp = cls.get_temp('compute-', yaml_input)
            if cee_ver == 'drop26':
                for _network_scheme_index in range(len(assignment_temp['networkScheme'])):
                    if assignment_temp['networkScheme'][_network_scheme_index].startswith('data_dpdk_compute_'):
                        assignment_temp['networkScheme'][_network_scheme_index] = assignment_temp['networkScheme'][
                                                                                      _network_scheme_index] + deploy
            elif cee_ver == 'drop28':
                assignment_temp['networkScheme'].append('sdnc_vtep_sp_%s' % deploy)
            assignment_temp['name'] = 'compute_%s' % deploy
            assignment_temp['routes'] = route_info[deploy]
            assignment_insert_list.append(assignment_temp)
        return dpdk_insert_list, assignment_insert_list

    @classmethod
    def get_assignment_index(cls, interface_assignment_list):
        assignment_index = None
        for interface_assignment_index in range(len(interface_assignment_list)):
            interface_assignment = interface_assignment_list[interface_assignment_index]
            name = interface_assignment['name']
            if name.startswith('compute-tor'):
                assignment_index = interface_assignment_index
        return assignment_index

    @classmethod
    def get_dpdk_index(cls, network_scheme_list):
        dpdk_index = None
        # for network_scheme in network_scheme_list:
        for network_scheme_index in range(len(network_scheme_list)):
            network_scheme = network_scheme_list[network_scheme_index]
            name = network_scheme['name']
            if name.startswith('data_dpdk_compute_tor'):
                dpdk_index = network_scheme_index
        return dpdk_index

    @classmethod
    def get_route_info(cls, excel_info_dict):
        res_dict = dict()
        for name, item in excel_info_dict.items():
            if name.startswith('sdnc_vtep_sp'):
                route_list = list()
                deploy = name.split('_')[-1]
                destination1 = item['destination1']
                destination2 = item['destination2']
                nexthop1 = item['nexthop1']
                nexthop2 = item['nexthop2']
                if (destination1 and destination1 != '-') and (nexthop1 and nexthop1 != '-'):
                    route_item = dict(destination=destination1, nexthop=nexthop1)
                    route_list.append(route_item)

                if (destination2 and destination2 != '-') and (nexthop2 and nexthop2 != '-'):
                    route_item = dict(destination=destination2, nexthop=nexthop2)
                    route_list.append(route_item)
                res_dict[deploy] = route_list

        return res_dict

#
# if __name__ == '__main__':
#     import pprint
#
#     excel_op_host = ExcelOp(file='gz_server.xlsx', sheet='hosts')
#     excel_op_network = ExcelOp(file='gz_server.xlsx', sheet='networks')
#     # pprint.pprint(BaseGenService.get_excel_info_list(excel_op_host))
#     want_dict = dict()
#     p = re.compile(r'[\u4e00-\u9fa5]')
#     result = list()
#     print(excel_op_host.get_col_value(16))
#     models = list()
#     for i in excel_op_host.get_col_value(16)[1:]:
#         if i is not None:
#             models.append(i)
#     models = set(models)
#     for i in models:
#         _ = p.split(i)
#         _site = _[0].lower()
#         _num = int(_[-1])
#         _l = want_dict.setdefault(_site, list())
#         _l.append(_num)
#     sites = sorted(want_dict.keys())
#     for site in sites:
#         nums = sorted(want_dict[site])
#         for num in nums:
#             result.append('%s%s' % (site, num))
#
#     print(result)
