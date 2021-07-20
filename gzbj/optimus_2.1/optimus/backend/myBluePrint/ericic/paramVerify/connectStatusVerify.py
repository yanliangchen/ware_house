import re
from flask import request
from backend.customer.paramCheck import ParamCheckBase
from backend.myException.myExecption import MyKeyError, MyParamCheckError


class ConnStatusVerify(ParamCheckBase):

    # def get(self, *args, **kwargs):
    #     print('xxxx')

    def post(self, *args, **kwargs):
        body = request.get_json()
        try:
            lcm_ip = body['lcm_ip']
            lcm_user = body['lcm_user']
            lcm_pwd = body['lcm_pwd']
        except KeyError as e:
            raise MyKeyError(e)
        # pattern = '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        # if not re.match(pattern, lcm_ip) :
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
        if not compile_ip.match(lcm_ip) and not compile_ipv6.match(lcm_ip):
            raise MyParamCheckError("lcm_ip format needs to be ip's format")

