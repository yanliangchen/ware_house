一、软件依赖

a)    Python 3.6

b)   Mysql  5.7.30

​          i.      如果不在同一台主机需要修改 bind

​         ii.      需要添加 用户名密码认证

c)    Redis 3.0.6

​          i.      如果不在同一台主机需要修改 bind

​         ii.      需要添加 密码 校验

d)   Nginx 1.10.3

​          i.      配置文件的目录为：/etc/nginx/conf.d/optimus.conf

​         ii.      需要修改的项目为：

\1.    前端： 修改前端项目路径

\2.    后端： 修改后端路由ip port

e)    Gunicorn  20.0.4

 

二、python环境依赖（建议使用virtualenv安装环境依赖）

Package   Version

------------ ---------

bcrypt    3.1.7

certifi   2020.6.20

cffi     1.14.2

chardet   3.0.4

click    7.1.2

cryptography 3.0

et-xmlfile  1.0.1

Flask    1.1.2

Flask-Cors  3.0.8

gunicorn   20.0.4

idna     2.10

itsdangerous 1.1.0

jdcal    1.4.1

Jinja2    2.11.2

MarkupSafe  1.1.1

openpyxl   2.6.4

paramiko   2.7.1

pip     20.2.2

pycparser  2.20

PyMySQL   0.10.0

PyNaCl    1.4.0

pytz     2020.1

PyYAML    5.3.1

redis    3.5.3

requests   2.24.0

setuptools  49.6.0

six     1.15.0

SQLAlchemy  1.3.19

urllib3   1.25.10

Werkzeug   1.0.1

wheel    0.35.1

 

三、项目启动命令：

a)    cd 到 optimus 后端所在文件夹

b)   执行gunicorn --workers=4 main:app -b 0.0.0.0:8000 &