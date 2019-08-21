"""
Test for Github issue 26: Problem when using resource in a loop

https://github.com/mjuenema/python-terrascript/issues/26

"""

from terrascript import *
from terrascript.datadog.r import datadog_monitor

def test_issue26():
    """Issue 26: Problem when using resource in a loop

       The introduction of the `terrascript.Terrascript` class makes this
       possible. The sample code of issue 26 as been altered for this test.

    """

    for name in ['first', 'second', 'third']:
        ts = Terrascript()
        ts += provider('datadog', api_key='DUMMY', app_key='DUMMY')
        ts += datadog_monitor(name, name=name, type='metric alert',
                                query='some query', message='a message',
                                escalation_message='some message')
        assert ts.validate(delete=False) is True
