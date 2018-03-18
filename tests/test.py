import os
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


AWS_AMI = 'ami-97785bed'
AWS_INSTANCE_TYPE = 't2.large'


class Test1ConfigDefaults(object):

    def setup(self):
        self.cfg = Terrascript()

    def test_data(self):
        assert isinstance(self.cfg.config['data'], defaultdict)

    def test_resource(self):
        assert isinstance(self.cfg.config['resource'], defaultdict)

    def test_module(self):
        assert isinstance(self.cfg.config['module'], dict)

    def test_variable(self):
        assert isinstance(self.cfg.config['variable'], dict)

    @raises(KeyError)
    def test_wrongkey(self):
        isinstance(self.cfg.config['wrongkey'], dict)

class Test2Config(object):

    def setup(self):
        self.cfg = Terrascript()

    def test_string(self):
        self.cfg += r.aws_instance('R1', argument=STRING)
        assert self.cfg.config['resource']['aws_instance']['R1']['argument'] == STRING

    def test_bool(self):
        self.cfg += r.aws_instance('R2', argument=BOOL)
        assert self.cfg.config['resource']['aws_instance']['R2']['argument'] == BOOL

    def test_int(self):
        self.cfg += r.aws_instance('R3', argument=INT)
        assert self.cfg.config['resource']['aws_instance']['R3']['argument'] == INT

    def test_float(self):
        self.cfg += r.aws_instance('R4', argument=FLOAT)
        assert self.cfg.config['resource']['aws_instance']['R4']['argument'] == FLOAT

    def test_list(self):
        self.cfg += r.aws_instance('R6', argument=LIST)
        assert self.cfg.config['resource']['aws_instance']['R6']['argument'] == LIST

    def test_dict(self):
        self.cfg += r.aws_instance('R7', argument=DICT)
        assert self.cfg.config['resource']['aws_instance']['R7']['argument'] == DICT

    def test_interpol_resource_attr(self):
        resource = r.aws_instance('R8', attr=STRING)
        self.cfg += resource 
        self.cfg += r.aws_instance('R10', argument=resource.attr)
        assert self.cfg.config['resource']['aws_instance']['R10']['argument'] == '${aws_instance.R8.attr}'

    def test_interpol_data_attr(self):
        data = d.aws_instance('D1')
        self.cfg += data 
        self.cfg += r.aws_instance('R9', argument=data.attr)
        assert self.cfg.config['resource']['aws_instance']['R9']['argument'] == '${data.aws_instance.D1.attr}'


class TestBase(object):

    def setup(self):
        self.cfg = Terrascript()
        self.cfg += provider('aws', region='us-east-1')

    def teardown(self):
        assert self.cfg.validate() is True


class TestVariable(TestBase):
    def test_string(self):
        self.cfg += variable('VAR1', description='DESCR', type='string', default='DEFAULT')

    def test_list(self):
        self.cfg += variable('VAR2', description='DESCR', type='list', default=[1,2,3])

    def test_map(self):
        self.cfg += variable('VAR3', description='DESCR', type='map', default={'a': 1, 'b': 2})

    def test_interpol_string(self):
        var = variable('VAR4', type='string', default='us-east-1')
        self.cfg += var
        res = r.aws_instance('NAME', ami=AWS_AMI, instance_type=var)
        self.cfg += res
        assert '"${var.VAR4}"' in self.cfg.dump()

    def test_interpol_listitem(self):
        var = variable('VAR5', type='list', default=['us-east-1', 'us-east-2'])
        self.cfg += var
        res = r.aws_instance('NAME', ami=var[1], instance_type=AWS_INSTANCE_TYPE)
        self.cfg += res
        assert '"${var.VAR5[1]}"' in self.cfg.dump()

    def test_interpol_mapitem(self):
        var = variable('VAR6', type='map', default={'one': 'us-east-1', 'two': 'us-east-2'})
        self.cfg += var
        res = r.aws_instance('NAME', ami=var['two'], instance_type=AWS_INSTANCE_TYPE)
        self.cfg += res
        assert '"${var.VAR6[\\"two\\"]}"' in self.cfg.dump()

class TestModule(TestBase):

    def setup(self):
        self.cfg = Terrascript()
        self.cfg += provider('aws', region='us-east-1')

    def teardown(self):
        assert self.cfg.validate() is True

    def test(self):
        mod = module('M1', source="devops-workflow/ami-ids/aws")
        self.cfg += mod

    def test_interpolate(self):
        mod = module('M2', source="devops-workflow/ami-ids/aws")
        self.cfg += mod
        res = r.aws_instance('NAME', ami=mod.ami_id, instance_type=AWS_INSTANCE_TYPE)
        self.cfg += res
        assert '"${module.M2.ami_id}"' in self.cfg.dump()

    def test_reference(self):
        mod = module('M3', source="devops-workflow/ami-ids/aws")
        self.cfg += mod
        res = r.aws_instance('NAME', ami=AWS_AMI, instance_type=AWS_INSTANCE_TYPE,
                             depends_on=[mod])
        self.cfg += res
        assert '"module.M3"' in self.cfg.dump()


class TestOutput(TestBase):
    def test(self):
        mod = module('NAME', source="devops-workflow/ami-ids/aws")
        self.cfg += mod
        out = output('NAME', value=mod.ami_id)
        self.cfg += out


class TestProvider(TestBase):
    def test(self):
        provider('aws', region='us-east-1')


class TestMultipleProvider(TestBase):
    def test(self):
        self.cfg += provider('aws', region='us-east-1')
        self.cfg += provider('aws', region='us-east-2', alias='PROVIDER2')
        assert '"PROVIDER2"' in self.cfg.dump()


class Test0Terraform(TestBase):
    # These tests must be executed first, thus the '0' in the name
    def test(self):
        self.cfg += terraform(required_version='> 0.9')

    def test_backend(self):
        b = backend(name='local', path='ARGUMENT')
        self.cfg += terraform(required_version='> 0.9', backend=b)


class TestProvisionerConnection(TestBase):

    def test(self):
        conn = connection(type='SSH', user='USER', password='PASSWORD')
        prov = provisioner('file', sorce='SOURCE', destination='DESTINATION', connection=conn)
        res = r.aws_instance('NAME', ami=AWS_AMI, instance_type=AWS_INSTANCE_TYPE, provisioner=prov)


class TestFunctions(object):

    def test_synonyms(self):
        assert function == func == fn == f

    def test_string(self):
        assert f.function('string') == '${function("string")}'

    def test_resource(self):
        res = r.aws_instance('NAME', ami=AWS_AMI, instance_type=AWS_INSTANCE_TYPE)
        assert f.somefunction(res) == '${somefunction(aws_instance.NAME)}'

    def test_variable(self):
        aws_region = variable('aws_region', default='us-east-1', description='The AWS region to create things in.')
        aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})
        assert f.somefunction(aws_amis, aws_region) == '${somefunction(var.aws_amis,var.aws_region)}'


class TestResourceData(TestBase):
    def test_data(self):
        data('aws_instance', 'NAME')

    def test_resource(self):
        resource('aws_instance', 'NAME', ami=AWS_AMI, instance_type=AWS_INSTANCE_TYPE)

