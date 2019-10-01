# tests/test_001.py
# https://www.terraform.io/docs/providers/aws/index.html

from shared import assert_deep_equal


def test():
    """Resource (001)"""

    import terrascript
    import terrascript.provider
    import terrascript.resource

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(version='~> 2.0', region='us-east-1')
    config += terrascript.resource.aws_vpc('example', cidr_block='10.0.0.0/16')

    assert_deep_equal(config, 'test_001.tf.json')
