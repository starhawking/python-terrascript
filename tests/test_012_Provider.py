from nose.tools import *
from tests.shared import *
import json

import terrascript

class Test_Provider(object):
    
    def test_povider_classes(self):
        provider = terrascript.Provider('name')
        assert isinstance(provider, terrascript.Block)
        
        
    def test_provider_with_nested_arguments(self):
        provider = terrascript.Provider('name', 
                                        integer=1, 
                                        string='string', 
                                        float=3.14,
                                        dictionary=dict(integer=2, 
                                                        string='string2', 
                                                        float=6.28),
                                        alist=[2, 'string2', 6.28], 
                                        nested=dict(dict2=dict(a=1, b=2),
                                                    list2=['a', 'b', 'c']))
        
        assert_equals_json(provider, 'Provider_provider_with_nested_arguments.json')
