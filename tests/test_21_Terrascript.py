
from terrascript import *
from tests import validate

class Test_Terrascript(object):
    
    def setup(self):
        self.config = Terrascript()
        
    def test(self):
        assert validate(self.config) == True
    
    def test_resource(self):       
        self.config += Resource('null_resource', 'label')
        assert validate(self.config) == True
    