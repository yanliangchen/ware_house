from backend.myBluePrint.ericic.model import hostModel, vmModel, tenantModel, volumeModel
from backend.myBluePrint.ericic.baseDao.uploadApiDao import uploadApiDao
from backend.myBluePrint.ericic.model.flavorModel import FlavorModel
import uuid


class uploadService():

    @classmethod
    def upload(cls, pre_times, dc_id, flavor_info, hosts_info, az_ha_info, vm_info, tenants, volume_info):
        vm_info_new = []
        vm_write_data = []
        host_write_data = []
        tenants_write_data = []
        flavor_write_data = []
        volume_write_data = []
        for every_flavor in flavor_info:
            flavor_id = uuid.uuid4().hex
            for every_vm in vm_info:
                if every_flavor['ID'] == every_vm['flavor']:
                    every_vm['flavor_id'] = flavor_id
                    vm_info_new.append(every_vm)

            flavor_uuid = every_flavor['ID']
            flavor_vcpu = every_flavor['VCPUs']
            flavor_ram = every_flavor['RAM']
            flavor_Disk = every_flavor['Disk']
            flavor_u = FlavorModel(_id=flavor_id, uuid=flavor_uuid,
                                   vcpu=flavor_vcpu, memory=flavor_ram, disk=flavor_Disk,
                                   data_center_id=dc_id, timestamp=pre_times)
            flavor_write_data.append(flavor_u)

        list_hosts = []
        for host in hosts_info:
            for az_ha in az_ha_info:
                if host['Hypervisor Hostname'] in az_ha['hosts']:
                    host['az'] = az_ha['availability_zone']
                    host['ha'] = az_ha['name']
            else:
                list_hosts.append(host)

        list_host = []
        for every_host in list_hosts:
            if every_host.get('ha') == None:
                every_host['ha'] = ''
                every_host['az'] = ''
            list_host.append(every_host)

        lists_host_id = []
        for every_host in list_host:
            host_id = uuid.uuid4().hex
            every_host['id'] = host_id
            lists_host_id.append(every_host)
            name = every_host['Hypervisor Hostname']
            ha = every_host['ha']
            az = every_host['az']
            compute_state = every_host['State']
            total_cpu = every_host['vCPUs']
            used_cpu = every_host['vCPUs Used']
            free_cpu = total_cpu - used_cpu
            total_memory = every_host['Memory MB']
            used_memory = every_host['Memory MB Used']
            free_memory = total_memory - used_memory
            total_disk = every_host['Total Disk']
            free_disk = every_host['Free Disk']
            host_u = hostModel.HostInfo(host_id, name, ha, az, compute_state, total_cpu, free_cpu, total_memory,
                                        free_memory, total_disk, free_disk, dc_id, pre_times)
            host_write_data.append(host_u)

        vm_hosts = []
        for every_vm in vm_info_new:
            for h_id_host in lists_host_id:
                if every_vm['host'] == h_id_host['Hypervisor Hostname']:
                    every_vm['host_id'] = h_id_host['id']
                    vm_hosts.append(every_vm)

        tenants_list = []
        for i in tenants:
            tenants_ID = uuid.uuid4().hex
            i_uuid = i['uuid'] = i['ID']
            i_id = i['ID'] = tenants_ID
            i_name = i['Name']
            tenants_list.append(i)
            tenants_u = tenantModel.TenantModel(uuid=i_uuid, _id=i_id, name=i_name, data_center_id=dc_id,
                                                timestamp=pre_times)
            tenants_write_data.append(tenants_u)

        for vm in vm_hosts:
            vm_id = uuid.uuid4().hex
            vm_uuid = vm['id']
            vm_name = vm['name']
            status = vm['status']
            power_state = vm['power_state']
            if int(power_state) == 1:
                power_state = 'Running'
            elif int(power_state) == 0:
                power_state = 'NOSTATE'
            elif int(power_state) == 4:
                power_state = 'Shutdown'

            create_time = vm['created']
            networks = vm['networks']
            vm_flavor_id = vm['flavor_id']
            host_id = vm['host_id']
            tenant_id = vm['tenant_id']
            # add  instance_name
            instance_name = vm['instance_name']
            for every_tenants in tenants_list:
                if every_tenants['uuid'] == tenant_id:
                    tenant_id = every_tenants['ID']
            vm_u = vmModel.VmInfo(_id=vm_id, uuid=vm_uuid, name=vm_name, status=status, power_state=power_state,
                                  create_time=create_time,
                                  networks=networks, flavor_id=vm_flavor_id, tenant_id=tenant_id,
                                  host_id=host_id, instance_name=instance_name,
                                  data_center_id=dc_id, timestamp=pre_times, )
            vm_write_data.append(vm_u)

        for every_volume in volume_info:
            volume_id = uuid.uuid4().hex
            volume_uuid = every_volume['ID']
            volume_name = every_volume['Name']
            volume_status = every_volume['Status']
            volume_size = every_volume['Size']
            type = every_volume['Type']
            if type == None:
                type = ''
            bootable = every_volume['Bootable']
            if bootable == 'false':
                bootable = False
            else:
                bootable = True
            vm_id = every_volume['Attached to'][0]['server_id'] if len(every_volume['Attached to']) else None
            for vm_item in vm_write_data:
                vm_item_id = vm_item.id
                vm_uuid = vm_item.uuid
                if vm_uuid == vm_id:
                    vm_id = vm_item_id

            volume_u = volumeModel.VolumeModel(volume_id, volume_uuid, volume_name, volume_status, volume_size,
                                               type,
                                               bootable, vm_id, dc_id, pre_times)
            volume_write_data.append(volume_u)

        uploadApiDao.upload_insert_data(dc_id,volume_write_data, flavor_write_data, vm_write_data, tenants_write_data,
                                        host_write_data)
