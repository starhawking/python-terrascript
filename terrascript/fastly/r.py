# terrascript/fastly/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class fastly_service_acl_entries_v1(terrascript.Resource):
    pass


class fastly_service_compute(terrascript.Resource):
    pass


class fastly_service_dictionary_items_v1(terrascript.Resource):
    pass


class fastly_service_dynamic_snippet_content_v1(terrascript.Resource):
    pass


class fastly_service_v1(terrascript.Resource):
    pass


class fastly_service_waf_configuration(terrascript.Resource):
    pass


class fastly_tls_activation(terrascript.Resource):
    pass


class fastly_tls_certificate(terrascript.Resource):
    pass


class fastly_tls_platform_certificate(terrascript.Resource):
    pass


class fastly_tls_private_key(terrascript.Resource):
    pass


class fastly_tls_subscription(terrascript.Resource):
    pass


class fastly_tls_subscription_validation(terrascript.Resource):
    pass


class fastly_user_v1(terrascript.Resource):
    pass
