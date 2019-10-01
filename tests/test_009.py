# https://www.terraform.io/docs/configuration/locals.html

import terrascript
import terrascript.provider
import terrascript.data

from shared import assert_equals_json


def test():
    """Update method (009)"""

    config = terrascript.Terrascript()
    config.add(terrascript.provider.aws(region='us-east-1'))

    ts2 = terrascript.Terrascript()
    ts2.add(terrascript.provider.aws(region='us-east-2', alias='useast2'))

    config.update(ts2)  # ts1 is now merged with ts2 items

    assert_equals_json(config, 'test_009.tf.json')
