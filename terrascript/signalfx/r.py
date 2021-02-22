# terrascript/signalfx/r.py
import warnings
warnings.warn("using the 'legacy layout' is deprecated", DeprecationWarning,
              stacklevel=2)
import terrascript


class signalfx_alert_muting_rule(terrascript.Resource):
    pass


class signalfx_aws_external_integration(terrascript.Resource):
    pass


class signalfx_aws_integration(terrascript.Resource):
    pass


class signalfx_aws_token_integration(terrascript.Resource):
    pass


class signalfx_azure_integration(terrascript.Resource):
    pass


class signalfx_dashboard(terrascript.Resource):
    pass


class signalfx_dashboard_group(terrascript.Resource):
    pass


class signalfx_data_link(terrascript.Resource):
    pass


class signalfx_detector(terrascript.Resource):
    pass


class signalfx_event_feed_chart(terrascript.Resource):
    pass


class signalfx_gcp_integration(terrascript.Resource):
    pass


class signalfx_heatmap_chart(terrascript.Resource):
    pass


class signalfx_jira_integration(terrascript.Resource):
    pass


class signalfx_list_chart(terrascript.Resource):
    pass


class signalfx_opsgenie_integration(terrascript.Resource):
    pass


class signalfx_org_token(terrascript.Resource):
    pass


class signalfx_pagerduty_integration(terrascript.Resource):
    pass


class signalfx_single_value_chart(terrascript.Resource):
    pass


class signalfx_slack_integration(terrascript.Resource):
    pass


class signalfx_team(terrascript.Resource):
    pass


class signalfx_text_chart(terrascript.Resource):
    pass


class signalfx_time_chart(terrascript.Resource):
    pass


class signalfx_victor_ops_integration(terrascript.Resource):
    pass


class signalfx_webhook_integration(terrascript.Resource):
    pass
