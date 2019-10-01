# https://www.terraform.io/docs/configuration/locals.html

import terrascript
import terrascript.provider
import terrascript.resource

from shared import assert_equals_json


def test():
    """Locals (007)"""

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(version='~> 2.0', region='us-east-1')

    blue = terrascript.resource.aws_instance(
        'blue', ami="AMI", instance_type="t2.micro")
    config += blue

    green = terrascript.resource.aws_instance(
        'green', ami="AMI", instance_type="t2.micro")
    config += green

    locals1 = terrascript.Locals(service_name='forum', owner='Community Team')
    config += locals1

    config += terrascript.Locals(
        instance_ids='concat(aws_instance.blue.*.id, aws_instance.green.*.id)')

    config += terrascript.Locals(Service=locals1.service_name,
                                 Owner=locals1.owner)

    assert_equals_json(config, 'test_007.tf.json')
