from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION

from backend.myBluePrint.ericic_v2.model.nova_service_table import NovaServiceModel
from backend.myBluePrint.ericic_v2.model.nova_aggregate_host_relation_table import AggregateHostRelation
from backend.myBluePrint.ericic_v2.model.nova_flavor_host_view import nova_flavor_host_View
from sqlalchemy import and_


class hostdataApiDao:

    @classmethod
    def select_host_data(cls, dc_id, query, filter, limit, offset, order, sort):

        db_session = SESSION()
        try:
            count = db_session.query(NovaServiceModel).filter(NovaServiceModel.dc_id == dc_id).count()
            sql = \
                "select * from " \
                "nova_service_table, (select count(*) as vm_amount, n_host from nova_flavor_host_view group by n_host) as t2 " \
                "where nova_service_table.host = t2.n_host{format_filter}{format_sql} limit {limit} offset {offset};"

            if sort == 'vm_amount':
                if order == 'desc':
                    format_order = " order by vm_amount desc"
                elif order == 'asc':
                    format_order = " order by vm_amount asc"
                else:
                    format_order = ""
            else:
                format_order = ""

            if query == 'state':
                format_filter = " and nova_service_table.state like '%s'" % filter

            elif query == 'host':
                format_filter = " and nova_service_table.host like '%s' " % filter

            else:
                format_filter = ""

            sql = sql.format(format_sql=format_order, limit=limit, offset=offset, format_filter=format_filter)
            cursor = db_session.execute(sql)
            service_data = cursor.fetchall()
            service_data = [dict(i) for i in service_data]
            _filter = and_(NovaServiceModel.dc_id == dc_id)

            if query == 'ha':
                _filter = and_(AggregateHostRelation.dc_id == dc_id,
                               AggregateHostRelation.aggregate_name.like('%{ha}%'.format(ha=filter)))

                hz_data = db_session.query(AggregateHostRelation).filter(_filter).all()
                nova_data = db_session.query(nova_flavor_host_View).filter(nova_flavor_host_View.n_dc_id == dc_id).all()
                return service_data, hz_data, nova_data, count
            elif query == 'az':
                _filter = and_(AggregateHostRelation.dc_id == dc_id,
                               AggregateHostRelation.availability_zone.like('%{az}%'.format(az=filter)))

                hz_data = db_session.query(AggregateHostRelation).filter(_filter).all()
                nova_data = db_session.query(nova_flavor_host_View).filter(nova_flavor_host_View.n_dc_id == dc_id).all()
                return service_data, hz_data, nova_data, count

            else:
                hz_data = db_session.query(AggregateHostRelation).filter(AggregateHostRelation.dc_id == dc_id).all()
                nova_data = db_session.query(nova_flavor_host_View).filter(nova_flavor_host_View.n_dc_id == dc_id).all()
                return service_data, hz_data, nova_data, count


        except Exception as e:
            BDLog.error(e)
            raise  e
        finally:
            db_session.close()
