"""
Test for Github issue 26: Problem when using resource in a loop

https://github.com/mjuenema/python-terrascript/issues/26

"""

import terrascript
import terrascript.resource

def test_issue_26():

    for name in ['first', 'second', 'third']:
        ts = terrascript.Terrascript()
        ts += terrascript.provider.datadog(api_key='DUMMY', app_key='DUMMY')
        ts += terrascript.resource.datadog_monitor(name, name=name, type='metric alert',
                                                   query='some query', message='a message',
                                                   escalation_message='some message')

        assert len(ts['resource']['datadog_monitor'].keys()) == 1
        assert ts['resource']['datadog_monitor'][name]['name'] == name

