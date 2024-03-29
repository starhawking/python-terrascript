# tests/test_provider_aequitas_transip.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:29:04 UTC)


def test_provider_import():
    import terrascript.provider.aequitas.transip


def test_resource_import():
    from terrascript.resource.aequitas.transip import transip_dns_record

    from terrascript.resource.aequitas.transip import transip_domain

    from terrascript.resource.aequitas.transip import transip_private_network

    from terrascript.resource.aequitas.transip import transip_private_network_attachment

    from terrascript.resource.aequitas.transip import transip_sshkey

    from terrascript.resource.aequitas.transip import transip_vps

    from terrascript.resource.aequitas.transip import transip_vps_firewall


def test_datasource_import():
    from terrascript.data.aequitas.transip import transip_domain

    from terrascript.data.aequitas.transip import transip_private_network

    from terrascript.data.aequitas.transip import transip_sshkey

    from terrascript.data.aequitas.transip import transip_vps


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.aequitas.transip
#
#      t = terrascript.provider.aequitas.transip.transip()
#      s = str(t)
#
#      assert 'https://github.com/aequitas/terraform-provider-transip' in s
#      assert '0.1.11' in s
