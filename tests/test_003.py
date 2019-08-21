import terrascript
import terrascript.aws
import terrascript.aws.r

from shared import assert_equals_json

def test():
    """Module (003)"""

    config = terrascript.Terrascript()

    config += terrascript.aws.aws(access_key='ACCESS_KEY_HERE',
                                  secret_key='SECRET_KEY_HERE',
                                  region='us-east-1')

    config += terrascript.Module('vpc',
                                 source="terraform-aws-modules/vpc/aws",
                                 version="2.9.0")

    assert_equals_json(config, 'test_003.tf.json')
