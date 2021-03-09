# terrascript/data/signalfx.py
import terrascript


class signalfx_aws_services(terrascript.Data):
    pass


class signalfx_azure_services(terrascript.Data):
    pass


class signalfx_gcp_services(terrascript.Data):
    pass


class signalfx_dimension_values(terrascript.Data):
    pass


class signalfx_pagerduty_integration(terrascript.Data):
    pass


class signalfx_data_link(terrascript.Data):
    pass


__all__ = [
    "signalfx_aws_services",
    "signalfx_azure_services",
    "signalfx_gcp_services",
    "signalfx_dimension_values",
    "signalfx_pagerduty_integration",
    "signalfx_data_link",
]
