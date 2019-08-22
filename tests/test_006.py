# https://www.terraform.io/docs/configuration/outputs.html

import terrascript
import terrascript.aws
import terrascript.aws.r

from shared import assert_equals_json

def test():
    """Output (006)"""

    config = terrascript.Terrascript()

    config += terrascript.aws.aws(version='~> 2.0', region='us-east-1')

    aws_instance = terrascript.aws.r.aws_instance('web', ami = "AMI", instance_type="t2.micro")
    config += aws_instance

    config += terrascript.Output('instance_ip_addr', value=aws_instance.server.private_ip)

    assert_equals_json(config, 'test_006.tf.json')