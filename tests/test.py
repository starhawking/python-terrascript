
from terrascript import *
from terrascript.aws import r
from terrascript.aws import d

from collections import defaultdict

from nose.tools import *

PRINT = False
"""Don't print configuration at exit."""

DEBUG = True

STRING = 'STRING'
BOOL = True
INT = 10
FLOAT = 1.1
LIST = [1,'2',False]
DICT = {'a': 1, 'b': '2', 'c': True}


class TestConfig(object):
    def test_data(self):
        assert isinstance(config['data'], defaultdict)
        
    def test_resource(self):
        assert isinstance(config['resource'], defaultdict)
        
    def test_module(self):
        assert isinstance(config['module'], dict)
        
    def test_variable(self):
        assert isinstance(config['variable'], dict)
        
    @raises(KeyError)
    def test_wrongkey(self):
        isinstance(config['wrongkey'], dict)
        

class _Validate(object):
    def teardown(self):
        assert validate() is True

class _BaseTypes(object):
    _type = None
    k1 = k2 = None
    k3 = name = 'NAME'

    def test_string(self):
        self._type(self.name, argument=STRING)
        assert config[self.k1][self.k2][self.k3]['argument'] == STRING

    def test_bool(self):
        self._type(self.name, argument=BOOL)
        assert config[self.k1][self.k2][self.k3]['argument'] == BOOL

    def test_int(self):
        self._type(self.name, argument=INT)
        assert config[self.k1][self.k2][self.k3]['argument'] == INT

    def test_float(self):
        self._type(self.name, argument=FLOAT)
        assert config[self.k1][self.k2][self.k3]['argument'] == FLOAT

    def test_list(self):
        self._type(self.name, argument=LIST)
        assert config[self.k1][self.k2][self.k3]['argument'] == LIST

    def test_dict(self):
        self._type(self.name, argument=DICT)
        assert config[self.k1][self.k2][self.k3]['argument'] == DICT

    def test_interpol_resource_attr(self):
        resource = r.aws_instance('RESOURCE')
        self._type(self.name, argument=resource.attr)
        assert config[self.k1][self.k2][self.k3]['argument'] == '${aws_instance.RESOURCE.attr}'

    def test_interpol_data_attr(self):
        data = d.aws_instance('DATA')
        self._type(self.name, argument=data.attr)
        assert config[self.k1][self.k2][self.k3]['argument'] == '${data.aws_instance.DATA.attr}'


class TestLongResourceTypes(_BaseTypes, _Validate):
    _type = r.aws_instance
    k1 = 'resource'
    k2 = 'aws_instance'

    def test_reference(self):
        res = r.aws_instance('NAME1')
        r.instance('NAME2', depends_on=[res])

class TestShortResourceTypes(_BaseTypes, _Validate):
    _type = r.instance
    k1 = 'resource'
    k2 = 'aws_instance'


class TestLongDataTypes(_BaseTypes, _Validate):
    _type = d.aws_instance
    k1 = 'data'
    k2 = 'aws_instance'


class TestShortDataTypes(_BaseTypes, _Validate):
    _type = d.instance
    k1 = 'data'
    k2 = 'aws_instance'


class TestVariable(_Validate):
    def test_string(self):
        variable('NAME', description='DESCR', type='string', default='DEFAULT')
        assert config['variable']['NAME'] == {'default': 'DEFAULT', 'type': 'string', 'description': 'DESCR'}

    def test_list(self):
        variable('NAME', description='DESCR', type='list', default=[1,2,3])
        assert config['variable']['NAME']['default'] == [1,2,3]

    def test_map(self):
        variable('NAME', description='DESCR', type='map', default={'a': 1, 'b': 2})
        assert config['variable']['NAME']['default'] == {'a': 1, 'b': 2}

    def test_interpol_string(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var)
        assert config['resource']['aws_instance']['NAME']['argument'] == var
        assert '"${var.NAME}"' in dump()

    def test_interpol_listitem(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var[1])
        assert '"${var.NAME[1]}"' in dump()

    def test_interpol_mapitem(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var['KEY'])
        assert '"${var.NAME[\\"KEY\\"]}"' in dump()

class TestModule(_Validate):
    def test(self):
        mod = module('NAME', source="github.com/hashicorp/consul/terraform/aws")

    def test_interpolate(self):
        mod = module('NAME', source="github.com/hashicorp/consul/terraform/aws")
        res = r.instance('NAME', argument=mod.output)
        assert '"${module.NAME.output}"' in dump()

    def test_reference(self):
        mod = module('NAME', source="github.com/hashicorp/consul/terraform/aws")
        res = r.instance('NAME', depends_on=[mod])
        assert '"module.NAME"' in dump()
        

class TestOutput(_Validate):
    def test(self):
        mod = module('NAME', source="github.com/hashicorp/consul/terraform/aws")
        out = output('NAME', value=mod.output)


class TestProvider(_Validate):
    def test(self):
        provider('NAME', region='REGION')
        
        
class Test0Terraform(_Validate):
    # These tests must be executed first, thus the '0' in the name
    def test(self):
        terraform(required_version='> 0.9')
        
    def test_backend(self):
        b = backend(name='NAME', argument='ARGUMENT')
        terraform(required_version='> 0.9', backend=b)


class TestProvisionerConnection(_Validate):

    def test(self):
        conn = connection(type='SSH', user='USER', password='PASSWORD')
        prov = provisioner('PROVISIONER', sorce='SOURCE', destination='DESTINATION', connection=conn)
        r.aws_instance('NAME', provisioner=[prov])
        

class TestFunctions(_Validate):
    
    def test_synonyms(self):
        assert function == func == fn == f
    
    def test_string(self):
        assert f.function('string') == '${function("string")}'
        
    def test_resource(self):
        res = r.aws_instance('NAME')
        assert f.function(res) == '${function(aws_instance.NAME)}'
        
    def test_variable(self):
        aws_region = variable('aws_region', default='us-east-1', description='The AWS region to create things in.')
        aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})
        assert function.lookup(aws_amis, aws_region) == '${lookup(var.aws_amis,var.aws_region)}'
        
        
class TestResourceData(_Validate):
    def test_data(self):
        data('aws_instance', 'NAME')
        
    def test_resource(self):
        resource('aws_instance', 'NAME')
        
