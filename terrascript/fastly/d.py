# terrascript/fastly/d.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class fastly_ip_ranges(terrascript.Data):
    pass


class fastly_tls_activation(terrascript.Data):
    pass


class fastly_tls_activation_ids(terrascript.Data):
    pass


class fastly_tls_certificate(terrascript.Data):
    pass


class fastly_tls_certificate_ids(terrascript.Data):
    pass


class fastly_tls_configuration(terrascript.Data):
    pass


class fastly_tls_configuration_ids(terrascript.Data):
    pass


class fastly_tls_domain(terrascript.Data):
    pass


class fastly_tls_platform_certificate(terrascript.Data):
    pass


class fastly_tls_platform_certificate_ids(terrascript.Data):
    pass


class fastly_tls_private_key(terrascript.Data):
    pass


class fastly_tls_private_key_ids(terrascript.Data):
    pass


class fastly_tls_subscription(terrascript.Data):
    pass


class fastly_tls_subscription_ids(terrascript.Data):
    pass


class fastly_waf_rules(terrascript.Data):
    pass
