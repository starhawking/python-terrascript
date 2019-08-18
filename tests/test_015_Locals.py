from nose.tools import *
from tests.shared import *
import json

import terrascript
import terrascript.aws.r

class Test_Locals(object):
    # https://www.terraform.io/docs/configuration/locals.html
    
    def setup(self):
        self.locals = terrascript.Locals(service_name='forum', owner='Community Team')
    
    
    def test_locals_classes(self):
        assert isinstance(self.locals, terrascript.Block)
        
    
    def test_output_example1(self):
        assert_equals_json(self.locals, 'Locals_locals_example1.json')