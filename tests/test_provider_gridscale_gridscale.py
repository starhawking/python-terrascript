# tests/test_provider_gridscale_gridscale.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:17:40 UTC)


def test_provider_import():
    import terrascript.provider.gridscale.gridscale


def test_resource_import():
    from terrascript.resource.gridscale.gridscale import gridscale_backupschedule

    from terrascript.resource.gridscale.gridscale import gridscale_firewall

    from terrascript.resource.gridscale.gridscale import gridscale_ipv4

    from terrascript.resource.gridscale.gridscale import gridscale_ipv6

    from terrascript.resource.gridscale.gridscale import gridscale_isoimage

    from terrascript.resource.gridscale.gridscale import gridscale_k8s

    from terrascript.resource.gridscale.gridscale import gridscale_loadbalancer

    from terrascript.resource.gridscale.gridscale import gridscale_mariadb

    from terrascript.resource.gridscale.gridscale import (
        gridscale_marketplace_application,
    )

    from terrascript.resource.gridscale.gridscale import (
        gridscale_marketplace_application_import,
    )

    from terrascript.resource.gridscale.gridscale import gridscale_memcached

    from terrascript.resource.gridscale.gridscale import gridscale_mysql

    from terrascript.resource.gridscale.gridscale import gridscale_network

    from terrascript.resource.gridscale.gridscale import (
        gridscale_object_storage_accesskey,
    )

    from terrascript.resource.gridscale.gridscale import gridscale_paas

    from terrascript.resource.gridscale.gridscale import gridscale_paas_securityzone

    from terrascript.resource.gridscale.gridscale import gridscale_postgresql

    from terrascript.resource.gridscale.gridscale import gridscale_redis_cache

    from terrascript.resource.gridscale.gridscale import gridscale_redis_store

    from terrascript.resource.gridscale.gridscale import gridscale_server

    from terrascript.resource.gridscale.gridscale import gridscale_snapshot

    from terrascript.resource.gridscale.gridscale import gridscale_snapshotschedule

    from terrascript.resource.gridscale.gridscale import gridscale_sqlserver

    from terrascript.resource.gridscale.gridscale import gridscale_sshkey

    from terrascript.resource.gridscale.gridscale import gridscale_ssl_certificate

    from terrascript.resource.gridscale.gridscale import gridscale_storage

    from terrascript.resource.gridscale.gridscale import gridscale_storage_clone

    from terrascript.resource.gridscale.gridscale import gridscale_storage_import

    from terrascript.resource.gridscale.gridscale import gridscale_template


def test_datasource_import():
    from terrascript.data.gridscale.gridscale import gridscale_backup_list

    from terrascript.data.gridscale.gridscale import gridscale_backupschedule

    from terrascript.data.gridscale.gridscale import gridscale_firewall

    from terrascript.data.gridscale.gridscale import gridscale_ipv4

    from terrascript.data.gridscale.gridscale import gridscale_ipv6

    from terrascript.data.gridscale.gridscale import gridscale_isoimage

    from terrascript.data.gridscale.gridscale import gridscale_loadbalancer

    from terrascript.data.gridscale.gridscale import gridscale_marketplace_application

    from terrascript.data.gridscale.gridscale import gridscale_network

    from terrascript.data.gridscale.gridscale import gridscale_object_storage_accesskey

    from terrascript.data.gridscale.gridscale import gridscale_paas

    from terrascript.data.gridscale.gridscale import gridscale_paas_securityzone

    from terrascript.data.gridscale.gridscale import gridscale_public_network

    from terrascript.data.gridscale.gridscale import gridscale_server

    from terrascript.data.gridscale.gridscale import gridscale_snapshot

    from terrascript.data.gridscale.gridscale import gridscale_snapshotschedule

    from terrascript.data.gridscale.gridscale import gridscale_sshkey

    from terrascript.data.gridscale.gridscale import gridscale_ssl_certificate

    from terrascript.data.gridscale.gridscale import gridscale_storage

    from terrascript.data.gridscale.gridscale import gridscale_template


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.gridscale.gridscale
#
#      t = terrascript.provider.gridscale.gridscale.gridscale()
#      s = str(t)
#
#      assert 'https://github.com/gridscale/terraform-provider-gridscale' in s
#      assert '1.13.0' in s
