
import json

from terrascript import *

from nose.tools import *


class Test_Provider(object):
    def setup(self):
        self.provider = Provider('openstack',
                                user_name="admin",
                                tenant_name="admin",
                                password="pwd",
                                auth_url="http://myauthurl:5000/v2.0",
                                region="RegionOne"
                                )

    def test_instance_Provider(self):
        assert isinstance(self.provider, Provider)

    def test_labels(self):
        assert self.provider._labels == ('openstack',)

    def test_str(self):
        assert json.loads(str(self.provider)) == self.provider


@raises(TypeError)
def test_provider_missing_label():
    Provider(arg1='arg1', arg2='arg2')
