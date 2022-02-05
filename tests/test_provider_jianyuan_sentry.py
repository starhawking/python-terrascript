# tests/test_provider_jianyuan_sentry.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:26:49 UTC)


def test_provider_import():
    import terrascript.provider.jianyuan.sentry


def test_resource_import():
    from terrascript.resource.jianyuan.sentry import sentry_key

    from terrascript.resource.jianyuan.sentry import sentry_organization

    from terrascript.resource.jianyuan.sentry import sentry_plugin

    from terrascript.resource.jianyuan.sentry import sentry_project

    from terrascript.resource.jianyuan.sentry import sentry_rule

    from terrascript.resource.jianyuan.sentry import sentry_team


def test_datasource_import():
    from terrascript.data.jianyuan.sentry import sentry_key

    from terrascript.data.jianyuan.sentry import sentry_organization


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.jianyuan.sentry
#
#      t = terrascript.provider.jianyuan.sentry.sentry()
#      s = str(t)
#
#      assert 'https://github.com/jianyuan/terraform-provider-sentry' in s
#      assert '0.6.0' in s