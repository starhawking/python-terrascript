# https://www.terraform.io/docs/configuration/variables.html

import terrascript

from shared import assert_equals_json


def test():
    """Variable (004)"""

    config = terrascript.Terrascript()

    config += terrascript.Variable('image_id', type='string')
    config += terrascript.Variable('availability_zone_names',
                                   type='list(string)', default=["us-west-1a"])

    assert_equals_json(config, 'test_004.tf.json')
