"""
Test for Github issues.

"""

from terrascript import *
from terrascript.aws.r import aws_instance
from terrascript.datadog.r import datadog_monitor


def test_issue22():
    """Issue 22: Allow multiple providers of same type.

       See also pull request #27 Feature/multiple providers

       {
         "provider": {
           "aws": {
             "__DEFAULT__": {
               "region": "us-east-1"
             },
             "useast2": {
               "alias": "useast2",
               "region": "us-east-2"
             }
           }
         },
         "resource": {
           "aws_instance": {
             "I1": {
               "ami": "ami-4bf3d731",
               "instance_type": "t2.large"
             },
             "I2": {
               "ami": "ami-e1496384",
               "instance_type": "t2.large",
               "provider": "aws.useast2"
             }
           }
         }
       }

    """
    ts = Terrascript()
    ts += provider('aws', region='us-east-1')
    ts += provider('aws', region='us-east-2', alias='useast2')
    ts += aws_instance('I1', ami='ami-4bf3d731', instance_type='t2.large')
    ts += aws_instance('I2', ami='ami-e1496384', instance_type='t2.large', provider='aws.useast2')
    assert ts.validate() is True


def test_issue26():
    """Issue 26: Problem when using resource in a loop

       The introduction of the `terrascript.Terrascript` class makes this
       possible. The sample code of issue 26 as been altered for this test.

    """

    for name in ['first', 'second', 'third']:
        ts = Terrascript()
        ts += provider('datadog', api_key='DUMMY', app_key='DUMMY')
        ts += datadog_monitor(name, name=name, type='metric alert',
                                query='some query', escalation_message='some message')
        ts.validate()
