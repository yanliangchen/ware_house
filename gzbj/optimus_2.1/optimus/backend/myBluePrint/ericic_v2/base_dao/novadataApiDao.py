from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic_v2.model.nova_flavor_host_view import nova_flavor_host_View
from backend.myBluePrint.ericic_v2.model.cinder_list_table import CinderModel
from backend.myBluePrint.ericic_v2.model.neutron_port_table import NeutronPortTable
from backend.myBluePrint.ericic_v2.model.openstack_stack_resource_table import OpenstackStackResourceModel
from sqlalchemy import and_


class novadataApiDao:

    @classmethod
    def select_nova_data(cls, dc_id, sort, order, query, filter, limit, offset):
        db_session = SESSION()
        try:
            _filter = and_(nova_flavor_host_View.n_dc_id == dc_id)
            _order = nova_flavor_host_View.n_timestamp.desc()
            if query == 'nova_name':
                _filter = and_(nova_flavor_host_View.n_dc_id == dc_id,
                               nova_flavor_host_View.n_name.like('%{nova_name}%'.format(nova_name=filter)))
            elif query == 'nova_status':
                _filter = and_(nova_flavor_host_View.n_dc_id == dc_id,
                               nova_flavor_host_View.n_task_state.like('%{nova_status}%'.format(nova_status=filter)))
            elif query == 'nova_host':
                _filter = and_(nova_flavor_host_View.n_dc_id == dc_id,
                               nova_flavor_host_View.n_host.like('%{nova_host}%'.format(nova_host=filter)))
            elif query == 'nova_tenant':
                _filter = and_(nova_flavor_host_View.n_dc_id == dc_id,
                               nova_flavor_host_View.t_name.like('%{nova_tenant}%'.format(nova_tenant=filter)))
            if sort == 'memory':

                if order == 'asc':

                    _order = nova_flavor_host_View.f_memory_mib.asc()
                else:
                    _order = nova_flavor_host_View.f_memory_mib.desc()

            elif sort == 'disk':
                if order == 'asc':

                    _order = nova_flavor_host_View.f_disk.asc()
                else:
                    _order = nova_flavor_host_View.f_disk.desc()


            elif sort == 'vcpu':
                if order == 'asc':
                    _order = nova_flavor_host_View.f_vcpus.asc()
                else:
                    _order = nova_flavor_host_View.f_vcpus.desc()


            elif sort == 'time':
                if order == 'asc':
                    _order = nova_flavor_host_View.n_created.asc()
                else:
                    _order = nova_flavor_host_View.n_created.desc()

            nova_data = db_session.query(nova_flavor_host_View).filter(_filter).order_by(
                _order).limit(
                int(limit)).offset(
                int(offset)).all()
            volume_data = db_session.query(CinderModel).filter(CinderModel.dc_id == dc_id).all()
            network_data = db_session.query(NeutronPortTable).filter(NeutronPortTable.dc_id == dc_id).all()

            count = db_session.query(nova_flavor_host_View).filter(_filter).count()

            return nova_data, volume_data, network_data, count

        except Exception as e:
            BDLog.error(e)
            raise e
        finally:
            db_session.close()

    @classmethod
    def query_stack_resource_id(cls, dc_id, filter):
        db_session = SESSION()
        try:
            resource_data = db_session.query(OpenstackStackResourceModel).filter(and_(
                OpenstackStackResourceModel.dc_id == dc_id,
                OpenstackStackResourceModel.stack_id.like('%{stack_id}%'.format(stack_id=filter)),
                OpenstackStackResourceModel.resource_type == 'OS::Nova::Server')).all()
            resource_id_list = []
            for every_resource_data in resource_data:
                resource_id_list.append(every_resource_data.id)
            return resource_id_list
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def query_nova_in_resource_id(cls, dc_id, resource_id_list, limit, offset, sort, order):
        db_session = SESSION()
        try:
            _filter = and_(nova_flavor_host_View.n_dc_id == dc_id,
                           nova_flavor_host_View.n_id.in_(
                               resource_id_list))

            if sort == 'vcpu':
                if order == 'asc':

                    _order = nova_flavor_host_View.f_vcpus.asc()
                else:
                    _order = nova_flavor_host_View.f_vcpus.desc()
            elif sort == 'time':
                if order == 'asc':

                    _order = nova_flavor_host_View.n_timestamp.asc()
                else:
                    _order = nova_flavor_host_View.n_timestamp.desc()
            elif sort == 'memory':

                if order == 'asc':

                    _order = nova_flavor_host_View.f_memory_mib.asc()
                else:
                    _order = nova_flavor_host_View.f_memory_mib.desc()
            elif sort == 'disk':
                if order == 'asc':

                    _order = nova_flavor_host_View.f_disk.asc()
                else:
                    _order = nova_flavor_host_View.f_disk.desc()
            resource_data = db_session.query(nova_flavor_host_View).filter(_filter).limit(
                int(limit)).offset(
                int(offset)).all()
            volume_data = db_session.query(CinderModel).filter(CinderModel.dc_id == dc_id).all()
            network_data = db_session.query(NeutronPortTable).filter(NeutronPortTable.dc_id == dc_id).all()
            count = db_session.query(nova_flavor_host_View).filter(_filter).count()
            return resource_data, volume_data, network_data, count
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()
