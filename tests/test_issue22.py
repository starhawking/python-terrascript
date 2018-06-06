"""
Test for Github issue 22: Allow multiple providers of same type

https://github.com/mjuenema/python-terrascript/issues/22

"""

from terrascript import *
from terrascript.aws.r import aws_instance

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
