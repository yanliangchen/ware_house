from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.openstack_project_table import OpenstackProjectModel
from backend.myBluePrint.ericic_v2.model.stack_table import StackModel

from backend.myBluePrint.ericic_v2.model.nova_aggregate_host_relation_table import AggregateHostRelation
from backend.myBluePrint.ericic_v2.common.model_to_dict import Model_To_Dict


class ConfigDataApiDao:
    @classmethod
    def select_tenants(cls, dc_id):
        db_session = SESSION()
        try:
            tenants_data = db_session.query(OpenstackProjectModel).filter(OpenstackProjectModel.dc_id == dc_id).all()
            data_dict = Model_To_Dict.model_to_dict(tenants_data)
            dup_dict = dict()
            for item in data_dict:
                id = item['id']
                dup_dict[id] = item
            response = list()
            for item in data_dict:
                name = item['name']
                _id = name.split('-')[0]
                if _id in dup_dict:
                    pass
                else:
                    response.append(item)
            tenants_data_list = []
            for every_tenant in response:
                tenants_data_dict = {}
                tenants_data_dict['tenant_id'] = every_tenant['id']
                tenants_data_dict['tenant_name'] = every_tenant['name']
                tenants_data_list.append(tenants_data_dict)
            return tenants_data_list

        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_stacks(cls, dc_id):
        db_session = SESSION()
        try:

            stacks_data = db_session.query(StackModel).filter(StackModel.dc_id == dc_id).all()
            stacks_data_list = []
            for every_stack in stacks_data:
                stacks_data_dict = {}
                stacks_data_dict['stack_id'] = every_stack.id
                stacks_data_dict['stack_name'] = every_stack.name
                stacks_data_list.append(stacks_data_dict)
            return stacks_data_list



        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()



    @classmethod
    def select_host_ha(cls, dc_id):
        db_session = SESSION()
        try:
            host_az_data = db_session.query(AggregateHostRelation).filter(AggregateHostRelation.dc_id == dc_id).all()
            az_list = []
            for every_host_az in host_az_data:
                az_dict = {}
                az_dict['aggregate_name'] = every_host_az.aggregate_name
                az_list.append(az_dict)
            return az_list

        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_host_az(cls, dc_id):
        db_session = SESSION()
        try:
            host_az_data = db_session.query(AggregateHostRelation).filter(AggregateHostRelation.dc_id == dc_id).all()
            az_list = []
            for every_host_az in host_az_data:
                az_dict = {}

                az_dict['availability_zone'] = every_host_az.availability_zone
                az_list.append(az_dict)
            return az_list

        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()
