# terrascript/cloudflare/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
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
