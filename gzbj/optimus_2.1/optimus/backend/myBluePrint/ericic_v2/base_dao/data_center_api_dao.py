from config import MONGO_TIMEOUT
from celery_app import celery_app
from sqlalchemy.exc import IntegrityError
from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION
from backend.myException.myExecption import MyRuntimeError
from backend.scheduler_handler.task_mapping import STATIC_REFRESH, DYNAMIC_REFRESH
from backend.myBluePrint.ericic_v2.model.data_center_table import DataCenterModel
from backend.myBluePrint.ericic_v2.model.cinder_list_table import CinderModel
from backend.myBluePrint.ericic_v2.model.cinder_quota_usage_table import CinderQuotaUsageModel
from backend.myBluePrint.ericic_v2.model.neutron_port_table import NeutronPortTable
from backend.myBluePrint.ericic_v2.model.neutron_vif_detail_table import NeutronVifDetailModel
from backend.myBluePrint.ericic_v2.model.nova_aggregate_host_relation_table import AggregateHostRelation
from backend.myBluePrint.ericic_v2.model.nova_aggregate_table import NovaAggregateModel
from backend.myBluePrint.ericic_v2.model.nova_flavor_table import NovaFlavorModel
from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.nova_table import NovaModel
from backend.myBluePrint.ericic_v2.model.openstack_hypervisor_stats_table import OpenstackHypervisorStatsModel
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel
from backend.myBluePrint.ericic_v2.model.openstack_quota_table import OpenstackQuotaModel
from backend.myBluePrint.ericic_v2.model.openstack_stack_resource_table import OpenstackStackResourceModel
from backend.myBluePrint.ericic_v2.model.openstack_volume_type_table import OpenstackVolumeTypeModel
from backend.myBluePrint.ericic_v2.model.db_refresh_task import DBRefreshTaskModel
from backend.myBluePrint.ericic_v2.model.stack_table import StackModel
from backend.myBluePrint.ericic_v2.model.record_table import Record


class datacenterApiDao:
    @classmethod
    def select_instances(cls, limit, offset):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).limit(int(limit)).offset(
                int(offset)).all()
            count = db_session.query(DataCenterModel).count()
            return _data, count
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_instance(cls, dc_id):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).filter(DataCenterModel.id == dc_id).all()
            return _data
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_name_dc(cls, name):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).filter(DataCenterModel.name == name).all()
            return _data[0].name
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def delete_all_relate_info(cls, _id):
        db_session = SESSION()
        try:
            db_session.query(DataCenterModel).filter(DataCenterModel.id == _id).delete()
            db_session.query(CinderModel).filter(CinderModel.dc_id == _id).delete()
            db_session.query(CinderQuotaUsageModel).filter(CinderQuotaUsageModel.dc_id == _id).delete()
            db_session.query(NeutronPortTable).filter(NeutronPortTable.dc_id == _id).delete()
            db_session.query(NeutronVifDetailModel).filter(NeutronVifDetailModel.dc_id == _id).delete()
            db_session.query(AggregateHostRelation).filter(AggregateHostRelation.dc_id == _id).delete()
            db_session.query(NovaAggregateModel).filter(NovaAggregateModel.dc_id == _id).delete()
            db_session.query(NovaFlavorModel).filter(NovaFlavorModel.dc_id == _id).delete()
            db_session.query(NovaServiceModel).filter(NovaServiceModel.dc_id == _id).delete()
            db_session.query(NovaModel).filter(NovaModel.dc_id == _id).delete()
            db_session.query(OpenstackHypervisorStatsModel).filter(OpenstackHypervisorStatsModel.dc_id == _id).delete()
            db_session.query(OpenstackProjectModel).filter(OpenstackProjectModel.dc_id == _id).delete()
            db_session.query(OpenstackQuotaModel).filter(OpenstackQuotaModel.dc_id == _id).delete()
            db_session.query(OpenstackStackResourceModel).filter(OpenstackStackResourceModel.dc_id == _id).delete()
            db_session.query(OpenstackVolumeTypeModel).filter(OpenstackVolumeTypeModel.dc_id == _id).delete()
            db_session.query(StackModel).filter(StackModel.dc_id == _id).delete()
            db_session.query(DBRefreshTaskModel).filter(DBRefreshTaskModel.dc_id == _id).delete()
            db_session.query(Record).filter(Record.cid == _id).delete()
            celery_app.send_task('optimus_executor.method_view.record_delete', args=(_id,),
                                 countdown=MONGO_TIMEOUT / 1000 + 1)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise e
        finally:
            db_session.close()

    @classmethod
    def add_data_center(cls, dc_entity):
        db_session = SESSION()
        try:
            dc_id = dc_entity.id
            db_session.add(dc_entity)
            dynamic_task = DBRefreshTaskModel('%s:%s' % (dc_id, DYNAMIC_REFRESH), DYNAMIC_REFRESH, 30 * 60, dc_id)
            static_task = DBRefreshTaskModel('%s:%s' % (dc_id, STATIC_REFRESH), STATIC_REFRESH, 60 * 60, dc_id)
            db_session.add_all([dynamic_task, static_task])
            db_session.commit()
        except IntegrityError:
            db_session.rollback()
            raise MyRuntimeError('Duplicate name', 400)
        except Exception as e:
            db_session.rollback()
            BDLog.error(e)
            raise e
        finally:
            db_session.close()
