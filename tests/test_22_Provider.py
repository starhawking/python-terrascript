
from terrascript import *
from tests import validate

class Test_Provider(object):
    
    def setup(self):
        self.config = Terrascript()
        
    def test_provider(self):
        self.config += Provider('openstack',
                                user_name="admin",
                                tenant_name="admin",
                                password="pwd",
                                auth_url="http://myauthurl:5000/v2.0",
                                region="RegionOne"
                                )
        assert validate(self.config) == True