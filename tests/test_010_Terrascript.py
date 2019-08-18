from nose.tools import *
from tests.shared import *

import terrascript

class Test_Terrascript(object):
    
    def setup(self):
        self.terrascript = terrascript.Terrascript()
    
    def test_terrascript_add(self):
        assert self.terrascript.hasattr('add')
        
    def test_terrascript_plus(self):
        assert self.terrascript.hasattr('__add__')
    
    @raises(TypeError)
    def test_terrascript_add_type_error(self):
        self.terrascript.add(1)
        
    @raises(TypeError)
    def test_terrascript_plus_type_error(self):
        self.terrascript += 1