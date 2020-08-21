# terrascript/data/cloudflare.py
import terrascript


class cloudflare_ip_ranges(terrascript.Data):
    pass


class cloudflare_waf_groups(terrascript.Data):
    pass


class cloudflare_waf_packages(terrascript.Data):
    pass


class cloudflare_waf_rules(terrascript.Data):
    pass


class cloudflare_zones(terrascript.Data):
    pass


__all__ = [
    "cloudflare_ip_ranges",
    "cloudflare_waf_groups",
    "cloudflare_waf_packages",
    "cloudflare_waf_rules",
    "cloudflare_zones",
]
