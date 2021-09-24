"""
Test for Github issue 22: Allow multiple providers of same type

https://github.com/mjuenema/python-terrascript/issues/22

"""

import terrascript
import terrascript.provider.hashicorp.aws
import terrascript.resource.hashicorp.aws


def test_issue_22():
    ts = terrascript.Terrascript()

    # Add two providers
    p1 = terrascript.provider.hashicorp.aws.aws(region="us-east-1")
    p2 = terrascript.provider.hashicorp.aws.aws(region="us-east-2", alias="useast2")

    ts += p1
    ts += p2

    assert ts["provider"]["aws"][0]["region"] == "us-east-1"
    assert ts["provider"]["aws"][1]["region"] == "us-east-2"

    ts += terrascript.resource.hashicorp.aws.aws_instance(
        "I1", ami="ami-4bf3d731", instance_type="t2.large"
    )
    ts += terrascript.resource.hashicorp.aws.aws_instance(
        "I2", ami="ami-e1496384", instance_type="t2.large", provider=p2.alias
    )

    assert ts["resource"]["aws_instance"]["I2"]["provider"] == "useast2"
