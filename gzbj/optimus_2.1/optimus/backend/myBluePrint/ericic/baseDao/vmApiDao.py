from backend.common.loghandler import BDLog
from backend.myException.myExecption import MyRuntimeError
from backend.myBluePrint.ericic.model.vmModel import VmInfo
from backend.myBluePrint.ericic.model.hostModel import HostInfo
from backend.myBluePrint.ericic.model.flavorModel import FlavorModel
from backend.myBluePrint.ericic.model.tenantModel import TenantModel
from backend.myBluePrint.ericic.model.volumeModel import VolumeModel
from backend.Model.connection import SESSION


class VmApiDao:

    @classmethod
    def insert_data(cls):
        pass

    @classmethod
    def delete_all_relate_info(cls, cid):
        db_session = SESSION()
        try:
            db_session.query(VolumeModel).filter(VolumeModel.data_center_id == cid).delete()
            db_session.query(TenantModel).filter(TenantModel.data_center_id == cid).delete()
            db_session.query(FlavorModel).filter(FlavorModel.data_center_id == cid).delete()
            db_session.query(VmInfo).filter(VmInfo.data_center_id == cid).delete()
            db_session.query(HostInfo).filter(HostInfo.data_center_id == cid).delete()
            # db_session.query(DataCenterModel).filter(DataCenterModel.id == cid).delete()
            db_session.commit()
        except Exception as e:
            db_session.rollback()
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
    def get_volume_by_vm_ids(cls, vm_id_list):
        db_session = SESSION()
        try:
            res_dict = dict()
            for vm_id in vm_id_list:
                if vm_id:
                    volume_list = res_dict.setdefault(vm_id, list())
                    res = db_session.query(VolumeModel).filter(VolumeModel.vm_id == vm_id)
                    [volume_list.append(item) for item in res]
                else:
                    pass
            return res_dict
        finally:
            db_session.close()
