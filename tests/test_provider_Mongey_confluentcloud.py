# tests/test_provider_Mongey_confluentcloud.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:14:33 UTC)


def test_provider_import():
    import terrascript.provider.Mongey.confluentcloud


def test_resource_import():
    from terrascript.resource.Mongey.confluentcloud import confluentcloud_api_key

    from terrascript.resource.Mongey.confluentcloud import confluentcloud_connector

    from terrascript.resource.Mongey.confluentcloud import confluentcloud_environment

    from terrascript.resource.Mongey.confluentcloud import confluentcloud_kafka_cluster

    from terrascript.resource.Mongey.confluentcloud import (
        confluentcloud_schema_registry,
    )

    from terrascript.resource.Mongey.confluentcloud import (
        confluentcloud_service_account,
    )


def test_datasource_import():
    from terrascript.data.Mongey.confluentcloud import confluentcloud_environment


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.Mongey.confluentcloud
#
#      t = terrascript.provider.Mongey.confluentcloud.confluentcloud()
#      s = str(t)
#
#      assert 'https://github.com/Mongey/terraform-provider-confluentcloud' in s
#      assert '0.0.12' in s
