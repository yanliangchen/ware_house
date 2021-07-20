from backend.common.loghandler import BDLog
from backend.myBluePrint.ericic.model.vmModel import VmInfo
from backend.myBluePrint.ericic.model.hostModel import HostInfo
from backend.myBluePrint.ericic.model.flavorModel import FlavorModel
from backend.myBluePrint.ericic.model.tenantModel import TenantModel
from backend.myBluePrint.ericic.model.volumeModel import VolumeModel
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel
from backend.Model.connection import SESSION


class uploadApiDao:
    @classmethod
    def upload_insert_data(cls, _id, volume_write_data, flavor_write_data, vm_write_data, tenants_write_data,
                           host_write_data):
        db_session = SESSION()
        try:

            db_session.query(VmInfo).filter(VmInfo.data_center_id == _id).delete()
            db_session.query(HostInfo).filter(HostInfo.data_center_id == _id).delete()
            db_session.query(TenantModel).filter(TenantModel.data_center_id == _id).delete()
            db_session.query(VolumeModel).filter(VolumeModel.data_center_id == _id).delete()
            db_session.query(FlavorModel).filter(FlavorModel.data_center_id == _id).delete()
            db_session.add_all(volume_write_data)
            db_session.add_all(flavor_write_data)
            db_session.add_all(vm_write_data)
            db_session.add_all(tenants_write_data)
            db_session.add_all(host_write_data)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise Exception
        finally:
            db_session.close()

    @classmethod
    def delete_all_relate_info(cls, _id):
        db_session = SESSION()
        try:
            db_session.query(DataCenterModel).filter(DataCenterModel.id == _id).delete()
            db_session.query(VmInfo).filter(VmInfo.data_center_id == _id).delete()
            db_session.query(HostInfo).filter(HostInfo.data_center_id == _id).delete()
            db_session.query(TenantModel).filter(TenantModel.data_center_id == _id).delete()
            db_session.query(VolumeModel).filter(VolumeModel.data_center_id == _id).delete()
            db_session.query(FlavorModel).filter(FlavorModel.data_center_id == _id).delete()
            db_session.query(DataCenterModel).filter(DataCenterModel.id == _id).delete()
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise Exception
        finally:
            db_session.close()
