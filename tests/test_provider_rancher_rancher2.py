# tests/test_provider_rancher_rancher2.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:25:37 UTC)


def test_provider_import():
    import terrascript.provider.rancher.rancher2


def test_resource_import():
    from terrascript.resource.rancher.rancher2 import rancher2_app

    from terrascript.resource.rancher.rancher2 import rancher2_app_v2

    from terrascript.resource.rancher.rancher2 import (
        rancher2_auth_config_activedirectory,
    )

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_adfs

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_azuread

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_freeipa

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_github

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_keycloak

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_okta

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_openldap

    from terrascript.resource.rancher.rancher2 import rancher2_auth_config_ping

    from terrascript.resource.rancher.rancher2 import rancher2_bootstrap

    from terrascript.resource.rancher.rancher2 import rancher2_catalog

    from terrascript.resource.rancher.rancher2 import rancher2_catalog_v2

    from terrascript.resource.rancher.rancher2 import rancher2_certificate

    from terrascript.resource.rancher.rancher2 import rancher2_cloud_credential

    from terrascript.resource.rancher.rancher2 import rancher2_cluster

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_alert_group

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_alert_rule

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_driver

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_logging

    from terrascript.resource.rancher.rancher2 import (
        rancher2_cluster_role_template_binding,
    )

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_sync

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_template

    from terrascript.resource.rancher.rancher2 import rancher2_cluster_v2

    from terrascript.resource.rancher.rancher2 import rancher2_etcd_backup

    from terrascript.resource.rancher.rancher2 import rancher2_feature

    from terrascript.resource.rancher.rancher2 import rancher2_global_dns

    from terrascript.resource.rancher.rancher2 import rancher2_global_dns_provider

    from terrascript.resource.rancher.rancher2 import rancher2_global_role

    from terrascript.resource.rancher.rancher2 import rancher2_global_role_binding

    from terrascript.resource.rancher.rancher2 import rancher2_machine_config_v2

    from terrascript.resource.rancher.rancher2 import rancher2_multi_cluster_app

    from terrascript.resource.rancher.rancher2 import rancher2_namespace

    from terrascript.resource.rancher.rancher2 import rancher2_node_driver

    from terrascript.resource.rancher.rancher2 import rancher2_node_pool

    from terrascript.resource.rancher.rancher2 import rancher2_node_template

    from terrascript.resource.rancher.rancher2 import rancher2_notifier

    from terrascript.resource.rancher.rancher2 import (
        rancher2_pod_security_policy_template,
    )

    from terrascript.resource.rancher.rancher2 import rancher2_project

    from terrascript.resource.rancher.rancher2 import rancher2_project_alert_group

    from terrascript.resource.rancher.rancher2 import rancher2_project_alert_rule

    from terrascript.resource.rancher.rancher2 import rancher2_project_logging

    from terrascript.resource.rancher.rancher2 import (
        rancher2_project_role_template_binding,
    )

    from terrascript.resource.rancher.rancher2 import rancher2_registry

    from terrascript.resource.rancher.rancher2 import rancher2_role_template

    from terrascript.resource.rancher.rancher2 import rancher2_secret

    from terrascript.resource.rancher.rancher2 import rancher2_secret_v2

    from terrascript.resource.rancher.rancher2 import rancher2_setting

    from terrascript.resource.rancher.rancher2 import rancher2_storage_class_v2

    from terrascript.resource.rancher.rancher2 import rancher2_token

    from terrascript.resource.rancher.rancher2 import rancher2_user


def test_datasource_import():
    from terrascript.data.rancher.rancher2 import rancher2_app

    from terrascript.data.rancher.rancher2 import rancher2_catalog

    from terrascript.data.rancher.rancher2 import rancher2_catalog_v2

    from terrascript.data.rancher.rancher2 import rancher2_certificate

    from terrascript.data.rancher.rancher2 import rancher2_cloud_credential

    from terrascript.data.rancher.rancher2 import rancher2_cluster

    from terrascript.data.rancher.rancher2 import rancher2_cluster_alert_group

    from terrascript.data.rancher.rancher2 import rancher2_cluster_alert_rule

    from terrascript.data.rancher.rancher2 import rancher2_cluster_driver

    from terrascript.data.rancher.rancher2 import rancher2_cluster_logging

    from terrascript.data.rancher.rancher2 import rancher2_cluster_role_template_binding

    from terrascript.data.rancher.rancher2 import rancher2_cluster_scan

    from terrascript.data.rancher.rancher2 import rancher2_cluster_template

    from terrascript.data.rancher.rancher2 import rancher2_cluster_v2

    from terrascript.data.rancher.rancher2 import rancher2_etcd_backup

    from terrascript.data.rancher.rancher2 import rancher2_global_dns_provider

    from terrascript.data.rancher.rancher2 import rancher2_global_role

    from terrascript.data.rancher.rancher2 import rancher2_global_role_binding

    from terrascript.data.rancher.rancher2 import rancher2_multi_cluster_app

    from terrascript.data.rancher.rancher2 import rancher2_namespace

    from terrascript.data.rancher.rancher2 import rancher2_node_driver

    from terrascript.data.rancher.rancher2 import rancher2_node_pool

    from terrascript.data.rancher.rancher2 import rancher2_node_template

    from terrascript.data.rancher.rancher2 import rancher2_notifier

    from terrascript.data.rancher.rancher2 import rancher2_pod_security_policy_template

    from terrascript.data.rancher.rancher2 import rancher2_project

    from terrascript.data.rancher.rancher2 import rancher2_project_alert_group

    from terrascript.data.rancher.rancher2 import rancher2_project_alert_rule

    from terrascript.data.rancher.rancher2 import rancher2_project_logging

    from terrascript.data.rancher.rancher2 import rancher2_project_role_template_binding

    from terrascript.data.rancher.rancher2 import rancher2_registry

    from terrascript.data.rancher.rancher2 import rancher2_role_template

    from terrascript.data.rancher.rancher2 import rancher2_secret

    from terrascript.data.rancher.rancher2 import rancher2_secret_v2

    from terrascript.data.rancher.rancher2 import rancher2_setting

    from terrascript.data.rancher.rancher2 import rancher2_storage_class_v2

    from terrascript.data.rancher.rancher2 import rancher2_user


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.rancher.rancher2
#
#      t = terrascript.provider.rancher.rancher2.rancher2()
#      s = str(t)
#
#      assert 'https://github.com/rancher/terraform-provider-rancher2' in s
#      assert '1.20.0' in s
