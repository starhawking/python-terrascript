
import json

from terrascript import *

class Test_Terrascript(object):
    def setup(self):
        self.terrascript = Terrascript()

    def test_instance_Terrascript(self):
        assert isinstance(self.terrascript, Terrascript)

    def test_labels(self):
        assert self.terrascript._labels == ()
        
    def test_str(self):
        assert json.loads(str(self.terrascript)) == self.terrascript