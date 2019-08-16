from terrascript import Resource
class alicloud_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_instance', _label, **kwargs)
instance = alicloud_instance

class alicloud_ram_role_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_role_attachment', _label, **kwargs)
ram_role_attachment = alicloud_ram_role_attachment

class alicloud_disk(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_disk', _label, **kwargs)
disk = alicloud_disk

class alicloud_disk_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_disk_attachment', _label, **kwargs)
disk_attachment = alicloud_disk_attachment

class alicloud_network_interface(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_network_interface', _label, **kwargs)
network_interface = alicloud_network_interface

class alicloud_network_interface_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_network_interface_attachment', _label, **kwargs)
network_interface_attachment = alicloud_network_interface_attachment

class alicloud_snapshot(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_snapshot', _label, **kwargs)
snapshot = alicloud_snapshot

class alicloud_snapshot_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_snapshot_policy', _label, **kwargs)
snapshot_policy = alicloud_snapshot_policy

class alicloud_launch_template(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_launch_template', _label, **kwargs)
launch_template = alicloud_launch_template

class alicloud_security_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_security_group', _label, **kwargs)
security_group = alicloud_security_group

class alicloud_security_group_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_security_group_rule', _label, **kwargs)
security_group_rule = alicloud_security_group_rule

class alicloud_db_database(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_database', _label, **kwargs)
db_database = alicloud_db_database

class alicloud_db_account(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_account', _label, **kwargs)
db_account = alicloud_db_account

class alicloud_db_account_privilege(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_account_privilege', _label, **kwargs)
db_account_privilege = alicloud_db_account_privilege

class alicloud_db_backup_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_backup_policy', _label, **kwargs)
db_backup_policy = alicloud_db_backup_policy

class alicloud_db_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_connection', _label, **kwargs)
db_connection = alicloud_db_connection

class alicloud_db_read_write_splitting_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_read_write_splitting_connection', _label, **kwargs)
db_read_write_splitting_connection = alicloud_db_read_write_splitting_connection

class alicloud_db_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_instance', _label, **kwargs)
db_instance = alicloud_db_instance

class alicloud_mongodb_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_mongodb_instance', _label, **kwargs)
mongodb_instance = alicloud_mongodb_instance

class alicloud_mongodb_sharding_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_mongodb_sharding_instance', _label, **kwargs)
mongodb_sharding_instance = alicloud_mongodb_sharding_instance

class alicloud_gpdb_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_gpdb_instance', _label, **kwargs)
gpdb_instance = alicloud_gpdb_instance

class alicloud_gpdb_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_gpdb_connection', _label, **kwargs)
gpdb_connection = alicloud_gpdb_connection

class alicloud_db_readonly_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_db_readonly_instance', _label, **kwargs)
db_readonly_instance = alicloud_db_readonly_instance

class alicloud_ess_scaling_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_scaling_group', _label, **kwargs)
ess_scaling_group = alicloud_ess_scaling_group

class alicloud_ess_scaling_configuration(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_scaling_configuration', _label, **kwargs)
ess_scaling_configuration = alicloud_ess_scaling_configuration

class alicloud_ess_scaling_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_scaling_rule', _label, **kwargs)
ess_scaling_rule = alicloud_ess_scaling_rule

class alicloud_ess_schedule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_schedule', _label, **kwargs)
ess_schedule = alicloud_ess_schedule

class alicloud_ess_scheduled_task(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_scheduled_task', _label, **kwargs)
ess_scheduled_task = alicloud_ess_scheduled_task

class alicloud_ess_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_attachment', _label, **kwargs)
ess_attachment = alicloud_ess_attachment

class alicloud_ess_lifecycle_hook(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_lifecycle_hook', _label, **kwargs)
ess_lifecycle_hook = alicloud_ess_lifecycle_hook

class alicloud_ess_alarm(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_alarm', _label, **kwargs)
ess_alarm = alicloud_ess_alarm

class alicloud_ess_scalinggroup_vserver_groups(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ess_scalinggroup_vserver_groups', _label, **kwargs)
ess_scalinggroup_vserver_groups = alicloud_ess_scalinggroup_vserver_groups

class alicloud_vpc(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_vpc', _label, **kwargs)
vpc = alicloud_vpc

class alicloud_nat_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_nat_gateway', _label, **kwargs)
nat_gateway = alicloud_nat_gateway

class alicloud_nas_file_system(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_nas_file_system', _label, **kwargs)
nas_file_system = alicloud_nas_file_system

class alicloud_nas_mount_target(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_nas_mount_target', _label, **kwargs)
nas_mount_target = alicloud_nas_mount_target

class alicloud_nas_access_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_nas_access_group', _label, **kwargs)
nas_access_group = alicloud_nas_access_group

class alicloud_nas_access_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_nas_access_rule', _label, **kwargs)
nas_access_rule = alicloud_nas_access_rule

class alicloud_subnet(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_subnet', _label, **kwargs)
subnet = alicloud_subnet

class alicloud_vswitch(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_vswitch', _label, **kwargs)
vswitch = alicloud_vswitch

class alicloud_route_entry(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_route_entry', _label, **kwargs)
route_entry = alicloud_route_entry

class alicloud_route_table(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_route_table', _label, **kwargs)
route_table = alicloud_route_table

class alicloud_route_table_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_route_table_attachment', _label, **kwargs)
route_table_attachment = alicloud_route_table_attachment

class alicloud_snat_entry(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_snat_entry', _label, **kwargs)
snat_entry = alicloud_snat_entry

class alicloud_forward_entry(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_forward_entry', _label, **kwargs)
forward_entry = alicloud_forward_entry

class alicloud_eip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_eip', _label, **kwargs)
eip = alicloud_eip

class alicloud_eip_association(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_eip_association', _label, **kwargs)
eip_association = alicloud_eip_association

class alicloud_slb(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb', _label, **kwargs)
slb = alicloud_slb

class alicloud_slb_listener(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_listener', _label, **kwargs)
slb_listener = alicloud_slb_listener

class alicloud_slb_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_attachment', _label, **kwargs)
slb_attachment = alicloud_slb_attachment

class alicloud_slb_backend_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_backend_server', _label, **kwargs)
slb_backend_server = alicloud_slb_backend_server

class alicloud_slb_server_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_server_group', _label, **kwargs)
slb_server_group = alicloud_slb_server_group

class alicloud_slb_rule(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_rule', _label, **kwargs)
slb_rule = alicloud_slb_rule

class alicloud_slb_acl(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_acl', _label, **kwargs)
slb_acl = alicloud_slb_acl

class alicloud_slb_ca_certificate(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_ca_certificate', _label, **kwargs)
slb_ca_certificate = alicloud_slb_ca_certificate

class alicloud_slb_server_certificate(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_slb_server_certificate', _label, **kwargs)
slb_server_certificate = alicloud_slb_server_certificate

class alicloud_oss_bucket(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_oss_bucket', _label, **kwargs)
oss_bucket = alicloud_oss_bucket

class alicloud_oss_bucket_object(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_oss_bucket_object', _label, **kwargs)
oss_bucket_object = alicloud_oss_bucket_object

class alicloud_ons_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ons_instance', _label, **kwargs)
ons_instance = alicloud_ons_instance

class alicloud_ons_topic(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ons_topic', _label, **kwargs)
ons_topic = alicloud_ons_topic

class alicloud_ons_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ons_group', _label, **kwargs)
ons_group = alicloud_ons_group

class alicloud_dns_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_dns_record', _label, **kwargs)
dns_record = alicloud_dns_record

class alicloud_dns(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_dns', _label, **kwargs)
dns = alicloud_dns

class alicloud_dns_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_dns_group', _label, **kwargs)
dns_group = alicloud_dns_group

class alicloud_key_pair(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_key_pair', _label, **kwargs)
key_pair = alicloud_key_pair

class alicloud_key_pair_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_key_pair_attachment', _label, **kwargs)
key_pair_attachment = alicloud_key_pair_attachment

class alicloud_kms_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_kms_key', _label, **kwargs)
kms_key = alicloud_kms_key

class alicloud_ram_user(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_user', _label, **kwargs)
ram_user = alicloud_ram_user

class alicloud_ram_account_password_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_account_password_policy', _label, **kwargs)
ram_account_password_policy = alicloud_ram_account_password_policy

class alicloud_ram_access_key(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_access_key', _label, **kwargs)
ram_access_key = alicloud_ram_access_key

class alicloud_ram_login_profile(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_login_profile', _label, **kwargs)
ram_login_profile = alicloud_ram_login_profile

class alicloud_ram_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_group', _label, **kwargs)
ram_group = alicloud_ram_group

class alicloud_ram_role(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_role', _label, **kwargs)
ram_role = alicloud_ram_role

class alicloud_ram_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_policy', _label, **kwargs)
ram_policy = alicloud_ram_policy

class alicloud_ram_alias(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_alias', _label, **kwargs)
ram_alias = alicloud_ram_alias

class alicloud_ram_account_alias(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_account_alias', _label, **kwargs)
ram_account_alias = alicloud_ram_account_alias

class alicloud_ram_group_membership(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_group_membership', _label, **kwargs)
ram_group_membership = alicloud_ram_group_membership

class alicloud_ram_user_policy_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_user_policy_attachment', _label, **kwargs)
ram_user_policy_attachment = alicloud_ram_user_policy_attachment

class alicloud_ram_role_policy_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_role_policy_attachment', _label, **kwargs)
ram_role_policy_attachment = alicloud_ram_role_policy_attachment

class alicloud_ram_group_policy_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ram_group_policy_attachment', _label, **kwargs)
ram_group_policy_attachment = alicloud_ram_group_policy_attachment

class alicloud_container_cluster(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_container_cluster', _label, **kwargs)
container_cluster = alicloud_container_cluster

class alicloud_cs_application(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cs_application', _label, **kwargs)
cs_application = alicloud_cs_application

class alicloud_cs_swarm(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cs_swarm', _label, **kwargs)
cs_swarm = alicloud_cs_swarm

class alicloud_cs_kubernetes(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cs_kubernetes', _label, **kwargs)
cs_kubernetes = alicloud_cs_kubernetes

class alicloud_cs_managed_kubernetes(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cs_managed_kubernetes', _label, **kwargs)
cs_managed_kubernetes = alicloud_cs_managed_kubernetes

class alicloud_cr_namespace(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cr_namespace', _label, **kwargs)
cr_namespace = alicloud_cr_namespace

class alicloud_cr_repo(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cr_repo', _label, **kwargs)
cr_repo = alicloud_cr_repo

class alicloud_cdn_domain(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cdn_domain', _label, **kwargs)
cdn_domain = alicloud_cdn_domain

class alicloud_cdn_domain_new(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cdn_domain_new', _label, **kwargs)
cdn_domain_new = alicloud_cdn_domain_new

class alicloud_cdn_domain_config(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cdn_domain_config', _label, **kwargs)
cdn_domain_config = alicloud_cdn_domain_config

class alicloud_router_interface(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_router_interface', _label, **kwargs)
router_interface = alicloud_router_interface

class alicloud_router_interface_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_router_interface_connection', _label, **kwargs)
router_interface_connection = alicloud_router_interface_connection

class alicloud_ots_table(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ots_table', _label, **kwargs)
ots_table = alicloud_ots_table

class alicloud_ots_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ots_instance', _label, **kwargs)
ots_instance = alicloud_ots_instance

class alicloud_ots_instance_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ots_instance_attachment', _label, **kwargs)
ots_instance_attachment = alicloud_ots_instance_attachment

class alicloud_cms_alarm(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cms_alarm', _label, **kwargs)
cms_alarm = alicloud_cms_alarm

class alicloud_pvtz_zone(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_pvtz_zone', _label, **kwargs)
pvtz_zone = alicloud_pvtz_zone

class alicloud_pvtz_zone_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_pvtz_zone_attachment', _label, **kwargs)
pvtz_zone_attachment = alicloud_pvtz_zone_attachment

class alicloud_pvtz_zone_record(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_pvtz_zone_record', _label, **kwargs)
pvtz_zone_record = alicloud_pvtz_zone_record

class alicloud_log_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_log_project', _label, **kwargs)
log_project = alicloud_log_project

class alicloud_log_store(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_log_store', _label, **kwargs)
log_store = alicloud_log_store

class alicloud_log_store_index(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_log_store_index', _label, **kwargs)
log_store_index = alicloud_log_store_index

class alicloud_log_machine_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_log_machine_group', _label, **kwargs)
log_machine_group = alicloud_log_machine_group

class alicloud_logtail_config(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_logtail_config', _label, **kwargs)
logtail_config = alicloud_logtail_config

class alicloud_logtail_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_logtail_attachment', _label, **kwargs)
logtail_attachment = alicloud_logtail_attachment

class alicloud_fc_service(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_fc_service', _label, **kwargs)
fc_service = alicloud_fc_service

class alicloud_fc_function(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_fc_function', _label, **kwargs)
fc_function = alicloud_fc_function

class alicloud_fc_trigger(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_fc_trigger', _label, **kwargs)
fc_trigger = alicloud_fc_trigger

class alicloud_vpn_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_vpn_gateway', _label, **kwargs)
vpn_gateway = alicloud_vpn_gateway

class alicloud_vpn_customer_gateway(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_vpn_customer_gateway', _label, **kwargs)
vpn_customer_gateway = alicloud_vpn_customer_gateway

class alicloud_vpn_connection(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_vpn_connection', _label, **kwargs)
vpn_connection = alicloud_vpn_connection

class alicloud_ssl_vpn_server(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ssl_vpn_server', _label, **kwargs)
ssl_vpn_server = alicloud_ssl_vpn_server

class alicloud_ssl_vpn_client_cert(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ssl_vpn_client_cert', _label, **kwargs)
ssl_vpn_client_cert = alicloud_ssl_vpn_client_cert

class alicloud_cen_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_instance', _label, **kwargs)
cen_instance = alicloud_cen_instance

class alicloud_cen_instance_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_instance_attachment', _label, **kwargs)
cen_instance_attachment = alicloud_cen_instance_attachment

class alicloud_cen_bandwidth_package(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_bandwidth_package', _label, **kwargs)
cen_bandwidth_package = alicloud_cen_bandwidth_package

class alicloud_cen_bandwidth_package_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_bandwidth_package_attachment', _label, **kwargs)
cen_bandwidth_package_attachment = alicloud_cen_bandwidth_package_attachment

class alicloud_cen_bandwidth_limit(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_bandwidth_limit', _label, **kwargs)
cen_bandwidth_limit = alicloud_cen_bandwidth_limit

class alicloud_cen_route_entry(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_route_entry', _label, **kwargs)
cen_route_entry = alicloud_cen_route_entry

class alicloud_cen_instance_grant(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cen_instance_grant', _label, **kwargs)
cen_instance_grant = alicloud_cen_instance_grant

class alicloud_kvstore_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_kvstore_instance', _label, **kwargs)
kvstore_instance = alicloud_kvstore_instance

class alicloud_kvstore_backup_policy(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_kvstore_backup_policy', _label, **kwargs)
kvstore_backup_policy = alicloud_kvstore_backup_policy

class alicloud_datahub_project(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_datahub_project', _label, **kwargs)
datahub_project = alicloud_datahub_project

class alicloud_datahub_subscription(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_datahub_subscription', _label, **kwargs)
datahub_subscription = alicloud_datahub_subscription

class alicloud_datahub_topic(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_datahub_topic', _label, **kwargs)
datahub_topic = alicloud_datahub_topic

class alicloud_mns_queue(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_mns_queue', _label, **kwargs)
mns_queue = alicloud_mns_queue

class alicloud_mns_topic(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_mns_topic', _label, **kwargs)
mns_topic = alicloud_mns_topic

class alicloud_havip(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_havip', _label, **kwargs)
havip = alicloud_havip

class alicloud_mns_topic_subscription(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_mns_topic_subscription', _label, **kwargs)
mns_topic_subscription = alicloud_mns_topic_subscription

class alicloud_havip_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_havip_attachment', _label, **kwargs)
havip_attachment = alicloud_havip_attachment

class alicloud_api_gateway_api(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_api_gateway_api', _label, **kwargs)
api_gateway_api = alicloud_api_gateway_api

class alicloud_api_gateway_group(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_api_gateway_group', _label, **kwargs)
api_gateway_group = alicloud_api_gateway_group

class alicloud_api_gateway_app(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_api_gateway_app', _label, **kwargs)
api_gateway_app = alicloud_api_gateway_app

class alicloud_api_gateway_app_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_api_gateway_app_attachment', _label, **kwargs)
api_gateway_app_attachment = alicloud_api_gateway_app_attachment

class alicloud_api_gateway_vpc_access(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_api_gateway_vpc_access', _label, **kwargs)
api_gateway_vpc_access = alicloud_api_gateway_vpc_access

class alicloud_common_bandwidth_package(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_common_bandwidth_package', _label, **kwargs)
common_bandwidth_package = alicloud_common_bandwidth_package

class alicloud_common_bandwidth_package_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_common_bandwidth_package_attachment', _label, **kwargs)
common_bandwidth_package_attachment = alicloud_common_bandwidth_package_attachment

class alicloud_drds_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_drds_instance', _label, **kwargs)
drds_instance = alicloud_drds_instance

class alicloud_elasticsearch_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_elasticsearch_instance', _label, **kwargs)
elasticsearch_instance = alicloud_elasticsearch_instance

class alicloud_actiontrail(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_actiontrail', _label, **kwargs)
actiontrail = alicloud_actiontrail

class alicloud_cas_certificate(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_cas_certificate', _label, **kwargs)
cas_certificate = alicloud_cas_certificate

class alicloud_ddoscoo_instance(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_ddoscoo_instance', _label, **kwargs)
ddoscoo_instance = alicloud_ddoscoo_instance

class alicloud_network_acl(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_network_acl', _label, **kwargs)
network_acl = alicloud_network_acl

class alicloud_network_acl_attachment(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_network_acl_attachment', _label, **kwargs)
network_acl_attachment = alicloud_network_acl_attachment

class alicloud_network_acl_entries(Resource):
    def __init__(self, _label, **kwargs): super().__init__('alicloud_network_acl_entries', _label, **kwargs)
network_acl_entries = alicloud_network_acl_entries

