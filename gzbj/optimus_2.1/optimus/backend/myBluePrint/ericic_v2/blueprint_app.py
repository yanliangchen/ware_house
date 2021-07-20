from flask import Blueprint
from backend.myBluePrint.ericic_v2.api.v1.scheduler_task_history_view import SchedulerTaskHistoryView
from backend.myBluePrint.ericic_v2.api.v1.scheduler_task_view import SchedulerTaskView
from backend.myBluePrint.ericic_v2.api.v1.infrastructure_view import InfrastructureView
from backend.myBluePrint.ericic_v2.api.v1.data_center_view import DataCenterView
from backend.myBluePrint.ericic_v2.api.v1.conn_state_view import ConnectStatusView
from backend.myBluePrint.ericic_v2.api.v1.novaDataView import NovaData
from backend.myBluePrint.ericic_v2.api.v1.configDataView import ConfigData
from backend.myBluePrint.ericic_v2.api.v1.infra_resource_view import InfraResourceView
from backend.myBluePrint.ericic_v2.api.v1.cpu_layout_view import CpuLayoutView
from backend.myBluePrint.ericic_v2.api.v1.interface_driver import InterfaceDriverView
from backend.myBluePrint.ericic_v2.api.v1.network_port_view import NetworkPortView
from backend.myBluePrint.ericic_v2.api.v1.tenant_quota_view import TenantQuotaView
from backend.myBluePrint.ericic_v2.api.v1.nova_service_detail_view import NovaServiceDetailsView
# from backend.myBluePrint.ericic_v2.api.v1.hostDataView import HostData
from backend.myBluePrint.ericic_v2.api.v1.host_view import HostView
from backend.myBluePrint.ericic_v2.api.v1.hostconfigDataView import HostConfigData
from backend.myBluePrint.ericic_v2.api.v1.recordView import RecordView
from backend.myBluePrint.ericic_v2.api.v1.downloadView import DownloadView

ericic_bp = Blueprint('ericic', __name__, url_prefix='/api/ericic/v2.1/')

ericic_bp.add_url_rule('scheduler/task', view_func=SchedulerTaskView.as_view('SchedulerTaskView'))
ericic_bp.add_url_rule('scheduler/task/history', view_func=SchedulerTaskHistoryView.as_view('SchedulerTaskHistoryView'))
ericic_bp.add_url_rule('infrastructure', view_func=InfrastructureView.as_view('InfrastructureView'))
ericic_bp.add_url_rule('data_center', view_func=DataCenterView.as_view('DataCenterView'))
ericic_bp.add_url_rule('connect_status', view_func=ConnectStatusView.as_view('ConnectStatusView'))
ericic_bp.add_url_rule('nova_data', view_func=NovaData.as_view('NovaData'))
ericic_bp.add_url_rule('config_data', view_func=ConfigData.as_view('ConfigData'))
ericic_bp.add_url_rule('host_data', view_func=HostView.as_view('HostView'))
ericic_bp.add_url_rule('host_config_data', view_func=HostConfigData.as_view('HostConfigData'))
ericic_bp.add_url_rule('<string:cid>/infra_resource/<string:hid>', view_func=InfraResourceView.as_view('InfraResourceView'))
ericic_bp.add_url_rule('<string:cid>/cpu_layout/<string:hid>', view_func=CpuLayoutView.as_view('CpuLayoutView'))
ericic_bp.add_url_rule('<string:cid>/interface_driver/<string:hid>', view_func=InterfaceDriverView.as_view('InterfaceDriverView'))
ericic_bp.add_url_rule('<string:cid>/<string:vid>/<string:uid>/network_port', view_func=NetworkPortView.as_view('NetworkPortView'))
ericic_bp.add_url_rule('<string:cid>/<string:tid>/tenant_quota', view_func=TenantQuotaView.as_view('TenantQuotaView'))
ericic_bp.add_url_rule('<string:cid>/nova_service/<any(down,up):status>', view_func=NovaServiceDetailsView.as_view('NovaServiceDetailsView'))
ericic_bp.add_url_rule('record', view_func=RecordView.as_view('RecordView'))
ericic_bp.add_url_rule('record/download', view_func=DownloadView.as_view('DownloadView'))
