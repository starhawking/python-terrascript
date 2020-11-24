import terrascript
import terrascript.provider
import terrascript.resource

import tests.shared


def test_example_001():
    config = terrascript.Terrascript()

    config += terrascript.provider.aws(region="us-east-1", version="~> 2.0")

    config += terrascript.resource.aws_vpc("example", cidr_block="10.0.0.0/16")

    tests.shared.assert_deep_equal(config, "test_001.tf.json")
