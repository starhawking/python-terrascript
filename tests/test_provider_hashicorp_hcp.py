# tests/test_provider_hashicorp_hcp.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:18:10 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.hcp


def test_resource_import():
    from terrascript.resource.hashicorp.hcp import hcp_aws_network_peering

    from terrascript.resource.hashicorp.hcp import hcp_aws_transit_gateway_attachment

    from terrascript.resource.hashicorp.hcp import hcp_consul_cluster

    from terrascript.resource.hashicorp.hcp import hcp_consul_cluster_root_token

    from terrascript.resource.hashicorp.hcp import hcp_consul_snapshot

    from terrascript.resource.hashicorp.hcp import hcp_hvn

    from terrascript.resource.hashicorp.hcp import hcp_hvn_peering_connection

    from terrascript.resource.hashicorp.hcp import hcp_hvn_route

    from terrascript.resource.hashicorp.hcp import hcp_vault_cluster

    from terrascript.resource.hashicorp.hcp import hcp_vault_cluster_admin_token


def test_datasource_import():
    from terrascript.data.hashicorp.hcp import hcp_aws_network_peering

    from terrascript.data.hashicorp.hcp import hcp_aws_transit_gateway_attachment

    from terrascript.data.hashicorp.hcp import hcp_consul_agent_helm_config

    from terrascript.data.hashicorp.hcp import hcp_consul_agent_kubernetes_secret

    from terrascript.data.hashicorp.hcp import hcp_consul_cluster

    from terrascript.data.hashicorp.hcp import hcp_consul_versions

    from terrascript.data.hashicorp.hcp import hcp_hvn

    from terrascript.data.hashicorp.hcp import hcp_hvn_peering_connection

    from terrascript.data.hashicorp.hcp import hcp_hvn_route

    from terrascript.data.hashicorp.hcp import hcp_packer_image

    from terrascript.data.hashicorp.hcp import hcp_packer_image_iteration

    from terrascript.data.hashicorp.hcp import hcp_packer_iteration

    from terrascript.data.hashicorp.hcp import hcp_vault_cluster


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.hcp
#
#      t = terrascript.provider.hashicorp.hcp.hcp()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-hcp' in s
#      assert '0.17.0' in s
