# tests/test_provider_NetApp_netapp-cloudmanager.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:22:08 UTC)


def test_provider_import():
    import terrascript.provider.NetApp.netapp_cloudmanager


def test_resource_import():
    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_aggregate,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_anf_volume,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_aws_fsx,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cifs_server,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_connector_aws,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_connector_azure,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_connector_gcp,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cvo_aws,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cvo_azure,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cvo_gcp,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cvs_gcp_volume,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_nss_account,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_snapmirror,
    )

    from terrascript.resource.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_volume,
    )


def test_datasource_import():
    from terrascript.data.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_cifs_server,
    )

    from terrascript.data.NetApp.netapp_cloudmanager import (
        netapp_cloudmanager_nss_account,
    )

    from terrascript.data.NetApp.netapp_cloudmanager import netapp_cloudmanager_volume


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.NetApp.netapp_cloudmanager
#
#      t = terrascript.provider.NetApp.netapp_cloudmanager.netapp_cloudmanager()
#      s = str(t)
#
#      assert 'https://github.com/NetApp/terraform-provider-netapp-cloudmanager' in s
#      assert '21.9.2' in s
