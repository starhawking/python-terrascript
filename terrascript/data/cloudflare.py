# terrascript/data/cloudflare.py
import terrascript


class cloudflare_api_token_permission_groups(terrascript.Data):
    pass


class cloudflare_ip_ranges(terrascript.Data):
    pass


class cloudflare_waf_groups(terrascript.Data):
    pass


class cloudflare_waf_packages(terrascript.Data):
    pass


class cloudflare_waf_rules(terrascript.Data):
    pass


class cloudflare_zone_dnssec(terrascript.Data):
    pass


class cloudflare_zones(terrascript.Data):
    pass


__all__ = [
    "cloudflare_api_token_permission_groups",
    "cloudflare_ip_ranges",
    "cloudflare_waf_groups",
    "cloudflare_waf_packages",
    "cloudflare_waf_rules",
    "cloudflare_zone_dnssec",
    "cloudflare_zones",
]
