
from terrascript import *


class Test_Terrascript(object):
    
    def setup(self):
        self.terrascript = Terrascript()
    
    def test_validate(self):
        assert self.terrascript.validate(delete=False) == True