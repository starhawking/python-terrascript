# tests/test_001.py
# https://www.terraform.io/docs/providers/aws/index.html

import terrascript
import terrascript.aws
import terrascript.aws.r

from shared import assert_equals_json

def test():
    """Resource (001)"""

    config = terrascript.Terrascript()

    config += terrascript.aws.aws(version='~> 2.0', region='us-east-1')
    config += terrascript.aws.r.aws_vpc('example', cidr_block='10.0.0.0/16')

    assert_equals_json(config, 'test_001.tf.json')
