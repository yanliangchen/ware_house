import time
from backend.common.loghandler import BDLog
from backend.myBluePrint.ericic.model.vmModel import VmInfo
from backend.myBluePrint.ericic.model.hostModel import HostInfo
from backend.myBluePrint.ericic.model.flavorModel import FlavorModel
from backend.myBluePrint.ericic.model.tenantModel import TenantModel
from backend.myBluePrint.ericic.model.volumeModel import VolumeModel
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel
from backend.Model.connection import SESSION


class OpenstackHostDao:

    @classmethod
    def get_all_dc(cls):
        db_session = SESSION()
        try:
            res = db_session.query(DataCenterModel).all()
        finally:
            db_session.close()
        return res

    @classmethod
    def refresh_db(cls, info_dicts):
        db_session = SESSION()
        timestamp = int(time.time())
        try:
            for cid, info_dict in info_dicts.items():
                this_flavor_list = info_dict['flavor']
                this_host_list = info_dict['host']
                this_vm_list = info_dict['vm']
                this_tenant_list = info_dict['tenant']
                this_volume_list = info_dict['volume']
                # flush tables with cid
                db_session.query(VmInfo).filter(VmInfo.data_center_id == cid, ).delete()
                db_session.query(HostInfo).filter(HostInfo.data_center_id == cid, ).delete()
                db_session.query(TenantModel).filter(TenantModel.data_center_id == cid, ).delete()
                db_session.query(VolumeModel).filter(VolumeModel.data_center_id == cid, ).delete()
                db_session.query(FlavorModel).filter(FlavorModel.data_center_id == cid, ).delete()
                # gen db entries
                flavor_entries = [FlavorModel(**_, timestamp=timestamp) for _ in this_flavor_list]
                host_entries = [HostInfo(**_, timestamp=timestamp) for _ in this_host_list]
                vm_entries = [VmInfo(**_, timestamp=timestamp) for _ in this_vm_list]
                tenant_entries = [TenantModel(**_, timestamp=timestamp) for _ in this_tenant_list]
                volume_entries = [VolumeModel(**_, timestamp=timestamp) for _ in this_volume_list]
                # insert entries
                db_session.add_all(flavor_entries + host_entries + vm_entries + tenant_entries + volume_entries)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise Exception
        finally:
            db_session.close()
