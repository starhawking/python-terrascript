# tests/test_provider_paultyng_unifi.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:29:45 UTC)


def test_provider_import():
    import terrascript.provider.paultyng.unifi


def test_resource_import():
    from terrascript.resource.paultyng.unifi import unifi_device

    from terrascript.resource.paultyng.unifi import unifi_dynamic_dns

    from terrascript.resource.paultyng.unifi import unifi_firewall_group

    from terrascript.resource.paultyng.unifi import unifi_firewall_rule

    from terrascript.resource.paultyng.unifi import unifi_network

    from terrascript.resource.paultyng.unifi import unifi_port_forward

    from terrascript.resource.paultyng.unifi import unifi_port_profile

    from terrascript.resource.paultyng.unifi import unifi_setting_mgmt

    from terrascript.resource.paultyng.unifi import unifi_setting_usg

    from terrascript.resource.paultyng.unifi import unifi_site

    from terrascript.resource.paultyng.unifi import unifi_static_route

    from terrascript.resource.paultyng.unifi import unifi_user

    from terrascript.resource.paultyng.unifi import unifi_user_group

    from terrascript.resource.paultyng.unifi import unifi_wlan


def test_datasource_import():
    from terrascript.data.paultyng.unifi import unifi_ap_group

    from terrascript.data.paultyng.unifi import unifi_network

    from terrascript.data.paultyng.unifi import unifi_port_profile

    from terrascript.data.paultyng.unifi import unifi_radius_profile

    from terrascript.data.paultyng.unifi import unifi_user

    from terrascript.data.paultyng.unifi import unifi_user_group


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.paultyng.unifi
#
#      t = terrascript.provider.paultyng.unifi.unifi()
#      s = str(t)
#
#      assert 'https://github.com/paultyng/terraform-provider-unifi' in s
#      assert '0.34.0' in s
