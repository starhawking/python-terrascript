import terrascript
import terrascript.provider
import terrascript.resource

import tests.shared


def test_example_002():
    config = terrascript.Terrascript()

    config += terrascript.provider.aws(
        region="us-east-1",
        version="~> 2.0",
        endpoints=terrascript.Block(
            dynamodb="http://localhost:4569",
            s3="http://localhost:4572",
        ),
    )

    config += terrascript.resource.aws_vpc("example", cidr_block="10.0.0.0/16")

    tests.shared.assert_deep_equal(config, "test_002.tf.json")
