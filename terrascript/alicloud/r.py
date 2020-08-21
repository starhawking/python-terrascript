# terrascript/alicloud/r.py
import terrascript


class alicloud_instance(terrascript.Resource):
    pass


class alicloud_image(terrascript.Resource):
    pass


class alicloud_reserved_instance(terrascript.Resource):
    pass


class alicloud_copy_image(terrascript.Resource):
    pass


class alicloud_image_export(terrascript.Resource):
    pass


class alicloud_image_copy(terrascript.Resource):
    pass


class alicloud_image_import(terrascript.Resource):
    pass


class alicloud_image_share_permission(terrascript.Resource):
    pass


class alicloud_ram_role_attachment(terrascript.Resource):
    pass


class alicloud_disk(terrascript.Resource):
    pass


class alicloud_disk_attachment(terrascript.Resource):
    pass


class alicloud_network_interface(terrascript.Resource):
    pass


class alicloud_network_interface_attachment(terrascript.Resource):
    pass


class alicloud_snapshot(terrascript.Resource):
    pass


class alicloud_snapshot_policy(terrascript.Resource):
    pass


class alicloud_launch_template(terrascript.Resource):
    pass


class alicloud_security_group(terrascript.Resource):
    pass


class alicloud_security_group_rule(terrascript.Resource):
    pass


class alicloud_db_database(terrascript.Resource):
    pass


class alicloud_db_account(terrascript.Resource):
    pass


class alicloud_db_account_privilege(terrascript.Resource):
    pass


class alicloud_db_backup_policy(terrascript.Resource):
    pass


class alicloud_db_connection(terrascript.Resource):
    pass


class alicloud_db_read_write_splitting_connection(terrascript.Resource):
    pass


class alicloud_db_instance(terrascript.Resource):
    pass


class alicloud_mongodb_instance(terrascript.Resource):
    pass


class alicloud_mongodb_sharding_instance(terrascript.Resource):
    pass


class alicloud_gpdb_instance(terrascript.Resource):
    pass


class alicloud_gpdb_connection(terrascript.Resource):
    pass


class alicloud_db_readonly_instance(terrascript.Resource):
    pass


class alicloud_auto_provisioning_group(terrascript.Resource):
    pass


class alicloud_ess_scaling_group(terrascript.Resource):
    pass


class alicloud_ess_scaling_configuration(terrascript.Resource):
    pass


class alicloud_ess_scaling_rule(terrascript.Resource):
    pass


class alicloud_ess_schedule(terrascript.Resource):
    pass


class alicloud_ess_scheduled_task(terrascript.Resource):
    pass


class alicloud_ess_attachment(terrascript.Resource):
    pass


class alicloud_ess_lifecycle_hook(terrascript.Resource):
    pass


class alicloud_ess_notification(terrascript.Resource):
    pass


class alicloud_ess_alarm(terrascript.Resource):
    pass


class alicloud_ess_scalinggroup_vserver_groups(terrascript.Resource):
    pass


class alicloud_vpc(terrascript.Resource):
    pass


class alicloud_nat_gateway(terrascript.Resource):
    pass


class alicloud_nas_file_system(terrascript.Resource):
    pass


class alicloud_nas_mount_target(terrascript.Resource):
    pass


class alicloud_nas_access_group(terrascript.Resource):
    pass


class alicloud_nas_access_rule(terrascript.Resource):
    pass


class alicloud_subnet(terrascript.Resource):
    pass


class alicloud_vswitch(terrascript.Resource):
    pass


class alicloud_route_entry(terrascript.Resource):
    pass


class alicloud_route_table(terrascript.Resource):
    pass


class alicloud_route_table_attachment(terrascript.Resource):
    pass


class alicloud_snat_entry(terrascript.Resource):
    pass


class alicloud_forward_entry(terrascript.Resource):
    pass


class alicloud_eip(terrascript.Resource):
    pass


class alicloud_eip_association(terrascript.Resource):
    pass


class alicloud_slb(terrascript.Resource):
    pass


class alicloud_slb_listener(terrascript.Resource):
    pass


class alicloud_slb_attachment(terrascript.Resource):
    pass


class alicloud_slb_backend_server(terrascript.Resource):
    pass


class alicloud_slb_domain_extension(terrascript.Resource):
    pass


class alicloud_slb_server_group(terrascript.Resource):
    pass


class alicloud_slb_master_slave_server_group(terrascript.Resource):
    pass


class alicloud_slb_rule(terrascript.Resource):
    pass


class alicloud_slb_acl(terrascript.Resource):
    pass


class alicloud_slb_ca_certificate(terrascript.Resource):
    pass


class alicloud_slb_server_certificate(terrascript.Resource):
    pass


class alicloud_oss_bucket(terrascript.Resource):
    pass


class alicloud_oss_bucket_object(terrascript.Resource):
    pass


class alicloud_ons_instance(terrascript.Resource):
    pass


class alicloud_ons_topic(terrascript.Resource):
    pass


class alicloud_ons_group(terrascript.Resource):
    pass


class alicloud_alikafka_consumer_group(terrascript.Resource):
    pass


class alicloud_alikafka_instance(terrascript.Resource):
    pass


class alicloud_alikafka_topic(terrascript.Resource):
    pass


class alicloud_alikafka_sasl_user(terrascript.Resource):
    pass


class alicloud_alikafka_sasl_acl(terrascript.Resource):
    pass


class alicloud_dns_record(terrascript.Resource):
    pass


class alicloud_dns(terrascript.Resource):
    pass


class alicloud_dns_group(terrascript.Resource):
    pass


class alicloud_key_pair(terrascript.Resource):
    pass


class alicloud_key_pair_attachment(terrascript.Resource):
    pass


class alicloud_kms_key(terrascript.Resource):
    pass


class alicloud_kms_ciphertext(terrascript.Resource):
    pass


class alicloud_ram_user(terrascript.Resource):
    pass


class alicloud_ram_account_password_policy(terrascript.Resource):
    pass


class alicloud_ram_access_key(terrascript.Resource):
    pass


class alicloud_ram_login_profile(terrascript.Resource):
    pass


class alicloud_ram_group(terrascript.Resource):
    pass


class alicloud_ram_role(terrascript.Resource):
    pass


class alicloud_ram_policy(terrascript.Resource):
    pass


class alicloud_ram_alias(terrascript.Resource):
    pass


class alicloud_ram_account_alias(terrascript.Resource):
    pass


class alicloud_ram_group_membership(terrascript.Resource):
    pass


class alicloud_ram_user_policy_attachment(terrascript.Resource):
    pass


class alicloud_ram_role_policy_attachment(terrascript.Resource):
    pass


class alicloud_ram_group_policy_attachment(terrascript.Resource):
    pass


class alicloud_container_cluster(terrascript.Resource):
    pass


class alicloud_cs_application(terrascript.Resource):
    pass


class alicloud_cs_swarm(terrascript.Resource):
    pass


class alicloud_cs_kubernetes(terrascript.Resource):
    pass


class alicloud_cs_managed_kubernetes(terrascript.Resource):
    pass


class alicloud_cs_serverless_kubernetes(terrascript.Resource):
    pass


class alicloud_cs_kubernetes_autoscaler(terrascript.Resource):
    pass


class alicloud_cr_namespace(terrascript.Resource):
    pass


class alicloud_cr_repo(terrascript.Resource):
    pass


class alicloud_cr_ee_namespace(terrascript.Resource):
    pass


class alicloud_cr_ee_repo(terrascript.Resource):
    pass


class alicloud_cr_ee_sync_rule(terrascript.Resource):
    pass


class alicloud_cdn_domain(terrascript.Resource):
    pass


class alicloud_cdn_domain_new(terrascript.Resource):
    pass


class alicloud_cdn_domain_config(terrascript.Resource):
    pass


class alicloud_router_interface(terrascript.Resource):
    pass


class alicloud_router_interface_connection(terrascript.Resource):
    pass


class alicloud_ots_table(terrascript.Resource):
    pass


class alicloud_ots_instance(terrascript.Resource):
    pass


class alicloud_ots_instance_attachment(terrascript.Resource):
    pass


class alicloud_cms_alarm(terrascript.Resource):
    pass


class alicloud_cms_site_monitor(terrascript.Resource):
    pass


class alicloud_pvtz_zone(terrascript.Resource):
    pass


class alicloud_pvtz_zone_attachment(terrascript.Resource):
    pass


class alicloud_pvtz_zone_record(terrascript.Resource):
    pass


class alicloud_log_project(terrascript.Resource):
    pass


class alicloud_log_store(terrascript.Resource):
    pass


class alicloud_log_store_index(terrascript.Resource):
    pass


class alicloud_log_machine_group(terrascript.Resource):
    pass


class alicloud_logtail_config(terrascript.Resource):
    pass


class alicloud_logtail_attachment(terrascript.Resource):
    pass


class alicloud_log_dashboard(terrascript.Resource):
    pass


class alicloud_log_alert(terrascript.Resource):
    pass


class alicloud_log_audit(terrascript.Resource):
    pass


class alicloud_fc_service(terrascript.Resource):
    pass


class alicloud_fc_function(terrascript.Resource):
    pass


class alicloud_fc_trigger(terrascript.Resource):
    pass


class alicloud_vpn_gateway(terrascript.Resource):
    pass


class alicloud_vpn_customer_gateway(terrascript.Resource):
    pass


class alicloud_vpn_route_entry(terrascript.Resource):
    pass


class alicloud_vpn_connection(terrascript.Resource):
    pass


class alicloud_ssl_vpn_server(terrascript.Resource):
    pass


class alicloud_ssl_vpn_client_cert(terrascript.Resource):
    pass


class alicloud_cen_instance(terrascript.Resource):
    pass


class alicloud_cen_instance_attachment(terrascript.Resource):
    pass


class alicloud_cen_bandwidth_package(terrascript.Resource):
    pass


class alicloud_cen_bandwidth_package_attachment(terrascript.Resource):
    pass


class alicloud_cen_bandwidth_limit(terrascript.Resource):
    pass


class alicloud_cen_route_entry(terrascript.Resource):
    pass


class alicloud_cen_instance_grant(terrascript.Resource):
    pass


class alicloud_kvstore_instance(terrascript.Resource):
    pass


class alicloud_kvstore_backup_policy(terrascript.Resource):
    pass


class alicloud_kvstore_account(terrascript.Resource):
    pass


class alicloud_datahub_project(terrascript.Resource):
    pass


class alicloud_datahub_subscription(terrascript.Resource):
    pass


class alicloud_datahub_topic(terrascript.Resource):
    pass


class alicloud_mns_queue(terrascript.Resource):
    pass


class alicloud_mns_topic(terrascript.Resource):
    pass


class alicloud_havip(terrascript.Resource):
    pass


class alicloud_mns_topic_subscription(terrascript.Resource):
    pass


class alicloud_havip_attachment(terrascript.Resource):
    pass


class alicloud_api_gateway_api(terrascript.Resource):
    pass


class alicloud_api_gateway_group(terrascript.Resource):
    pass


class alicloud_api_gateway_app(terrascript.Resource):
    pass


class alicloud_api_gateway_app_attachment(terrascript.Resource):
    pass


class alicloud_api_gateway_vpc_access(terrascript.Resource):
    pass


class alicloud_common_bandwidth_package(terrascript.Resource):
    pass


class alicloud_common_bandwidth_package_attachment(terrascript.Resource):
    pass


class alicloud_drds_instance(terrascript.Resource):
    pass


class alicloud_elasticsearch_instance(terrascript.Resource):
    pass


class alicloud_actiontrail(terrascript.Resource):
    pass


class alicloud_cas_certificate(terrascript.Resource):
    pass


class alicloud_ddoscoo_instance(terrascript.Resource):
    pass


class alicloud_ddosbgp_instance(terrascript.Resource):
    pass


class alicloud_network_acl(terrascript.Resource):
    pass


class alicloud_network_acl_attachment(terrascript.Resource):
    pass


class alicloud_network_acl_entries(terrascript.Resource):
    pass


class alicloud_emr_cluster(terrascript.Resource):
    pass


class alicloud_cloud_connect_network(terrascript.Resource):
    pass


class alicloud_cloud_connect_network_attachment(terrascript.Resource):
    pass


class alicloud_cloud_connect_network_grant(terrascript.Resource):
    pass


class alicloud_sag_acl(terrascript.Resource):
    pass


class alicloud_sag_acl_rule(terrascript.Resource):
    pass


class alicloud_sag_qos(terrascript.Resource):
    pass


class alicloud_sag_qos_policy(terrascript.Resource):
    pass


class alicloud_sag_qos_car(terrascript.Resource):
    pass


class alicloud_sag_snat_entry(terrascript.Resource):
    pass


class alicloud_sag_dnat_entry(terrascript.Resource):
    pass


class alicloud_sag_client_user(terrascript.Resource):
    pass


class alicloud_yundun_dbaudit_instance(terrascript.Resource):
    pass


class alicloud_yundun_bastionhost_instance(terrascript.Resource):
    pass


class alicloud_polardb_cluster(terrascript.Resource):
    pass


class alicloud_polardb_backup_policy(terrascript.Resource):
    pass


class alicloud_polardb_database(terrascript.Resource):
    pass


class alicloud_polardb_account(terrascript.Resource):
    pass


class alicloud_polardb_account_privilege(terrascript.Resource):
    pass


class alicloud_polardb_endpoint(terrascript.Resource):
    pass


class alicloud_polardb_endpoint_address(terrascript.Resource):
    pass


class alicloud_hbase_instance(terrascript.Resource):
    pass


class alicloud_market_order(terrascript.Resource):
    pass


class alicloud_adb_cluster(terrascript.Resource):
    pass


class alicloud_adb_backup_policy(terrascript.Resource):
    pass


class alicloud_adb_account(terrascript.Resource):
    pass


class alicloud_adb_connection(terrascript.Resource):
    pass


class alicloud_cen_flowlog(terrascript.Resource):
    pass


class alicloud_kms_secret(terrascript.Resource):
    pass


class alicloud_maxcompute_project(terrascript.Resource):
    pass


class alicloud_kms_alias(terrascript.Resource):
    pass


class alicloud_dns_instance(terrascript.Resource):
    pass


class alicloud_dns_domain_attachment(terrascript.Resource):
    pass


class alicloud_edas_application(terrascript.Resource):
    pass


class alicloud_edas_deploy_group(terrascript.Resource):
    pass


class alicloud_edas_application_scale(terrascript.Resource):
    pass


class alicloud_edas_slb_attachment(terrascript.Resource):
    pass


class alicloud_edas_cluster(terrascript.Resource):
    pass


class alicloud_edas_instance_cluster_attachment(terrascript.Resource):
    pass


class alicloud_edas_application_deployment(terrascript.Resource):
    pass


class alicloud_dns_domain(terrascript.Resource):
    pass


class alicloud_dms_enterprise_instance(terrascript.Resource):
    pass


class alicloud_waf_domain(terrascript.Resource):
    pass


class alicloud_cen_route_map(terrascript.Resource):
    pass


class alicloud_resource_manager_role(terrascript.Resource):
    pass


class alicloud_resource_manager_resource_group(terrascript.Resource):
    pass


class alicloud_resource_manager_folder(terrascript.Resource):
    pass


class alicloud_resource_manager_handshake(terrascript.Resource):
    pass


class alicloud_cen_private_zone(terrascript.Resource):
    pass


class alicloud_resource_manager_policy(terrascript.Resource):
    pass


class alicloud_resource_manager_account(terrascript.Resource):
    pass


class alicloud_waf_instance(terrascript.Resource):
    pass


class alicloud_resource_manager_resource_directory(terrascript.Resource):
    pass


class alicloud_alidns_domain_group(terrascript.Resource):
    pass


class alicloud_resource_manager_policy_version(terrascript.Resource):
    pass


class alicloud_kms_key_version(terrascript.Resource):
    pass


class alicloud_alidns_record(terrascript.Resource):
    pass


class alicloud_ddoscoo_scheduler_rule(terrascript.Resource):
    pass


class alicloud_cassandra_cluster(terrascript.Resource):
    pass


class alicloud_cassandra_data_center(terrascript.Resource):
    pass


class alicloud_cen_vbr_health_check(terrascript.Resource):
    pass


class alicloud_eci_openapi_image_cache(terrascript.Resource):
    pass


class alicloud_eci_image_cache(terrascript.Resource):
    pass


class alicloud_dms_enterprise_user(terrascript.Resource):
    pass


class alicloud_ecs_dedicated_host(terrascript.Resource):
    pass


class alicloud_oos_template(terrascript.Resource):
    pass


class alicloud_edas_k8s_cluster(terrascript.Resource):
    pass


class alicloud_oos_execution(terrascript.Resource):
    pass


class alicloud_resource_manager_policy_attachment(terrascript.Resource):
    pass
