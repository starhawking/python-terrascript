# tests/test_provider_camptocamp_geoserver.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:16:50 UTC)


def test_provider_import():
    import terrascript.provider.camptocamp.geoserver


def test_resource_import():
    from terrascript.resource.camptocamp.geoserver import geoserver_datastore

    from terrascript.resource.camptocamp.geoserver import geoserver_featuretype

    from terrascript.resource.camptocamp.geoserver import geoserver_workspace


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.camptocamp.geoserver
#
#      t = terrascript.provider.camptocamp.geoserver.geoserver()
#      s = str(t)
#
#      assert 'https://github.com/camptocamp/terraform-provider-geoserver' in s
#      assert '0.0.3' in s