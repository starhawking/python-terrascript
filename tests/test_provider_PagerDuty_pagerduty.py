# tests/test_provider_PagerDuty_pagerduty.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:24:19 UTC)


def test_provider_import():
    import terrascript.provider.PagerDuty.pagerduty


def test_resource_import():
    from terrascript.resource.PagerDuty.pagerduty import pagerduty_addon

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_business_service

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_escalation_policy

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_event_rule

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_extension

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_extension_servicenow

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_maintenance_window

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_response_play

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_ruleset

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_ruleset_rule

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_schedule

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_service

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_service_dependency

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_service_event_rule

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_service_integration

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_slack_connection

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_team

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_team_membership

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_user

    from terrascript.resource.PagerDuty.pagerduty import pagerduty_user_contact_method

    from terrascript.resource.PagerDuty.pagerduty import (
        pagerduty_user_notification_rule,
    )


def test_datasource_import():
    from terrascript.data.PagerDuty.pagerduty import pagerduty_business_service

    from terrascript.data.PagerDuty.pagerduty import pagerduty_escalation_policy

    from terrascript.data.PagerDuty.pagerduty import pagerduty_extension_schema

    from terrascript.data.PagerDuty.pagerduty import pagerduty_priority

    from terrascript.data.PagerDuty.pagerduty import pagerduty_ruleset

    from terrascript.data.PagerDuty.pagerduty import pagerduty_schedule

    from terrascript.data.PagerDuty.pagerduty import pagerduty_service

    from terrascript.data.PagerDuty.pagerduty import pagerduty_service_integration

    from terrascript.data.PagerDuty.pagerduty import pagerduty_team

    from terrascript.data.PagerDuty.pagerduty import pagerduty_user

    from terrascript.data.PagerDuty.pagerduty import pagerduty_user_contact_method

    from terrascript.data.PagerDuty.pagerduty import pagerduty_vendor


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.PagerDuty.pagerduty
#
#      t = terrascript.provider.PagerDuty.pagerduty.pagerduty()
#      s = str(t)
#
#      assert 'https://github.com/PagerDuty/terraform-provider-pagerduty' in s
#      assert '1.11.0' in s
