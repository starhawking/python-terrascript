# tests/test_provider_hashicorp_kubernetes-alpha.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:20:48 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.kubernetes_alpha


def test_resource_import():
    from terrascript.resource.hashicorp.kubernetes_alpha import kubernetes_manifest


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.kubernetes_alpha
#
#      t = terrascript.provider.hashicorp.kubernetes_alpha.kubernetes_alpha()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-kubernetes-alpha' in s
#      assert '0.6.0' in s
