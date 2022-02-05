# tests/test_provider_techBeck03_guacamole.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:17:53 UTC)


def test_provider_import():
    import terrascript.provider.techBeck03.guacamole


def test_resource_import():
    from terrascript.resource.techBeck03.guacamole import guacamole_connection_group

    from terrascript.resource.techBeck03.guacamole import (
        guacamole_connection_kubernetes,
    )

    from terrascript.resource.techBeck03.guacamole import guacamole_connection_rdp

    from terrascript.resource.techBeck03.guacamole import guacamole_connection_ssh

    from terrascript.resource.techBeck03.guacamole import guacamole_connection_telnet

    from terrascript.resource.techBeck03.guacamole import guacamole_connection_vnc

    from terrascript.resource.techBeck03.guacamole import guacamole_user

    from terrascript.resource.techBeck03.guacamole import guacamole_user_group


def test_datasource_import():
    from terrascript.data.techBeck03.guacamole import guacamole_connection_group

    from terrascript.data.techBeck03.guacamole import guacamole_connection_kubernetes

    from terrascript.data.techBeck03.guacamole import guacamole_connection_rdp

    from terrascript.data.techBeck03.guacamole import guacamole_connection_ssh

    from terrascript.data.techBeck03.guacamole import guacamole_connection_telnet

    from terrascript.data.techBeck03.guacamole import guacamole_connection_vnc

    from terrascript.data.techBeck03.guacamole import guacamole_user

    from terrascript.data.techBeck03.guacamole import guacamole_user_group


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.techBeck03.guacamole
#
#      t = terrascript.provider.techBeck03.guacamole.guacamole()
#      s = str(t)
#
#      assert 'https://github.com/techBeck03/terraform-provider-guacamole' in s
#      assert '1.2.7' in s