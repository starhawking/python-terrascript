# https://www.terraform.io/docs/configuration/locals.html

import terrascript
import terrascript.aws
import terrascript.aws.d

from shared import assert_equals_json

def test():
    """Data (008)"""

    config = terrascript.Terrascript()

    config += terrascript.aws.aws(version='~> 2.0', region='us-east-1')

    config += terrascript.aws.d.aws_ami('example', most_recent=True, owners=['self'],
                                        tags=dict(Name="app-server", Tested="true"))

    assert_equals_json(config, 'test_008.tf.json')