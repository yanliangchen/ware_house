from backend.common.loghandler import BDLog
from backend.myBluePrint.ericic.model.vmModelView import VmModelView
from backend.myBluePrint.ericic.model.volumeModel import VolumeModel
from backend.myException.myExecption import MyRuntimeError
from backend.Model.connection import SESSION


class HostApiDao:

    @classmethod
    def get_vm_by_hid(cls, host_id):
        db_session = SESSION()
        try:
            res = db_session.query(VmModelView).filter(VmModelView.host_id == host_id)
            return res
        except Exception as e:
            BDLog.error(e)
            raise MyRuntimeError('service error', 503)
        finally:
            db_session.close()

    @classmethod
    def get_volume_by_vid(cls, vm_id):
        db_session = SESSION()
        try:
            res = db_session.query(VolumeModel).filter(VolumeModel.vm_id == vm_id)
            return res
        except Exception as e:
            BDLog.error(e)
            raise MyRuntimeError('service error', 503)
        finally:
            db_session.close()

    @classmethod
    def get_vm_infos(cls, host_id_list, vm_columns):
        res_dict = dict()
        db_session = SESSION()
        try:
            for host_id in host_id_list:
                vm_info_list = res_dict.setdefault(host_id, list())
                vm_entities = db_session.query(VmModelView).filter(VmModelView.host_id == host_id)
                for vm_entity in vm_entities:
                    vm_info_dict = dict()
                    for column in vm_columns:
                        if column == 'volume':
                            vm_info_dict[column] = list()
                            vm_id = vm_entity.id
                            volume_entities = db_session.query(VolumeModel).filter(VolumeModel.vm_id == vm_id)
                            for volume_entity in volume_entities:
                                volume_info_dict = dict()
                                volume_info_dict['name'] = volume_entity.name
                                volume_info_dict['status'] = volume_entity.status
                                volume_info_dict['size'] = volume_entity.size
                                volume_info_dict['type'] = volume_entity.type
                                volume_info_dict['bootable'] = volume_entity.bootable
                                vm_info_dict[column].append(volume_info_dict)
                        # elif column == 'id':
                        #     continue
                        else:
                            db_entity_attr_val = getattr(vm_entity, column)
                            vm_info_dict[column] = db_entity_attr_val
                    vm_info_list.append(vm_info_dict)
            return res_dict
        finally:
            db_session.close()
