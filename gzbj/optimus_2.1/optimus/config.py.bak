#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : config.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/1/21 14:22
# @Desc  :
# import configparser
#
# config = configparser.ConfigParser()
# config.read('setting.ini')

# print(config['scheduler']['max_instances'])
# mysql
# MYSQL_HOST = config['mysql']['host']
# MYSQL_HOST = config['mysql']['host']
# MYSQL_DB = config['mysql']['dbname']
# MYSQL_NAME = config['mysql']['uname']
# MYSQL_PASS = config['mysql']['upass']
# MYSQL_HOST = '100.98.97.86'
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DB = 'optimus'
MYSQL_NAME = 'root'
# MYSQL_PASS = '123shiwodemima'
MYSQL_PASS = 'optimus'
RETRY_TIME = 3

# redis
# REDIS_HOST = config['redis']['host']
# REDIS_PORT = config['redis']['port']
# REDIS_PASS = config['redis']['upass']
# REDIS_HOST = '100.98.97.86'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
# REDIS_PASS = '123shiwodemima'
REDIS_PASS = 'optimus'
REDIS_CONNECT_CACHE = 60 * 10

# authentication
ACCESS_TIME = 60 * 10
ACCESS_SALT = 'SXTxg6O'
REFRESH_TIME = 60 * 60 * 24 * 3
REFRESH_SALT = 'gkLZcFCi'
# REFRESH_BASE = 'sqlite'
REFRESH_BASE = 'redis'

# scripts
SSH_TIMEOUT = 5

# celery
# # BROKER_URL = 'amqp://root:optimus@100.98.97.86:5672/db_refresh'
# BROKER_URL = 'amqp://root:optimus@100.98.97.86:5672/db_refresh'
# # CELERY_RESULT_BACKEND = 'redis://100.98.97.86:6379/15'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/15'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

# mongo
MONGO_DBNAME = 'optimus'
# MONGO_HOST = '100.98.97.83'
MONGO_HOST = 'localhost'
MONGO_NAME = 'root'
MONGO_PASS = 'optimus'
MONGO_PORT = 27017
MONGO_TIMEOUT = 2000  # ms

#
# if __name__ == '__main__':
#     import base64
#     path = 'FilesFolder/yaml_gen/472966182a1c422380fc2300d8c41428.zip'
#     with open(path, 'rb') as f:
#         content = f.read()
#     a = base64.b64encode(content).decode('utf-8')
#     print(a)
#     path2 = 'FilesFolder/yaml_gen/test.zip'
#     with open(path2, 'wb') as f2:
#         f2.write(base64.b64decode(a))
