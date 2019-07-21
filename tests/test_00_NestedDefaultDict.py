
import json

from terrascript import NestedDefaultDict


class Test_NestedDefaultDict(object):

    def setup(self):
        self.nd = NestedDefaultDict()
        self.nd[1][2][3] = 123

    def test_instance(self):
        assert isinstance(self.nd, NestedDefaultDict)
        assert isinstance(self.nd[1], NestedDefaultDict)
        assert isinstance(self.nd[1][2], NestedDefaultDict)
        assert self.nd[1][2][3] == 123

    def test_setting_values(self):
        self.nd[11] = 11
        assert self.nd[1][2][3] == 123
        assert self.nd[11] == 11
        
    def test_str(self):
        assert json.loads(str(self.nd)) == {'1': {'2': {'3': 123}}}
