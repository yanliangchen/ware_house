from backend.myException.myExecption import MyParamCheckError
from flask import request
from backend.customer.paramCheck import ParamCheckBase
import re
from backend.myException.myExecption import MyKeyError
from backend.myBluePrint.ericic.baseDao.datacenterApiDao import datacenterApiDao


class DataCenterCheck(ParamCheckBase):

    def post(self, *args, **kwargs):
        body = request.get_json()
        name = body.get('name', None)
        db_name = datacenterApiDao.select_name_dc(name)

        if name is None:
            raise MyParamCheckError('The name fields must be passed')
        elif len(name.strip()) == 0:
            raise MyParamCheckError('The name field is not allowed to be empty')
        elif name == db_name:
            raise MyParamCheckError('The name field is unique and has been repeated')
        elif len(name) > 50:
            raise MyParamCheckError('The name field is too long')

        compile_ip = re.compile(
            '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        compile_ipv6 = re.compile(r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,6}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,6}(:[0-9a-f]{1,4}){1,1}\Z)|'
                                  r'(\A(([0-9a-f]{1,4}:){1,7}|:):\Z)|(\A:(:[0-9a-f]{1,4})'
                                  r'{1,7}\Z)|(\A((([0-9a-f]{1,4}:){6})(25[0-5]|2[0-4]\d|[0-1]'
                                  r'?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
                                  r'(\A(([0-9a-f]{1,4}:){5}[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|'
                                  r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){5}:[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|'
                                  r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
                                  r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,4}:(25[0-5]|'
                                  r'2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d))'
                                  r'{3}\Z)|(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,3}:'
                                  r'(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?'
                                  r'\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4})'
                                  r'{1,2}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|'
                                  r'[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]'
                                  r'{1,4}){1,1}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|'
                                  r'2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A(([0-9a-f]{1,4}:){1,5}|:):'
                                  r'(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?'
                                  r'\d?\d)){3}\Z)|(\A:(:[0-9a-f]{1,4}){1,5}:(25[0-5]|2[0-4]\d|'
                                  r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)')
        dc_mode = body.get('mode', True)
        cee_lists = ['drop26', 'drop28', 'drop30', 'drop33', 'drop35', 'drop37']
        # online  1
        if dc_mode == 1:
            try:
                lcm_ip = body['lcm_ip']
                lcm_user = body['lcm_user']
                lcm_pwd = body['lcm_pwd']
                lcmrc_dir = body['lcmrc_dir']
                system_name = body['system_name']
                cee_version = body['cee_version']
                openstackrc_dir = body['openstackrc_dir']
            except KeyError as  key:
                raise MyKeyError(key)
            if not compile_ip.match(lcm_ip)  and  not compile_ipv6.match(lcm_ip) :
                raise MyParamCheckError('The IP field is not formatted correctly')
            elif len(lcm_ip) > 128:
                raise MyParamCheckError('The ip field is too long')

            if lcm_user == None:
                raise MyParamCheckError('The lcm_user field is not allowed to be empty ')
            elif len(lcm_user) > 20:
                raise MyParamCheckError('The lcm_user field is too long')

            if lcm_pwd == None:
                raise MyParamCheckError('The lcm_pwd field is not allowed to be empty ')
            elif len(lcm_pwd) > 20:
                raise MyParamCheckError('The lcm_pwd field is too long')

            if openstackrc_dir == None:
                raise MyParamCheckError('The openstackrc_dir field is not allowed to be empty ')
            elif len(openstackrc_dir) > 100:
                raise MyParamCheckError('The openstackrc_dir field is too long')

            if lcmrc_dir == None:
                raise MyParamCheckError('The lcmrc_dir field is not allowed to be empty ')
            elif len(lcmrc_dir) > 100:
                raise MyParamCheckError('The lcmrc_dir field is too long')

            if system_name == None:
                raise MyParamCheckError('The system_name field is not allowed to be empty')
            elif len(system_name) > 50:
                raise MyParamCheckError('The system_name field is too long')

            if cee_version == None:
                raise MyParamCheckError('The cee_version field is not allowed to be empty')
            if cee_version.lower().strip() not in cee_lists:
                raise MyParamCheckError('The specified cee_version does not currently exist')
            elif len(cee_version) > 50:
                raise MyParamCheckError('The  cee_version field is too long')
        # offline  0
        if dc_mode == 0:
            try:
                system_name = body['system_name']
                cee_version = body['cee_version']
            except KeyError as  key:
                raise MyKeyError(key)

            if system_name == None:
                raise MyParamCheckError('The system_name field is not allowed to be empty')
            elif len(system_name) > 50:
                raise MyParamCheckError('The  system_name field is too long')

            if cee_version == None:
                raise MyParamCheckError('The cee_version field is not allowed to be empty')
            elif len(cee_version) > 50:
                raise MyParamCheckError('The  cee_version field is too long')
            if cee_version.lower().strip() not in cee_lists:
                raise MyParamCheckError('The specified CEE version does not currently exist')

    def put(self, *args, **kwargs):
        body = request.get_json()
        try:
            name = body['name']
            mode = body['mode']
        except KeyError as key:
            raise MyKeyError(key)
        if len(name) > 50:
            raise MyParamCheckError('The name field is too long')

        dc_mode = body.get('mode', 1)
        lcm_ip = body.get('lcm_ip')
        compile_ip = re.compile(
            '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        lcm_user = body.get('lcm_user')
        lcm_pwd = body.get('lcm_pwd')
        openstackrc_dir = body.get('openstackrc_dir')
        lcmrc_dir = body.get('lcmrc_dir')
        system_name = body.get('system_name')
        cee_version = body.get('cee_version')
        cee_lists = ['drop26', 'drop28', 'drop30', 'drop33', 'drop35', 'drop37']
        # online  1
        if dc_mode == 1:
            if lcm_ip == None:
                raise MyParamCheckError('The lcm_ip field is not allowed to be empty ')
            elif not compile_ip.match(lcm_ip):
                raise MyParamCheckError('The IP field is not formatted correctly')
            elif len(lcm_ip) > 16:
                raise MyParamCheckError('The ip field is too long')

            if lcm_user == None:
                raise MyParamCheckError('The lcm_user field is not allowed to be empty ')
            elif len(lcm_user) > 20:
                raise MyParamCheckError('The lcm_user field is too long')

            if lcm_pwd == None:
                raise MyParamCheckError('The lcm_pwd field is not allowed to be empty ')
            elif len(lcm_pwd) > 20:
                raise MyParamCheckError('The lcm_pwd field is too long')

            if openstackrc_dir == None:
                raise MyParamCheckError('The openstackrc_dir field is not allowed to be empty ')
            elif len(openstackrc_dir) > 100:
                raise MyParamCheckError('The openstackrc_dir field is too long')

            if lcmrc_dir == None:
                raise MyParamCheckError('The lcmrc_dir field is not allowed to be empty ')
            elif len(lcmrc_dir) > 100:
                raise MyParamCheckError('The lcmrc_dir field is too long')

            if system_name == None:
                raise MyParamCheckError('The system_name field is not allowed to be empty')
            elif len(system_name) > 50:
                raise MyParamCheckError('The system_name field is too long')

            if cee_version == None:
                raise MyParamCheckError('The cee_version field is not allowed to be empty')
            if cee_version.lower().strip() not in cee_lists:
                raise MyParamCheckError('The specified cee_version does not currently exist')
            elif len(cee_version) > 50:
                raise MyParamCheckError('The  cee_version field is too long')
        # offline  0
        if dc_mode == 0:
            if system_name == None:
                raise MyParamCheckError('The system_name field is not allowed to be empty')
            elif len(system_name) > 50:
                raise MyParamCheckError('The  system_name field is too long')

            if cee_version == None:
                raise MyParamCheckError('The cee_version field is not allowed to be empty')
            elif len(cee_version) > 50:
                raise MyParamCheckError('The  cee_version field is too long')
            if cee_version.lower().strip() not in cee_lists:
                raise MyParamCheckError('The specified CEE version does not currently exist')
