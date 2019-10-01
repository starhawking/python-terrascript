# https://www.terraform.io/docs/provisioners/file.html

import terrascript
import terrascript.provider
import terrascript.resource

from shared import assert_equals_json


def test():
    """Provisioner (005)"""

    config = terrascript.Terrascript()

    config += terrascript.provider.aws(version='~> 2.0', region='us-east-1')

    #  Copies the myapp.conf file to /etc/myapp.conf
    provisioner1 = terrascript.Provisioner('file', source='conf/myapp.conf',
                                           destination='/etc/myapp.conf')

    # Copies the string in content into /tmp/file.log
    provisioner2 = terrascript.Provisioner('file', source='ami used: ${self.ami}',
                                           destination='/tmp/file.log')

    # Copies the configs.d folder to /etc/configs.d
    provisioner3 = terrascript.Provisioner('file', source='conf/configs.d',
                                           destination='/etc')

    # Copies all files and folders in apps/app1 to D:/IIS/webapp1
    provisioner4 = terrascript.Provisioner('file', source='apps/app1/',
                                           destination='D:/IIS/webapp1')

    config += terrascript.resource.aws_instance('web',
                                                ami="AMI",
                                                instance_type="t2.micro",
                                                provisioner=[provisioner1,
                                                             provisioner2,
                                                             provisioner3,
                                                             provisioner4])

    assert_equals_json(config, 'test_005.tf.json')
