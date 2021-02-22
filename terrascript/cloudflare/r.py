# terrascript/cloudflare/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class cloudflare_access_application(terrascript.Resource):
    pass


class cloudflare_access_group(terrascript.Resource):
    pass


class cloudflare_access_identity_provider(terrascript.Resource):
    pass


class cloudflare_access_policy(terrascript.Resource):
    pass


class cloudflare_access_rule(terrascript.Resource):
    pass


class cloudflare_access_service_token(terrascript.Resource):
    pass


class cloudflare_account_member(terrascript.Resource):
    pass


class cloudflare_api_token(terrascript.Resource):
    pass


class cloudflare_argo(terrascript.Resource):
    pass


class cloudflare_argo_tunnel(terrascript.Resource):
    pass


class cloudflare_authenticated_origin_pulls(terrascript.Resource):
    pass


class cloudflare_authenticated_origin_pulls_certificate(terrascript.Resource):
    pass


class cloudflare_byo_ip_prefix(terrascript.Resource):
    pass


class cloudflare_certificate_pack(terrascript.Resource):
    pass


class cloudflare_custom_hostname(terrascript.Resource):
    pass


class cloudflare_custom_hostname_fallback_origin(terrascript.Resource):
    pass


class cloudflare_custom_pages(terrascript.Resource):
    pass


class cloudflare_custom_ssl(terrascript.Resource):
    pass


class cloudflare_filter(terrascript.Resource):
    pass


class cloudflare_firewall_rule(terrascript.Resource):
    pass


class cloudflare_healthcheck(terrascript.Resource):
    pass


class cloudflare_ip_list(terrascript.Resource):
    pass


class cloudflare_load_balancer(terrascript.Resource):
    pass


class cloudflare_load_balancer_monitor(terrascript.Resource):
    pass


class cloudflare_load_balancer_pool(terrascript.Resource):
    pass


class cloudflare_logpull_retention(terrascript.Resource):
    pass


class cloudflare_logpush_job(terrascript.Resource):
    pass


class cloudflare_logpush_ownership_challenge(terrascript.Resource):
    pass


class cloudflare_magic_firewall_ruleset(terrascript.Resource):
    pass


class cloudflare_origin_ca_certificate(terrascript.Resource):
    pass


class cloudflare_page_rule(terrascript.Resource):
    pass


class cloudflare_rate_limit(terrascript.Resource):
    pass


class cloudflare_record(terrascript.Resource):
    pass


class cloudflare_spectrum_application(terrascript.Resource):
    pass


class cloudflare_waf_group(terrascript.Resource):
    pass


class cloudflare_waf_override(terrascript.Resource):
    pass


class cloudflare_waf_package(terrascript.Resource):
    pass


class cloudflare_waf_rule(terrascript.Resource):
    pass


class cloudflare_worker_cron_trigger(terrascript.Resource):
    pass


class cloudflare_worker_route(terrascript.Resource):
    pass


class cloudflare_worker_script(terrascript.Resource):
    pass


class cloudflare_workers_kv(terrascript.Resource):
    pass


class cloudflare_workers_kv_namespace(terrascript.Resource):
    pass


class cloudflare_zone(terrascript.Resource):
    pass


class cloudflare_zone_dnssec(terrascript.Resource):
    pass


class cloudflare_zone_lockdown(terrascript.Resource):
    pass


class cloudflare_zone_settings_override(terrascript.Resource):
    pass
