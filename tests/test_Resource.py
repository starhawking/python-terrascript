from nose.tools import *
from tests.shared import *
import json

import terrascript

class Test_Resource(object):
    
    def test_resource_classes(self):
        resource = terrascript.Resource('name')
        assert isinstance(resource, terrascript.Block)
        assert isinstance(resource['name'], terrascript.Block)
        
        
    def test_resource_attributes(self):
        resource = terrascript.Resource('name')
        assert resource.name == 'name'
        
            
    def test_resource(self):
        resource = terrascript.Resource('name')
        
        assert_equals_json(resource, 'Resource_resource.json')
        
        
    def test_resource_with_arguments(self):
        resource = terrascript.Resource('name', 
                                        integer=1, 
                                        string='string', 
                                        float=3.14)
        
        assert_equals_json(resource, 'Resource_resource_with_arguments.json')
        
        
    def test_resource_with_dictionary(self):
        resource = terrascript.Resource('name', 
                                        integer=1, 
                                        string='string', 
                                        float=3.14, 
                                        dictionary=dict(integer=2, 
                                                        string='string2', 
                                                        float=6.28)
                                        )
        
        assert_equals_json(resource, 'Resource_resource_with_dictionary.json')
        
        
    def test_resource_with_list(self):
        resource = terrascript.Resource('name', 
                                        integer=1, 
                                        string='string', 
                                        float=3.14, 
                                        alist=[2, 'string2', 6.28]
                                        )
        
        assert_equals_json(resource, 'Resource_resource_with_list.json')
        
        
    def test_resource_with_nested_arguments(self):
        resource = terrascript.Resource('name', 
                                        integer=1, 
                                        string='string', 
                                        float=3.14,
                                        dictionary=dict(integer=2, 
                                                        string='string2', 
                                                        float=6.28),
                                        alist=[2, 'string2', 6.28], 
                                        nested=dict(dict2=dict(a=1, b=2),
                                                    list2=['a', 'b', 'c']))
        
        assert_equals_json(resource, 'Resource_resource_with_nested_arguments.json')
