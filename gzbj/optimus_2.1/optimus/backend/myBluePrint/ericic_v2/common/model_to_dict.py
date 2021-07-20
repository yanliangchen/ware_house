from collections import Iterable


class Model_To_Dict():
    @classmethod
    def model_to_dict(cls, result):
        try:
            if isinstance(result, Iterable):
                tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
                for t in tmp:
                    t.pop('_sa_instance_state')
            else:
                tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
                tmp.pop('_sa_instance_state')
            return tmp
        except BaseException as e:
            print(e.args)
            raise TypeError('Type error of parameter')

    @classmethod
    def dict_handle(cls, _data):
        nova_h_f_t_dict = cls.model_to_dict(_data[0])
        volume_dict = cls.model_to_dict(_data[1])
        net_work_dict = cls.model_to_dict(_data[2])
        nova_new_list = []
        for every_nova in nova_h_f_t_dict:
            nova_volume_list = every_nova['volume'] = []
            nova_networks_list = every_nova['networks'] = []
            for every_volume in volume_dict:
                if every_nova['n_id'] == every_volume['attach_to']:
                    every_volume_data = {}
                    every_volume_data['id'] = every_volume['attach_to']
                    every_volume_data['volume_type'] = every_volume['volume_type']
                    every_volume_data['volume_name'] = every_volume['name']
                    every_volume_data['volume_status'] = every_volume['status']
                    every_volume_data['volume_size'] = every_volume['size']
                    every_volume_data['volume_bootable'] = every_volume['bootable']
                    nova_volume_list.append(every_volume_data)
                    # nova_volume_list.append(every_volume['attach_to'])
            for every_networks in net_work_dict:
                if every_nova['n_id'] == every_networks['device_id']:
                    every_networks_data = {}
                    every_networks_data['id'] = every_networks['device_id']
                    every_networks_data['name'] = every_networks['name']
                    every_networks_data['ip'] = every_networks['ip_address']
                    nova_networks_list.append(every_networks_data)
                    # nova_networks_list.append(every_networks['device_id'])
            nova_new_list.append(every_nova)
        # 按需返回
        resp = []
        for every_resp in nova_new_list:
            resp_dict = {}
            resp_dict['dc_id'] = every_resp['n_dc_id']
            resp_dict['nova_uuid'] = every_resp['n_id']
            resp_dict['nova_name'] = every_resp['n_name']
            resp_dict['nova_power_state'] = every_resp['n_power_state']
            resp_dict['nova_status'] = every_resp['n_task_state']
            resp_dict['flavor_vcpu'] = every_resp['f_vcpus']
            resp_dict['flavor_memory'] = every_resp['f_memory_mib']
            resp_dict['flavor_disk'] = every_resp['f_disk']
            resp_dict['tenant'] = every_resp['t_name']
            resp_dict['created_time'] = every_resp['n_created']
            resp_dict['host'] = every_resp['h_host']
            resp_dict['volume'] = every_resp['volume']
            resp_dict['networks'] = every_resp['networks']
            resp.append(resp_dict)

        return resp
