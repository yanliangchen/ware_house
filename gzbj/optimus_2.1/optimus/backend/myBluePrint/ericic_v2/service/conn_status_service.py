# import socket
import traceback
from functools import wraps
from config import REDIS_CONNECT_CACHE
from backend.common.loghandler import RedisLog
from backend.common.redisHandler import CACHE_RDS
from backend.common.scriptHandler import ScriptHandler
from backend.myException.myExecption import MyParamCheckError, MySSHError
# from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel


class ConnCache:

    @staticmethod
    def status_cache(func):
        @wraps(func)
        def inner(*args, **kwargs):
            _cls, lcm_ip, lcm_user, lcm_pwd = args
            key = '%s-%s-%s' % (lcm_ip, lcm_user, lcm_pwd)
            try:
                RedisLog.info('get status from cache -- key : %s' % key)
                res_dict = CACHE_RDS.hgetall(key)
                if not res_dict:
                    RedisLog.info('failed to get status from cache -- key : %s' % key)
                    res_dict = func(*args, **kwargs)
                    try:
                        p = CACHE_RDS.pipeline()
                        p.hmset(key, res_dict)
                        p.expire(key, REDIS_CONNECT_CACHE)
                        p.execute()
                        RedisLog.info('set  status into cache -- key : %s' % key)
                    except Exception:
                        e = traceback.format_exc()
                        RedisLog.error(e)
                status = True if res_dict['status'] == 'true' else False
                return dict(status=status, msg=res_dict['msg'])
            finally:
                CACHE_RDS.close()

        return inner


class ConnStatusService:

    @classmethod
    def check_by_cid(cls, cid):
        dc_obj = DataCenterModel.get_one_by_id(cid)
        if dc_obj:
            mode = dc_obj.mode
            if mode:
                lcm_ip = dc_obj.lcm_ip
                lcm_user = dc_obj.lcm_user
                lcm_pwd = dc_obj.lcm_pwd
                res = cls.check_by_ip(lcm_ip, lcm_user, lcm_pwd)
            else:
                raise MyParamCheckError('wrong data center mode')
        else:
            raise MyParamCheckError('wrong data center id')
        return res

    @classmethod
    @ConnCache.status_cache
    def check_by_ip(cls, lcm_ip, lcm_user, lcm_pwd):
        try:
            ScriptHandler(lcm_ip, lcm_user, lcm_pwd)
            status = 'true'
            msg = 'success'
        except MySSHError as e:
            msg = e.msg
            status = 'false'
        return dict(status=status, msg=msg)
