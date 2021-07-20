/*
 Navicat Premium Data Transfer

 Source Server         : bj
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : optimus

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 03/03/2021 11:00:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cinder_list_table
-- ----------------------------
DROP TABLE IF EXISTS `cinder_list_table`;
CREATE TABLE `cinder_list_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `size` int(11) NULL DEFAULT NULL,
  `volume_type` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `bootable` tinyint(1) NULL DEFAULT NULL,
  `attach_to` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `tenant_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cinder_quota_usage_table
-- ----------------------------
DROP TABLE IF EXISTS `cinder_quota_usage_table`;
CREATE TABLE `cinder_quota_usage_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `project_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `resource` json NULL,
  `in_use` int(11) NULL DEFAULT NULL,
  `reserved` int(11) NULL DEFAULT NULL,
  `limit` int(11) NULL DEFAULT NULL,
  `allocated` int(11) NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for data_center_bak
-- ----------------------------
DROP TABLE IF EXISTS `data_center_bak`;
CREATE TABLE `data_center_bak`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `mode` tinyint(1) NOT NULL,
  `country` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `province` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `system_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cee_version` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lcm_ip` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lcm_user` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lcm_pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `openstackrc_dir` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `lcmrc_dir` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for db_refresh_task
-- ----------------------------
DROP TABLE IF EXISTS `db_refresh_task`;
CREATE TABLE `db_refresh_task`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `start` int(11) NOT NULL DEFAULT 28800,
  `end` int(11) NOT NULL DEFAULT 64800,
  `interval` int(11) NULL DEFAULT NULL,
  `dc_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `version` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flavor
-- ----------------------------
DROP TABLE IF EXISTS `flavor`;
CREATE TABLE `flavor`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `vcpu` int(10) NOT NULL,
  `memory` int(10) NOT NULL,
  `disk` int(10) NOT NULL,
  `data_center_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for host_info2
-- ----------------------------
DROP TABLE IF EXISTS `host_info2`;
CREATE TABLE `host_info2`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `host_aggregate` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `availability_zone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `compute_state` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `total_cpu` int(11) NOT NULL,
  `free_cpu` int(11) NOT NULL,
  `total_memory` int(11) NOT NULL,
  `free_memory` int(11) NOT NULL,
  `total_disk` int(11) NOT NULL,
  `free_disk` int(11) NOT NULL,
  `data_center_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hypervisor_stats
-- ----------------------------
DROP TABLE IF EXISTS `hypervisor_stats`;
CREATE TABLE `hypervisor_stats`  (
  `item_id` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `local_gb` int(11) NOT NULL,
  `local_gb_used` int(11) NOT NULL,
  `memory_mg` int(11) NOT NULL,
  `memory_mg_used` int(11) NOT NULL,
  `vcpus` int(11) NOT NULL,
  `vcpus_used` int(11) NOT NULL,
  `dc_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `update_time` int(11) NOT NULL,
  PRIMARY KEY (`item_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for json_mapping
-- ----------------------------
DROP TABLE IF EXISTS `json_mapping`;
CREATE TABLE `json_mapping`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for neutron_port_table
-- ----------------------------
DROP TABLE IF EXISTS `neutron_port_table`;
CREATE TABLE `neutron_port_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `status` varchar(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `binding_host_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `binding_profile` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `binding_vif_type` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `device_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `subnet_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `ip_address` varchar(63) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `allowed_address_pairs` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `mac_address` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `qos_policy_id` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `security_groups` json NULL,
  `port_security_enabled` tinyint(1) NULL DEFAULT NULL,
  `vif_details` json NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for neutron_vif_detail_table
-- ----------------------------
DROP TABLE IF EXISTS `neutron_vif_detail_table`;
CREATE TABLE `neutron_vif_detail_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `vif_details` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `tenant_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nova_aggregate_host_relation_table
-- ----------------------------
DROP TABLE IF EXISTS `nova_aggregate_host_relation_table`;
CREATE TABLE `nova_aggregate_host_relation_table`  (
  `ag_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `aggregate_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `availability_zone` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `host` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `meta_data` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`host`, `ag_id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nova_aggregate_table
-- ----------------------------
DROP TABLE IF EXISTS `nova_aggregate_table`;
CREATE TABLE `nova_aggregate_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `availability_zone` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nova_flavor_table
-- ----------------------------
DROP TABLE IF EXISTS `nova_flavor_table`;
CREATE TABLE `nova_flavor_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `vcpus` int(11) NULL DEFAULT NULL,
  `memory_mib` int(11) NULL DEFAULT NULL,
  `disk` int(11) NULL DEFAULT NULL,
  `extra_specs` json NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nova_service_table
-- ----------------------------
DROP TABLE IF EXISTS `nova_service_table`;
CREATE TABLE `nova_service_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `host` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `status` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `state` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `zone` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `update_at` int(11) NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for nova_table
-- ----------------------------
DROP TABLE IF EXISTS `nova_table`;
CREATE TABLE `nova_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `power_state` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `task_state` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `flavor` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `host` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `created` int(11) NULL DEFAULT NULL,
  `image` json NULL,
  `instance_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `tenant_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `meta_data` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for openstack_hypervisor_stats_table
-- ----------------------------
DROP TABLE IF EXISTS `openstack_hypervisor_stats_table`;
CREATE TABLE `openstack_hypervisor_stats_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `local_gb` int(11) NULL DEFAULT NULL,
  `local_gb_used` int(11) NULL DEFAULT NULL,
  `memory_mg` int(11) NULL DEFAULT NULL,
  `memory_mg_used` int(11) NULL DEFAULT NULL,
  `vcpus` int(11) NULL DEFAULT NULL,
  `vcpus_used` int(11) NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for openstack_project_table
-- ----------------------------
DROP TABLE IF EXISTS `openstack_project_table`;
CREATE TABLE `openstack_project_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for openstack_quota_table
-- ----------------------------
DROP TABLE IF EXISTS `openstack_quota_table`;
CREATE TABLE `openstack_quota_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `cores_in_use` int(11) NULL DEFAULT NULL,
  `cores_limit` int(11) NULL DEFAULT NULL,
  `ram_in_use` int(11) NULL DEFAULT NULL,
  `ram_limit` int(11) NULL DEFAULT NULL,
  `project_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for openstack_stack_resource_table
-- ----------------------------
DROP TABLE IF EXISTS `openstack_stack_resource_table`;
CREATE TABLE `openstack_stack_resource_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `resource_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `physical_resource_id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `resource_type` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `resource_status` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `stack_id` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for openstack_volume_type_table
-- ----------------------------
DROP TABLE IF EXISTS `openstack_volume_type_table`;
CREATE TABLE `openstack_volume_type_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `is_public` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `data_center` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cid` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cee_version` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `lcm_ip` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `system_name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `openrc_path` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `status` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `pid` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL COMMENT 'post_id the pkey of mongo\'s record collection',
  `timestamp` int(11) NULL DEFAULT NULL,
  `traceback` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `version` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `optimus_record_name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for refresh_task_history_table
-- ----------------------------
DROP TABLE IF EXISTS `refresh_task_history_table`;
CREATE TABLE `refresh_task_history_table`  (
  `id` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `task_name` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `dc_name` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `status` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `error_info` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for snapshot
-- ----------------------------
DROP TABLE IF EXISTS `snapshot`;
CREATE TABLE `snapshot`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `data_center` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `cee_version` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` int(11) NULL DEFAULT NULL,
  `data_load_time` int(11) NULL DEFAULT NULL,
  `timestamp` int(11) NULL DEFAULT NULL,
  `version` int(11) NULL DEFAULT NULL,
  `excel_file` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `snapshot_name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for stack_table
-- ----------------------------
DROP TABLE IF EXISTS `stack_table`;
CREATE TABLE `stack_table`  (
  `id` varchar(36) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `project` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `stack_status` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `creation_time` int(11) NULL DEFAULT NULL,
  `dc_id` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  PRIMARY KEY (`id`, `dc_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task`  (
  `id` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `project_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `site_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cee_version` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `input` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `output` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL DEFAULT 0,
  `visible` tinyint(1) NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for tenant_info
-- ----------------------------
DROP TABLE IF EXISTS `tenant_info`;
CREATE TABLE `tenant_info`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `data_center_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `version` int(255) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for vm_info2
-- ----------------------------
DROP TABLE IF EXISTS `vm_info2`;
CREATE TABLE `vm_info2`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `power_state` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `networks` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `flavor_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tenant_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `host_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `data_center_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  `instance_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for volume_info
-- ----------------------------
DROP TABLE IF EXISTS `volume_info`;
CREATE TABLE `volume_info`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `size` int(11) NOT NULL,
  `type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bootable` tinyint(1) NOT NULL,
  `vm_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `data_center_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `timestamp` int(11) NOT NULL,
  `version` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- View structure for host_view
-- ----------------------------
DROP VIEW IF EXISTS `host_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`%` SQL SECURITY DEFINER VIEW `host_view` AS select `host_info2`.`id` AS `host_id`,`host_info2`.`name` AS `host`,`host_info2`.`host_aggregate` AS `host_aggregate`,`host_info2`.`availability_zone` AS `availability_zone`,`host_info2`.`compute_state` AS `compute_state`,concat(`host_info2`.`free_cpu`,'/',`host_info2`.`total_cpu`) AS `cpu_percent`,concat(`host_info2`.`free_memory`,'/',`host_info2`.`total_memory`) AS `memory_percent`,concat(`host_info2`.`free_disk`,'/',`host_info2`.`total_disk`) AS `disk_percent`,`host_info2`.`data_center_id` AS `data_center_id`,`data_center_bak`.`cee_version` AS `cee_version`,`host_info2`.`timestamp` AS `timestamp` from (`host_info2` join `data_center_bak`) where (`host_info2`.`data_center_id` = `data_center_bak`.`id`);

-- ----------------------------
-- View structure for nova_flavor_host_view
-- ----------------------------
DROP VIEW IF EXISTS `nova_flavor_host_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `nova_flavor_host_view` AS select `nova_table`.`id` AS `n_id`,`nova_table`.`name` AS `n_name`,`nova_table`.`power_state` AS `n_power_state`,`nova_table`.`task_state` AS `n_task_state`,`nova_table`.`flavor` AS `n_flavor`,`nova_table`.`host` AS `n_host`,`nova_table`.`created` AS `n_created`,`nova_table`.`image` AS `n_image`,`nova_table`.`instance_name` AS `n_instance_name`,`nova_table`.`tenant_id` AS `n_tenant_id`,`nova_table`.`meta_data` AS `n_meta_data`,`nova_table`.`dc_id` AS `n_dc_id`,`nova_table`.`timestamp` AS `n_timestamp`,`nova_flavor_table`.`id` AS `f_id`,`nova_flavor_table`.`vcpus` AS `f_vcpus`,`nova_flavor_table`.`memory_mib` AS `f_memory_mib`,`nova_flavor_table`.`disk` AS `f_disk`,`nova_flavor_table`.`extra_specs` AS `f_extra_specs`,`nova_flavor_table`.`dc_id` AS `f_dc_id`,`nova_flavor_table`.`timestamp` AS `f_timestamp`,`nova_service_table`.`id` AS `h_id`,`nova_service_table`.`host` AS `h_host`,`nova_service_table`.`status` AS `h_status`,`nova_service_table`.`state` AS `h_state`,`nova_service_table`.`zone` AS `h_zone`,`nova_service_table`.`update_at` AS `h_update_at`,`nova_service_table`.`dc_id` AS `h_dc_id`,`nova_service_table`.`timestamp` AS `h_timestamp`,`openstack_project_table`.`id` AS `t_id`,`openstack_project_table`.`name` AS `t_name`,`openstack_project_table`.`dc_id` AS `t_dc_id`,`openstack_project_table`.`timestamp` AS `t_timestamp` from (((`nova_table` join `nova_flavor_table`) join `nova_service_table`) join `openstack_project_table`) where ((`nova_table`.`flavor` = `nova_flavor_table`.`id`) and (`nova_table`.`host` = `nova_service_table`.`host`) and (`nova_table`.`tenant_id` = `openstack_project_table`.`id`) and (`nova_table`.`dc_id` = `nova_flavor_table`.`dc_id`) and (`nova_table`.`dc_id` = `nova_service_table`.`dc_id`) and (`nova_table`.`dc_id` = `openstack_project_table`.`dc_id`));

-- ----------------------------
-- View structure for nova_flavor_host_view_new
-- ----------------------------
DROP VIEW IF EXISTS `nova_flavor_host_view_new`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `nova_flavor_host_view_new` AS select `nova_table`.`id` AS `n_id`,`nova_table`.`name` AS `n_name`,`nova_table`.`power_state` AS `n_power_state`,`nova_table`.`task_state` AS `n_task_state`,`nova_table`.`flavor` AS `n_flavor`,`nova_table`.`host` AS `n_host`,`nova_table`.`created` AS `n_created`,`nova_table`.`image` AS `n_image`,`nova_table`.`instance_name` AS `n_instance_name`,`nova_table`.`tenant_id` AS `n_tenant_id`,`nova_table`.`meta_data` AS `n_meta_data`,`nova_table`.`dc_id` AS `n_dc_id`,`nova_table`.`timestamp` AS `n_timestamp`,`nova_flavor_table`.`id` AS `f_id`,`nova_flavor_table`.`vcpus` AS `f_vcpus`,`nova_flavor_table`.`memory_mib` AS `f_memory_mib`,`nova_flavor_table`.`disk` AS `f_disk`,`nova_flavor_table`.`extra_specs` AS `f_extra_specs`,`nova_flavor_table`.`dc_id` AS `f_dc_id`,`nova_flavor_table`.`timestamp` AS `f_timestamp`,`nova_service_table`.`id` AS `h_id`,`nova_service_table`.`host` AS `h_host`,`nova_service_table`.`status` AS `h_status`,`nova_service_table`.`state` AS `h_state`,`nova_service_table`.`zone` AS `h_zone`,`nova_service_table`.`update_at` AS `h_update_at`,`nova_service_table`.`dc_id` AS `h_dc_id`,`nova_service_table`.`timestamp` AS `h_timestamp`,`openstack_project_table`.`id` AS `t_id`,`openstack_project_table`.`name` AS `t_name`,`openstack_project_table`.`dc_id` AS `t_dc_id`,`openstack_project_table`.`timestamp` AS `t_timestamp`,`neutron_port_table`.`ip_address` AS `np_ipaddress` from ((((`nova_table` join `nova_flavor_table`) join `nova_service_table`) join `openstack_project_table`) join `neutron_port_table`) where ((`nova_table`.`flavor` = `nova_flavor_table`.`id`) and (`nova_table`.`host` = `nova_service_table`.`host`) and (`nova_table`.`tenant_id` = `openstack_project_table`.`id`) and (`nova_table`.`dc_id` = `nova_flavor_table`.`dc_id`) and (`nova_table`.`dc_id` = `nova_service_table`.`dc_id`) and (`nova_table`.`dc_id` = `openstack_project_table`.`dc_id`) and (`nova_table`.`id` = `neutron_port_table`.`device_id`));

-- ----------------------------
-- View structure for nova_service_view
-- ----------------------------
DROP VIEW IF EXISTS `nova_service_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`%` SQL SECURITY DEFINER VIEW `nova_service_view` AS select `optimus`.`nova_service_table`.`id` AS `id`,`optimus`.`nova_service_table`.`host` AS `host`,`optimus`.`nova_service_table`.`status` AS `status`,`optimus`.`nova_service_table`.`state` AS `state`,`optimus`.`nova_service_table`.`zone` AS `availability_zone`,`optimus`.`nova_service_table`.`update_at` AS `update_at`,`optimus`.`nova_service_table`.`dc_id` AS `dc_id`,`optimus`.`nova_service_table`.`timestamp` AS `timestamp`,if(isnull(`t`.`vm_num`),0,`t`.`vm_num`) AS `vm_num`,`optimus`.`nova_aggregate_host_relation_table`.`aggregate_name` AS `host_aggregate` from ((`optimus`.`nova_service_table` left join (select `optimus`.`nova_table`.`host` AS `host`,`optimus`.`nova_table`.`dc_id` AS `dc_id`,count(0) AS `vm_num` from `optimus`.`nova_table` group by `optimus`.`nova_table`.`dc_id`,`optimus`.`nova_table`.`host`) `t` on(((`optimus`.`nova_service_table`.`dc_id` = `t`.`dc_id`) and (`t`.`host` = `optimus`.`nova_service_table`.`host`)))) left join `optimus`.`nova_aggregate_host_relation_table` on(((`optimus`.`nova_service_table`.`host` = `optimus`.`nova_aggregate_host_relation_table`.`host`) and (`optimus`.`nova_service_table`.`dc_id` = `optimus`.`nova_aggregate_host_relation_table`.`dc_id`))));

-- ----------------------------
-- View structure for vm_host_view
-- ----------------------------
DROP VIEW IF EXISTS `vm_host_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`%` SQL SECURITY DEFINER VIEW `vm_host_view` AS select `vm_view`.`id` AS `vm_id`,`vm_view`.`uuid` AS `uuid`,`vm_view`.`name` AS `name`,`vm_view`.`status` AS `status`,`vm_view`.`power_state` AS `power_state`,`vm_view`.`create_time` AS `create_time`,`vm_view`.`networks` AS `networks`,`vm_view`.`vcpu` AS `vcpu`,`vm_view`.`memory` AS `memory`,`vm_view`.`disk` AS `disk`,`vm_view`.`tenant` AS `tenant`,`host_view`.`host_id` AS `host_id`,`host_view`.`host` AS `host`,`host_view`.`host_aggregate` AS `host_aggregate`,`host_view`.`availability_zone` AS `availability_zone`,`host_view`.`compute_state` AS `compute_state`,`host_view`.`cpu_percent` AS `cpu_percent`,`host_view`.`memory_percent` AS `memory_percent`,`host_view`.`disk_percent` AS `disk_percent`,`host_view`.`data_center_id` AS `data_center_id`,`host_view`.`timestamp` AS `timestamp` from (`optimus`.`host_view` left join `optimus`.`vm_view` on((`host_view`.`host_id` = `vm_view`.`host_id`)));

-- ----------------------------
-- View structure for vm_view
-- ----------------------------
DROP VIEW IF EXISTS `vm_view`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`%` SQL SECURITY DEFINER VIEW `vm_view` AS select `this_view`.`id` AS `id`,`this_view`.`uuid` AS `uuid`,`this_view`.`name` AS `name`,`this_view`.`status` AS `status`,`this_view`.`power_state` AS `power_state`,`this_view`.`create_time` AS `create_time`,`this_view`.`networks` AS `networks`,`this_view`.`vcpu` AS `vcpu`,`this_view`.`memory` AS `memory`,`this_view`.`disk` AS `disk`,`this_view`.`host_id` AS `host_id`,`optimus`.`tenant_info`.`name` AS `tenant`,`optimus`.`tenant_info`.`data_center_id` AS `data_center_id`,`this_view`.`timestamp` AS `timestamp` from (`optimus`.`tenant_info` join (select `optimus`.`vm_info2`.`id` AS `id`,`optimus`.`vm_info2`.`uuid` AS `uuid`,`optimus`.`vm_info2`.`name` AS `name`,`optimus`.`vm_info2`.`status` AS `status`,`optimus`.`vm_info2`.`power_state` AS `power_state`,`optimus`.`vm_info2`.`create_time` AS `create_time`,`optimus`.`vm_info2`.`networks` AS `networks`,`optimus`.`flavor`.`vcpu` AS `vcpu`,`optimus`.`flavor`.`memory` AS `memory`,`optimus`.`flavor`.`disk` AS `disk`,`optimus`.`vm_info2`.`tenant_id` AS `tenant_id`,`optimus`.`vm_info2`.`host_id` AS `host_id`,`optimus`.`vm_info2`.`timestamp` AS `timestamp` from (`optimus`.`vm_info2` join `optimus`.`flavor`) where (`optimus`.`vm_info2`.`flavor_id` = `optimus`.`flavor`.`id`)) `this_view`) where (`optimus`.`tenant_info`.`id` = `this_view`.`tenant_id`);

SET FOREIGN_KEY_CHECKS = 1;
