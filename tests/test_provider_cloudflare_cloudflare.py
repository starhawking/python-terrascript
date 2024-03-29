# tests/test_provider_cloudflare_cloudflare.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:14:07 UTC)


def test_provider_import():
    import terrascript.provider.cloudflare.cloudflare


def test_resource_import():
    from terrascript.resource.cloudflare.cloudflare import cloudflare_access_application

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_access_ca_certificate,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_access_group

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_access_identity_provider,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_access_keys_configuration,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_access_mutual_tls_certificate,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_access_policy

    from terrascript.resource.cloudflare.cloudflare import cloudflare_access_rule

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_access_service_token,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_account_member

    from terrascript.resource.cloudflare.cloudflare import cloudflare_api_token

    from terrascript.resource.cloudflare.cloudflare import cloudflare_argo

    from terrascript.resource.cloudflare.cloudflare import cloudflare_argo_tunnel

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_authenticated_origin_pulls,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_authenticated_origin_pulls_certificate,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_byo_ip_prefix

    from terrascript.resource.cloudflare.cloudflare import cloudflare_certificate_pack

    from terrascript.resource.cloudflare.cloudflare import cloudflare_custom_hostname

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_custom_hostname_fallback_origin,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_custom_pages

    from terrascript.resource.cloudflare.cloudflare import cloudflare_custom_ssl

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_device_posture_rule,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_filter

    from terrascript.resource.cloudflare.cloudflare import cloudflare_firewall_rule

    from terrascript.resource.cloudflare.cloudflare import cloudflare_healthcheck

    from terrascript.resource.cloudflare.cloudflare import cloudflare_ip_list

    from terrascript.resource.cloudflare.cloudflare import cloudflare_load_balancer

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_load_balancer_monitor,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_load_balancer_pool

    from terrascript.resource.cloudflare.cloudflare import cloudflare_logpull_retention

    from terrascript.resource.cloudflare.cloudflare import cloudflare_logpush_job

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_logpush_ownership_challenge,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_magic_firewall_ruleset,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_notification_policy,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_notification_policy_webhooks,
    )

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_origin_ca_certificate,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_page_rule

    from terrascript.resource.cloudflare.cloudflare import cloudflare_rate_limit

    from terrascript.resource.cloudflare.cloudflare import cloudflare_record

    from terrascript.resource.cloudflare.cloudflare import cloudflare_ruleset

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_spectrum_application,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_static_route

    from terrascript.resource.cloudflare.cloudflare import cloudflare_teams_account

    from terrascript.resource.cloudflare.cloudflare import cloudflare_teams_list

    from terrascript.resource.cloudflare.cloudflare import cloudflare_teams_location

    from terrascript.resource.cloudflare.cloudflare import cloudflare_teams_rule

    from terrascript.resource.cloudflare.cloudflare import cloudflare_waf_group

    from terrascript.resource.cloudflare.cloudflare import cloudflare_waf_override

    from terrascript.resource.cloudflare.cloudflare import cloudflare_waf_package

    from terrascript.resource.cloudflare.cloudflare import cloudflare_waf_rule

    from terrascript.resource.cloudflare.cloudflare import cloudflare_waiting_room

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_worker_cron_trigger,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_worker_route

    from terrascript.resource.cloudflare.cloudflare import cloudflare_worker_script

    from terrascript.resource.cloudflare.cloudflare import cloudflare_workers_kv

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_workers_kv_namespace,
    )

    from terrascript.resource.cloudflare.cloudflare import cloudflare_zone

    from terrascript.resource.cloudflare.cloudflare import cloudflare_zone_dnssec

    from terrascript.resource.cloudflare.cloudflare import cloudflare_zone_lockdown

    from terrascript.resource.cloudflare.cloudflare import (
        cloudflare_zone_settings_override,
    )


def test_datasource_import():
    from terrascript.data.cloudflare.cloudflare import (
        cloudflare_api_token_permission_groups,
    )

    from terrascript.data.cloudflare.cloudflare import cloudflare_ip_ranges

    from terrascript.data.cloudflare.cloudflare import (
        cloudflare_origin_ca_root_certificate,
    )

    from terrascript.data.cloudflare.cloudflare import cloudflare_waf_groups

    from terrascript.data.cloudflare.cloudflare import cloudflare_waf_packages

    from terrascript.data.cloudflare.cloudflare import cloudflare_waf_rules

    from terrascript.data.cloudflare.cloudflare import cloudflare_zone_dnssec

    from terrascript.data.cloudflare.cloudflare import cloudflare_zones


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.cloudflare.cloudflare
#
#      t = terrascript.provider.cloudflare.cloudflare.cloudflare()
#      s = str(t)
#
#      assert 'https://github.com/cloudflare/terraform-provider-cloudflare' in s
#      assert '3.1.0' in s
