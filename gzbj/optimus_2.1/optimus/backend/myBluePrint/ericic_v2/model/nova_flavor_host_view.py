#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backend.myBluePrint.ericic_v2.model.ericic_base_model import EriCICBase
from sqlalchemy import Column, String, Integer, JSON
from backend.Model.connection import BASE


class nova_flavor_host_View(BASE):
    __tablename__ = 'nova_flavor_host_view'
    '''
    +-----------------+--------------+------+-----+---------+-------+
    | Field           | Type         | Null | Key | Default | Extra |
    +-----------------+--------------+------+-----+---------+-------+
    | n_id            | varchar(255) | NO   |     | NULL    |       |
    | n_name          | varchar(255) | YES  |     | NULL    |       |
    | n_power_state   | varchar(255) | YES  |     | NULL    |       |
    | n_task_state    | varchar(255) | YES  |     | NULL    |       |
    | n_flavor        | varchar(255) | YES  |     | NULL    |       |
    | n_host          | varchar(255) | YES  |     | NULL    |       |
    | n_created       | int(11)      | YES  |     | NULL    |       |
    | n_image         | json         | YES  |     | NULL    |       |
    | n_instance_name | varchar(255) | YES  |     | NULL    |       |
    | n_tenant_id     | varchar(255) | YES  |     | NULL    |       |
    | n_meta_data     | json         | YES  |     | NULL    |       |
    | n_dc_id         | varchar(50)  | NO   |     | NULL    |       |
    | n_timestamp     | int(11)      | NO   |     | NULL    |       |
    | f_id            | varchar(255) | NO   |     | NULL    |       |
    | f_vcpus         | int(11)      | YES  |     | NULL    |       |
    | f_memory_mib    | int(11)      | YES  |     | NULL    |       |
    | f_disk          | int(11)      | YES  |     | NULL    |       |
    | f_extra_specs   | json         | YES  |     | NULL    |       |
    | f_dc_id         | varchar(50)  | NO   |     | NULL    |       |
    | f_timestamp     | int(11)      | NO   |     | NULL    |       |
    | h_id            | varchar(255) | NO   |     | NULL    |       |
    | h_host          | varchar(255) | YES  |     | NULL    |       |
    | h_status        | varchar(36)  | YES  |     | NULL    |       |
    | h_state         | varchar(36)  | YES  |     | NULL    |       |
    | h_zone          | varchar(255) | YES  |     | NULL    |       |
    | h_update_at     | int(11)      | YES  |     | NULL    |       |
    | h_dc_id         | varchar(50)  | NO   |     | NULL    |       |
    | h_timestamp     | int(11)      | NO   |     | NULL    |       |
    | t_id            | varchar(255) | NO   |     | NULL    |       |
    | t_name          | varchar(255) | YES  |     | NULL    |       |
    | t_dc_id         | varchar(50)  | NO   |     | NULL    |       |
    | t_timestamp     | int(11)      | NO   |     | NULL    |       |
    +-----------------+--------------+------+-----+---------+-------+
    
    '''
    #  primary_key ?  id 我后加的 todo  .. ..

    n_id = Column(String(255), nullable=False, primary_key=True)
    n_name = Column(String(255), )
    n_power_state = Column(String(255), )
    n_task_state = Column(String(255), )
    n_flavor = Column(String(255), )
    n_host = Column(String(255), )
    n_created = Column(Integer(), )
    n_image = Column(JSON(), )
    n_instance_name = Column(String(255), )
    n_tenant_id = Column(String(255), )
    n_meta_data = Column(String(255), )
    n_dc_id = Column(String(50), nullable=False)
    n_timestamp = Column(Integer(), nullable=False)

    f_id = Column(String(255), nullable=False)
    f_vcpus = Column(Integer(), )
    f_memory_mib = Column(Integer(), )
    f_disk = Column(Integer(), )
    f_extra_specs = Column(JSON(), )
    f_dc_id = Column(String(50), nullable=False)
    f_timestamp = Column(Integer(), nullable=False)

    h_id = Column(String(255), nullable=False)
    h_host = Column(String(255), )
    h_status = Column(String(36), )
    h_state = Column(String(36), )
    h_zone = Column(String(255), )
    h_update_at = Column(Integer(), )
    h_dc_id = Column(String(50), nullable=False)
    h_timestamp = Column(Integer(), nullable=False)

    t_id = Column(String(255), nullable=False)
    t_name = Column(String(255), )
    t_dc_id = Column(String(50), nullable=False)
    t_timestamp = Column(Integer(), nullable=False)

    def __init__(self, n_id, n_name, n_power_state, n_task_state, n_flavor, n_host, n_created, n_image, n_instance_name,
                 n_tenant_id, n_meta_data, n_dc_id, n_timestamp, f_id, f_vcpus, f_memory_mib, f_disk, f_extra_specs,
                 f_dc_id, f_timestamp, h_id, h_host, h_status, h_state, h_zone, h_update_at, h_dc_id, h_timestamp, t_id,
                 t_name, t_dc_id, t_timestamp):
        self.n_id = n_id
        self.n_name = n_name
        self.n_power_state = n_power_state
        self.n_task_state = n_task_state
        self.n_flavor = n_flavor
        self.n_host = n_host
        self.n_created = n_created
        self.n_image = n_image
        self.n_instance_name = n_instance_name
        self.n_tenant_id = n_tenant_id
        self.n_meta_data = n_meta_data
        self.n_dc_id = n_dc_id
        self.n_timestamp = n_timestamp
        self.f_id = f_id
        self.f_vcpus = f_vcpus
        self.f_memory_mib = f_memory_mib
        self.f_disk = f_disk
        self.f_extra_specs = f_extra_specs
        self.f_dc_id = f_dc_id
        self.f_timestamp = f_timestamp
        self.h_dc_id = h_id
        self.n_host = h_host
        self.h_status = h_status
        self.h_state = h_state
        self.h_zone = h_zone
        self.h_update_at = h_update_at
        self.h_dc_id = h_dc_id
        self.h_timestamp = h_timestamp
        self.t_id = t_id
        self.t_name = t_name
        self.t_dc_id = t_dc_id
        self.t_timestamp = t_timestamp




