# Optimus api 文档

此文档主要用来介绍Optimus接口功能以及调用方式，有任何文档意外的问题，欢迎联系[gaofeng.a.zhang](gaofeng.a.zhang@ericsson.com)

## 一、系统模块

### API login

- 使用说明: 此api用于用户的登录，通过返回access_token的方式来控制用户权限

- url: `{host}:{port}/api/v1/login`

#### method: post

- parameter: `{host}:{port}/api/v1/login`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| name | False |True | 用户 name |
| password | False |  True|用户密码 |


- request body: 
```json5
{
    "name": "name",
    "password": "password"
}
```

- response: 
```json5
{
    "status": true,
    "data": {
        "access_token": "token",
        "expires_in": 123213, // access_token 的有效时间
        "refresh_token": "refresh_token",
        "time": 123123123, // refresh_token 的有效时间
    },
    "code": 200,
}
```

---

### API refresh

- 使用说明: 此api用于刷新过期的access_token

- url: `{host}:{port}/api/v1/refresh`

- authentication: False

#### method: post

- parameter: `{host}:{port}/api/v1/refresh`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| refresh_token | False |  True|refresh_token|



- request body: 
```json5
{
    "refresh_token": "refresh_token",
}
```

- response: 
```json5
{
    "status": true,
    "data": {
        "access_token": "access_token",
        "expires_in": 11111,
    },
    "code": 200,
}
```

---

### API sign

- 使用说明: 用于注册用户，用户名不区分大小写。用户校验方式为， 在header中设置Authorization字段

- url: `{host}:{port}/api/v1/sign`

#### method: post

- parameter: `{host}:{port}/api/v1/sign`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| name | False |True|用户name|
| password | False |  True|用户密码|


- request body: 
```json5
{
    "name": "name",
    "password": "password"
}
```

- response: 
```json5
{
    "status": true,
    "data": [],
    "code": 201,
}
```

---

### API logout

- 使用说明: 用于注册用户，用户名不区分大小写。用户校验方式为， 在header中设置Authorization字段

- url: `{host}:{port}/api/v1/logout`

#### method: post

- parameter: `{host}:{port}/api/v1/logout`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |



- request body: 
```json5
{
    "refresh_token": "refresh_token"
}
```

- response: 
```json5
{
    "status": true,
    "code": 200,
}
```



---

## 二、YamlGenerator 模块


#### yaml config 生成

- 使用说明: 通过上传文件来生成yaml文件，至少上传一个yaml模板文件和一个excel文件，yaml模板为[hosts.yaml, networks.yaml, host_profile.yaml, interface_assignment.yaml]之中一个或者多个。此功能为同步功能，执行成功后会返回success以及此次作业的id

- authentication: True

- url: `{host}:{port}/api/v1/config/yaml_gen`

- method: post

- parameter: `{host}:{port}/api/v1/config/yaml_gen?site={site}&cee_ver={cee_ver}&pjt_name={project_name}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|site|False|True| 可选范围 GZ or ZZ|
|cee_ver|False|True| 可选范围 drop 22, 25, 26, 28, 35|
|pjt_name|False|True| 作业名称|



- request body: (form-data)

| key | value | description |
| :-----   | ----:|:----:|
|excel|demo.xlsx| 上传的excel输入（字段类型为File）|
|yaml|hosts.yaml| 批量上传的yaml文件列表（字段类型为File）|


- response: 
```json5
{
    "status": true,
    "data": {
        "id": "job_id"
    },
    "code": 201,
}
```

---


#### 作业历史记录

- 使用说明: 

- authentication: True

- url: `{host}:{port}/api/v1/config/yaml_gen/history`

- method: get

- parameter: `{host}:{port}/api/v1/config/yaml_gen/history`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |



- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "data": [
        {
            "id": "uuid",
            "project_name": "project_name",
            "cee_version": "cee_version",
            "timestamp": "runtime",
            "task_status": "success", //success failed running
        }
    ],
    "code": 201,
}
```

---

#### 历史记录删除

- 使用说明: 通过id list 删除任务

- authentication: True

- url: `{host}:{port}/api/v1/config/yaml_gen/history`

- method: delete

- parameter: `{host}:{port}/api/v1/config/yaml_gen/history`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|id|False|True|任务执行id|



- request body: 
```json5
{
    "id": [
        "id1",
    ]
}
```

- response: 
```json5
{
    "status": true,
    "code":200,
}
```

---

#### 任务结果下载

- 使用说明: 通过id下载任务执行结果，以base64的格式返回

- authentication: True

- url: `{host}:{port}/api/v1/config/yaml_gen/result?id={id}`

- method: get

- parameter: `{host}:{port}/api/v1/config/yaml_gen/history`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|id|False|True|任务执行id|



- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "data":  "Base64 content",
    "code": 200
}
```

---

## 三、 Ericic模块

### API DataCenter

- 使用说明: 此api用于data_center功能的增删改查

- authentication: True

- url: `{host}:{port}/api/ericic/v1/data_center`

#### method: get

##### case1：通过id获取指定的data_center信息

- parameter: `{host}:{port}/api/ericic/v1/data_center?id={id}`

| 参数名称 | multi | 必填 |   description    |
| :------- | ----: | ---: | :--------------: |
| id       | False | True | data_center 的id |


- request body: 

```json5
{}
```

- response: 

```json5
{
    "status": true,
    "data": {
        "cee_version": "cee_version",
        "city": "city",
        "country": "abc",
        "id": "id",
        "lcm_ip": "lcm_ip",
        "lcm_pwd": "lcm_pwd",
        "lcm_user": "lcm_user",
        "lcmrc_dir": "lcmrc_dir ",
        "mode": "mode",
        "name": "name",
        "openstackrc_dir":"openstackrc_dir",
        "province": "province",
        "system_name": "system_name"
    },
    "code": 200
}
```

##### case2：通过data_center全量信息

- request body: 

```json5
{}
```

- response: 

```json5
{
	"code": 200,
	"data": [
		{
			"cee_version": "cee_version",
			"city": "city",
			"country": "country",
			"id": "id",
			"lcm_ip": "lcm_ip",
			"lcm_pwd": "lcm_pwd",
			"lcm_user": "lcm_user",
			"lcmrc_dir": "lcmrc_dir",
			"mode": "mode",
			"name": "name",
			"openstackrc_dir":"openstackrc_dir",
			"province": "province",
			"system_name": "system_name"
		}
	],
	"status": true,
	"total": 200 //数据总量
}
```

#### method: post

##### case1: 添加offline 的 data_center

- parameter: `{host}:{port}/api/ericic/v1/data_center`

| 参数名称 | multi |  必填 |                   description                   |
| :------- | ----: | ----: | :---------------------------------------------:|
| id       | False |  True |                 data_center  id                |
| mode     | False | False | mode =True为online模式,mode=False为offline模式. |


- request body: 

```json5
{
	"name": "name",
	"mode": false,
	"country": "country",
	"province": "province",
	"city": "city",
    "cee_version": "cee_version",
}
```

- response: 

```json5
{
    "status": true,
    "data": "id",
    "message": "message",
    "code": 200
}
```

##### case2: 添加online 的 data_center，添加同时也会将mode为online的data_center设置定时任务，然后再response中分别显示静态任务和动态任务最近一次的运行时间


- request body: 

```json5
{
	"name": "name",
	"mode": true,
	"country": "country",
	"province": "province",
	"city": "city",
	"system_name": "system_name",
    "cee_version": "cee_version",
	"lcm_ip": "lcm_ip",
	"lcm_user": "lcm_user",
	"lcm_pwd": "lcm_pwd",
	"openstackrc_dir": "openstackrc_dir",
	"lcmrc_dir": "lcmrc_dir ",
}
```

- response: 

```json5
{
    "status": true,
    "data": "id",
    "static_job": 1111111, // 静态任务下次执行的时间， 如果定时任务添加失败则为None
    "dynamic_job": 1111111, // 动态任务下次执行的时间， 如果定时任务添加失败则为None
    "message": "message",
    "code": 200
}
```

#### method: delete

##### case: 通过id删除data_center，同时也会将指定DC对应的动静态任务从定时任务模块中删除

- parameter: `{host}:{port}/api/ericic/v1/data_center`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 

```json5
{
    "id": "id",
}
```

- response: 

```json5
{
    "status": true,
    "data": "id",
    "message": "message",
    "code": 200
}
```

#### method: put

##### case1: 通过id 更新 online data_center， mode&name字段为不可编辑字段

- parameter: `{host}:{port}/api/ericic/v1/data_center`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 

```json5
{
    "id": "id",
    "country": "country",
    "province": "province",
    "city": "city",
    "system_name": "system_name",
    "cee_version":"cee_version",
    "lcm_ip": "lcm_ip",
    "lcm_user": "lcm_user",
    "lcm_pwd": "lcm_pwd",
    "openstackrc_dir": "openstackrc_dir",
    "lcmrc_dir": "lcmrc_dir",
}
```

- response: 

```json5
{
    "status": true,
    "message":"message",
    "code": 200
}
```
 
 
##### case2: 通过id 更新 offline data_center

- parameter: `{host}:{port}/api/ericic/v1/data_center`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 

```json5
{
    "id": "id",
    "country": "country",
    "province": "province",
    "city": "city",
    "cee_version":"cee_version",
}
```

- response: 

```json5
{
    "status": true,
    "message":"message",
    "code": 200
}
```
 
 ---
 
### API record

- 使用说明: 此api用户record的添加和record的分页查询

- authentication: True

- url: `{host}:{port}/api/ericic/v1/record`

#### method: get

##### case1：批量获取record信息 

- parameter: `{host}:{port}/api/ericic/v1/record?sort={sort}&order=desc&limit={limit}&offset={offset}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|sort | False |  False  | 排序所依据的字段，取值范围为[], 默认为系统字段timestamp|
|order | False |  False  | 升序或者降序，取值范围为[asc, desc], 默认为desc|
|limit | False |  False  | 分页查询，单页展示数据量， 默认为50|
|offset | False |  False  | 分页查询偏移量， 默认为0|

- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "total": 1000,
    "data": [
        {
            "id": "id",
            "name": "name",
            "data_center": "data_center",
            "cee_version": "cee_version",
            "host": "data_center",
        },
    ],
    "code": 200
}
```
#### method: post

##### case1：新增record 

- parameter: `{host}:{port}/api/ericic/v1/record`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{
    "name": "name",
    "data_center": "data_center",
    "cee_version": "cee_version",
    "host": "data_center",
}
```

- response: 
```json5
{
    "status": true,
    "data": "id",
    "code": 201
}
```

 #### method: delete

##### case1：通过id删除record

- parameter: `{host}:{port}/api/ericic/v1/record`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{
    "id": "id"
}
```

- response: 
```json5
{
    "status": true,
    "code": 200
}
```
 
 ---
 
 
### API infrastructure

- 使用说明: 此api用于查询指定dc下，cpu memory disk 的使用情况汇总，以及nova service 和 volume 信息的汇总

- authentication: True

- url: `{host}:{port}/api/ericic/v1/infrastructure`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/infrastructure?cid={cid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | data center 的 id|

- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "data": {
        "host_info": {
            "down": 0,
            "total": 0,
            "up": 0
        },
        "tenant_info": [
            {
                "core_used": 0,
                "id": "tenant_id",
                "name": "tenant_name",
                "ram_used": 0
            },
        ],
        "total_memory": 0,
        "total_storage": 0,
        "total_vcpus": 0,
        "used_memory": 0,
        "used_storage": 0,
        "used_vcpus": 0,
        "volume_info": [
            {
                "id": "volume_id",
                "name": "volume_name",
            }
        ]
    },
    "code": 200
}
```
 
---

### API infra_resource

- 使用说明: 此api用于查询指定dc下，cpu memory disk 的使用情况汇总，以及nova service 和 volume 信息的汇总

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/infra_resource/{hid}`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/{cid}/infra_resource/{hid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | data center 的 id|
|hid | False |  True  | 指定nova service 的 id|

- request body: 
```json5
{}
```

- response: 
```json5
{
    "code": 200,
    "data": {
        "total_cpu": 56,
        "total_ram": 385401,
        "total_rom": 811,
        "used_cpu": 24,
        "used_ram": 45568,
        "used_rom": 0
    },
    "status": true
}
```
 
 ---
 
### API cpu_layout

- 使用说明: 此api用于获取指定host的cpu layout信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/cpu_layout/{hid}`

#### method: get


 parameter: `{host}:{port}/api/ericic/v1/{cid}/cpu_layout/{hid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | 目标data center的id |
|hid | False |  True  | 目标host的id |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "data": {
        "socket_info": {
            "core 0": {"socket 0": [0, 48], "socket 1": [1, 49],},
            "core 1": {"socket 0": [0, 48], "socket 1": [1, 49],},
        },
        "instance_info": [
            {
                "vcpu": [4, 52, 5, 53],
                "vm": "vm_a_01",
                "instance": "instance-0000a",
            }
        ]
    },
    "code": 200
}
```
 
 ---

### API interface_driver

- 使用说明: 此api用于获取指定host的interface_drivert信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/interface_driver/{hid}`

#### method: get


 parameter: `{host}:{port}/api/ericic/v1/{cid}/interface_driver/{hid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | 目标data center的id |
|hid | False |  True  | 目标host的id |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "code": 200,
    "data": {
        "firmware": {
            "control0": {
                "desc": "Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)",
                "driver": "i40e",
                "driver_info": "2.8.20-k",
                "firmware_version": "6.01 0x80003d3b 1.1862.0",
                "interface": "control0",
                "mac": "6c:92:bf:f6:8f:54",
                "pci_number": "0000:3b:00.0"
            },
            "control1": {
                "desc": "Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)",
                "driver": "i40e",
                "driver_info": "2.8.20-k",
                "firmware_version": "6.01 0x80003d3b 1.1862.0",
                "interface": "control1",
                "mac": "6c:92:bf:f6:8f:54",
                "pci_number": "0000:b0:00.1"
            },
            "storage0": {
                "desc": "Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)",
                "driver": "i40e",
                "driver_info": "2.8.20-k",
                "firmware_version": "6.01 0x80003d3b 1.1862.0",
                "interface": "storage0",
                "mac": "b4:05:5d:1a:02:fd",
                "pci_number": "0000:af:00.1"
            },
            "storage1": {
                "desc": "Ethernet controller: Intel Corporation Ethernet Controller X710 for 10GbE SFP+ (rev 02)",
                "driver": "i40e",
                "driver_info": "2.8.20-k",
                "firmware_version": "6.01 0x80003d3b 1.1862.0",
                "interface": "storage1",
                "mac": "b4:05:5d:1a:02:fd",
                "pci_number": "0000:b0:00.0"
            }
        },
        "static": {
            "control0": {
                "interface": "control0",
                "mac": "6c:92:bf:f6:8f:54",
                "pci_number": "0000:3b:00.0",
                "rx_dropped": 0,
                "rx_errors": 0,
                "tx_dropped": 0,
                "tx_errors": 0,
                "tx_packets": 176395534
            },
            "control1": {
                "interface": "control1",
                "mac": "6c:92:bf:f6:8f:54",
                "pci_number": "0000:b0:00.1",
                "rx_dropped": 0,
                "rx_errors": 0,
                "tx_dropped": 0,
                "tx_errors": 0,
                "tx_packets": 0
            },
            "storage0": {
                "interface": "storage0",
                "mac": "b4:05:5d:1a:02:fd",
                "pci_number": "0000:af:00.1",
                "rx_dropped": 0,
                "rx_errors": 0,
                "tx_dropped": 0,
                "tx_errors": 0,
                "tx_packets": 192519
            },
            "storage1": {
                "interface": "storage1",
                "mac": "b4:05:5d:1a:02:fd",
                "pci_number": "0000:b0:00.0",
                "rx_dropped": 0,
                "rx_errors": 0,
                "tx_dropped": 0,
                "tx_errors": 0,
                "tx_packets": 192513
            }
        }
    },
    "status": true
}
```
 
 ---

### API network_port

- 使用说明: 此api用于获取指定vm的network_port信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/{vid}/network_port`

#### method: get


 parameter: `{host}:{port}/api/ericic/v1/{cid}/{vid}/network_port`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | 目标data center的id |
|vid | False |  True  | 目标vm的id |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "code": 200,
    "data": [
        {
            "id": "767b85ad-b6ea-4b34-8a28-ed63940f76ec",
            "ip_address": "128.3.0.4",
            "mac": "02:00:00:01:02:01",
            "name": "vSMF205-1_vsfo-cp-3_BP",
            "rx_dropped": "3", //因为返回值有 ? 的形式 所以字段以str进行返回
            "rx_errors": "?",
            "rx_packets": "6",
            "tx_dropped": "3",
            "tx_errors": "?",
            "tx_packets": "6",
            "vhostuser": "vhu767b85ad-b6",
            "vif_type": "vhostuser"
        },
    ],
    "status": true
}
```
 
 ---

### API tenant_quota

- 使用说明: 此api用于获取指定tenant的quota信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/{tid}/tenant_quota`

#### method: get


 parameter: `{host}:{port}/api/ericic/v1/{cid}/{tid}/tenant_quota`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | 目标data center的id |
|tid | False |  True  | 目标tenant的id |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "code": 200,
    "data": {
        "cores": {
            "in_use": 0,
            "limit": 20,
            "total": 20,
            "other": 20,
            "availability": 20,
        },
        "ram": {
            "in_use": 0,
            "limit": 20,
            "total": 20,
            "other": 20,
            "availability": 20,
        },
        "volume": { // 当有多个volume 信息时， 会存在多个key， default 信息一定存在
            "default": {
                "in_use": 0,
                "limit": 1000
            },
            "pool_1": {
                "in_use": 0,
                "limit": 10
            },
        }
    },
    "status": true
}
```
 
 ---

### API nova_service

- 使用说明: 此api用于获取指定dc下 state 为 up / down 的host 信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/{cid}/nova_service/{state}`

#### method: get


 parameter: `{host}:{port}/api/ericic/v1/{cid}/nova_service/{state}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | 目标data center的id |
|state | False |  True  | 取值为 up 或者 down |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "code": 200,
    "data": [
        {
            "availability_zone": "vepc_cp",
            "cid": "gaofzhan_test",
            "host": "compute4.bjitte.ericsson.se",
            "id": "100",
            "state": "up",
            "status": "enabled"
        },
    ],
    "status": true
}
```
  
 ---
 
### API scheduler/task/history

- 使用说明: 此api用于追踪指定dc定时更新任务的历史记录

- authentication: True

- url: `{host}:{port}/api/ericic/v1/scheduler/task/history`

#### method: get

##### case1: 通过id获取dc定时任务状态， 默认通过timestamp 倒叙排序


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task/history?cid={cid}&?filter={filter}&limit={limit}&offset={offset}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| cid   | false| true|data center 的 id |
| filter   | false| false| filter的取值范围为[static, dynamic], 默认filter取值为none(即返回结果包含static 和 dynamic的全部信息) |
| limit   | false| false| 每页展示条目， 默认为50 |
| offset   | false| false| 数据偏移量， 默认为0 |


- request body: 
```json5
{}
```

- response: 
```json5
    {
        "code": 200,
        "data": [
            {
                "id": "id",
                "task_name": "task_name",
                "dc_id": "dc_id",
                "dc_name": "dc_name",
                "status": "status", // status 的范围为 [true, false]
                "error_info": "traceback info", // 如果 status 为success， 此字段为 null
                "timestamp": 1111111
            }
        ],
        "total_num": 100,
        "status": true
    }
```
 
  ---

### API scheduler/task

- 使用说明: 此api用于管理dc更新的定时任务

- authentication: True

- url: `{host}:{port}/api/ericic/v1/scheduler/task`

#### method: get

##### case1: 通过id获取dc定时任务状态


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task?cid={cid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
| cid   | false| true|data center 的 id |


- request body: 
```json5
{}
```

- response: 
```json5
    {
        "code": 200,
        "data": [ // 当指定dc_id时， data数组内最多只有一个元素
            {
                "cid": "gaofzhan_test",
                "dynamic_task": {
                    "job_id": "gaofzhan_test:taskModel:method_view:dynamic_data_refresh",
                    "next_run_time": null,
                    "interval": 3600,
                    "start": 0,
                    "end": 0,
                    "status": false, //当该字段为false时， 表明任务处于pause状态， 并且此时的next_run_time一定为空
                },
                "static_task": {
                    "job_id": "gaofzhan_test:taskModel:method_view:refresh_static_task",
                    "next_run_time": "Wed, 16 Dec 2020 07:59:26 GMT",
                    "interval": 3600,
                    "start": 0,
                    "end": 0,
                    "status": true, // 当该字段为true是， 表明该任务处于running状态， 并且此时的next_run_time 一定有值
                }
            }
        ],
        "status": true
    }
```
##### case2: 获取全部dc 的数据更新定时任务（未加入定时任务的dc不会显示）  !!! 暂时关闭


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{}
```

- response: 
```json5
    {
        "code": 200,
        "data": [
           {
                "cid": "gaofzhan_test",
                "dynamic_task": {
                    "job_id": "gaofzhan_test:taskModel:method_view:dynamic_data_refresh",
                    "next_run_time": null,
                    "interval": 3600,
                    "start": 0,
                    "end": 0,
                    "status": false, //当该字段为false时， 表明任务处于pause状态， 并且此时的next_run_time一定为空
                },
                "static_task": {
                    "job_id": "gaofzhan_test:taskModel:method_view:refresh_static_task",
                    "next_run_time": "Wed, 16 Dec 2020 07:59:26 GMT",
                    "interval": 3600,
                    "start": 0,
                    "end": 0,
                    "status": true, // 当该字段为true是， 表明该任务处于running状态， 并且此时的next_run_time 一定有值
                }
            }
        ],
        "status": true
    }
```

#### method: post

##### case1: 恢复dc的定时任务（如果当前dc没有加入定时任务，则自动加入定时任务）


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{
    "cid": "gaofzhan_test", // dc 的 id
    "action": "resume", // action的取值范围为[resume, pause], resume 恢复， pause 暂停
    "task": "dynamic" // 取值范围为 [dynamic, static] dynamic 为dc的动态任务， static 为dc 的静态任务
}
```

- response: 
```json5
{
    "code": 201,
    "status": true
}
```
##### case2: 获取全部dc 的数据更新定时任务（为加入定时任务的dc不会显示）


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{
    "cid": "gaofzhan_test", // dc 的 id
    "action": "pause", // action的取值范围为[resume, pause], resume 恢复， pause 暂停
    "task": "dynamic" // 取值范围为 [dynamic, static] dynamic 为dc的动态任务， static 为dc 的静态任务
}
```

- response: 
```json5
{
    "code": 201,
    "status": true
}
```

#### method: put

##### case1: 修改dc定时任务的执行周期


- parameter: `{host}:{port}/api/ericic/v1/scheduler/task`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |


- request body: 
```json5
{
    "cid": "gaofzhan_test", // dc 的 id
    "interval": 3600, // interval 为task的执行周期单位为 秒
    "task": "dynamic" // 取值范围为 [dynamic, static] dynamic 为dc的动态任务， static 为dc 的静态任务
}
```

- response: 
```json5
{
    "code": 200,
    "status": true
}
```
 
 ---
 
### API connect_status

- 使用说明: 此api用于获取data_center 的连接状态

- authentication: True

- url: `{host}:{port}/api/ericic/v1/connect_status`

#### method: get


- parameter: `{host}:{port}/api/ericic/v1/connect_status?cid={cid}`

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |
|cid | False |  True  | data_center 的id |

- request body: 
```json5
{}
```

- response: 
```json5
{
    "status": true,
    "data": true,
    "code": 200
}
```

#### method: post


 - parameter: `{host}:{port}/api/ericic/v1/connect_status`
 
 

| 参数名称 | multi | 必填| description |
| :-----   | ----:| ----:|:----: |

- request body: 
```json5
{
    "lcm_ip": "lcm_ip",
    "lcm_user": "username",
    "lcm_pwd": "lcm_password",
}
```

- response: 
```json5
{
    "status": true,
    "data": true,
    "message": "message", // msg 预定义的msg包含 [Permission denied, Authentication failed, unable to connect to the host, unable to reach the host], 且仅在data 取值为 false 时 message 内容才具有具体含义
    "code": 200
}
```
 
 ---

### API config_data

- 使用说明:  动态获取APInova_data查询条件nova_tenant,stack_id

- authentication: True

- url: `{host}:{port}/api/ericic/v1/config_data`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/config_data?dc_id={dc_id}`

| 参数名称 | multi | 必填 |         description          |      |
| :------- | ----: | ---: | :--------------------------: | ---- |
| dc_id    | False | True | vm info 所属data_center 的id |      |



- request body: 

```json5
{}
```

- response:

```json5
{
    "code": 200,
    "data": [
        {
            "stack": [
                {"stack_id": "stack_id", "stack_name": "stack_name"},
            ],
            "tenant": [
                {"tenant_id": "tenant_id", "tenant_name": "tenant__name"}
            ]
        }
    ],
    "status": true
}
```

 
  ---
  
 

### API nova_data


- 使用说明: 此api用于获取与vm相关联的信息， 且一并返回相关flavor network tenant volume等信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/nova_data`

#### method: get

##### case: nova_data

- parameter: `{host}:{port}/api/ericic/v1/nova_data?dc_id={dc_id}&query={query}&filter={filter}&sort={sort}&order={order}&limit={limit}&offset={offset}`

| 参数名称 | multi |  必填 |                         description                          |
| :------- | ----: | ----: | :----------------------------------------------------------: |
| dc_id    | False |  True |                 vm info 所属data_center 的id                 |
| query    | False | False | 过滤查询条件，取值范围[nova_name,nova_status,nova_host,nova_tenant,stack_id],比如query=nova_name |
| filter   | False | False |                   filter=nova_name的属性值                   |
| sort     | False | False | 排序所依据的字段，取值范围为[memory,disk,vcpu,time]， 默认为time排序 |
| order    | False | False |       升序或者降序，取值范围为[asc, desc], 默认为desc        |
| limit    | False | False |             分页查询，单页展示数据量， 默认为10              |
| offset   | False | False |                   分页查询偏移量， 默认为0                   |


- request body: 

```json5
{}
```

- response: 

```json5
{
    "code": 200,
    "data": [
        {
            "created_time": 0,
            "dc_id": "dc_id",
            "flavor_disk": 0,
            "flavor_memory": 40960,
            "flavor_vcpu": 20,
            "host": "host",
            "networks": [
                {
                    "id": "network_id",
                    "ip": "ip",
                    "name": "network_name"
                },
            ],
            "nova_name": "nova_name",
            "nova_power_state": "Running",
            "nova_status": "Active",
            "nova_uuid": "nova_uuid",
            "tenant": "tenant",
            "volume": [
                {
                    "id":"volume_id",
                    "volume_type":"volume_type",
                    "volume_status":"volume_status",
                    "volume_size":"volume_size",
                    "volume_bootable":"volume_bootable"
        		}
            ]
        },
    ],
    "status": true,
    "total": 26
}
```
 
 ---
 

### API  host_config_data

- 使用说明:  动态获取APIhost_data查询条件,aggregate_name,availability_zone

- authentication: True

- url: `{host}:{port}/api/ericic/v1/host_config_data`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/host_config_data?dc_id={dc_id}`

| 参数名称 | multi | 必填 |          description           |
| :------- | ----: | ---: | :----------------------------: |
| dc_id    | False | True | host info 所属data_center 的id |


- request body: 

```json5
{}
```

- response: 

```json5
{
    "code": 200,
    "data": [
        {
            "host_az": [
                {
                    "availability_zone": "vepc_nm"
                },

            ],
            "host_ha": [
                {
                    "aggregate_name": "vepc_nm"
                },
            ]
        }
    ],
    "status": true
}
```

 
  ---


### API host_data


- 使用说明:  此api用于获取与host相关联的信息， 且一并返回相关vm信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/host_data`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/host_data?dc_id={dc_id}&query={query}&filter={filter}&sort={sort}&order={order}`

| 参数名称 | multi | 必填  | description                                           |
| -------- | ----- | ----- | ----------------------------------------------------- |
| dc_id    | False | True  | host info 所属data_center 的id                        |
| query    | False | False | 过滤查询条件，取值范围['host', 'host_aggregate', 'availability_zone', 'state'] |
| filter   | False | False | 当query=host时，filter取like逻辑，其余取equal逻辑                                    |
| sort     | False | False | 取值范围为['vm_num', 'update_time'], 默认为update_time                                             |
| order    | False | False | 升序或者降序，取值范围为[asc, desc], 默认为desc       |
| limit    | False | False | 分页查询，单页展示数据量， 默认为10                   |
| offset   | False | False | 分页查询偏移量， 默认为0                              |

- request body: 

```json5
{}
```

- response: 

```json5
{
    "code": 200,
    "data": [
        {
            "availability_zone": "availability_zone",
            "dc_id": "data_center_id",
            "host": "host_name",
            "host_aggregate": "host_aggregate",
            "id": "host_id",
            "state": "state",
            "status": "status",
            "timestamp": 1608533544,
            "update_at": 1608533346,
            "vm_info": [
                {
                    "id": "vm_id",
                    "name": "vm_name",
                    "status": "status",
                    "tenant_id": "tenant_id",
                    "tenant_name": "tenant_name"
                }
            ],
            "vm_num": 1
        },
    ],
    "status": true,
    "total": 12
}
```


  ---


### API Record


- 使用说明:  此api用于生成record，并批量获取record信息

- authentication: True

- url: `{host}:{port}/api/ericic/v1/record`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/record?cid={cid}`

| 参数名称 | multi | 必填  | description                                           |
| -------- | ----- | ----- | ----------------------------------------------------- |
| cid    | False | False  | record所属的data center 的id， cid为空时返回空                        |
| order    | False | False | 升序或者降序，取值范围为[asc, desc], 默认为按照timestamp，desc       |
| limit    | False | False | 分页查询，单页展示数据量， 默认为20                   |
| offset   | False | False | 分页查询偏移量， 默认为0                              |

- request body: 

```json5
{}
```

- response: 

```json5
{
    "code": 200,
    "data": [
        {
            "cee_version": "drop28",
            "cid": "d9fd0c83a9a243adab8fe97087ab9d62",
            "data_center": "gaofzhan",
            "id": "de8c46a08b244793b7472e462718da48",
            "lcm_ip": "fd00:7070:0:2bd::17",
            "name": "gaofzhan_record_test_2",
            "openrc_path": "/home/ceeinfra/admin-openrc.sh",
            "pid": "65062673e1344c47af7ae80d64cfeb57",
            "status": "successful",
            "system_name": "DL33",
            "timestamp": 1614678997,
            "traceback": null
        }
    ],
    "status": true,
    "total": 1
}
```


#### method: POST

- 使用说明:  此api用于生成record

- parameter: `{host}:{port}/api/ericic/v1/record`

| 参数名称 | multi | 必填  | description                                           |
| -------- | ----- | ----- | ----------------------------------------------------- |

- request body: 

```json5
{
    "name":"test",
    "cid": "d9fd0c83a9a243adab8fe97087ab9d62"
}
```

- response: 

```json5
{
    "code": 201,
    "id": "79859023651f4ebba67a9222c6014067",
    "status": true
}
```



#### method: DELETE

- 使用说明:  此api用于删除指定record，record状态为running时不可删除

- parameter: `{host}:{port}/api/ericic/v1/record`

| 参数名称 | multi | 必填  | description                                           |
| -------- | ----- | ----- | ----------------------------------------------------- |

- request body: 

```json5
{
    "id":"79859023651f4ebba67a9222c6014067",
}
```

- response: 

```json5
{
    "code": 200,
    "status": true
}
```



### API Record/Download


- 使用说明: 此api用于下载生成好的record报表

- authentication: True

- url: `{host}:{port}/api/ericic/v1/record/download`

#### method: get

- parameter: `{host}:{port}/api/ericic/v1/record/download?id={id}`

| 参数名称 | multi | 必填  | description                                           |
| -------- | ----- | ----- | ----------------------------------------------------- |
| id    | False | False  | record的id， id为空时返回空                        |

- request body: 

```json5
{}
```

- response: 

```json5
{
    "code": 200,
    "data": "base64",
    "status": true
}
```

