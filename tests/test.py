
from terrascript import *
from terrascript.aws import r
from terrascript.aws import d

PRINT = False
"""Don't print configuration at exit."""

STRING = 'STRING'
BOOL = True
INT = 10
FLOAT = 1.1
LIST = [1,'2',False]
DICT = {'a': 1, 'b': '2', 'c': True}

class _BaseTypes(object):
    _type = None
    k1 = k2 = None
    k3 = name = 'NAME'

    def test_string(self):
        self._type(self.name, argument=STRING)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': STRING}

    def test_bool(self):
        self._type(self.name, argument=BOOL)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': BOOL}

    def test_int(self):
        self._type(self.name, argument=INT)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': INT}

    def test_float(self):
        self._type(self.name, argument=FLOAT)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': FLOAT}

    def test_list(self):
        self._type(self.name, argument=LIST)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': LIST}

    def test_dict(self):
        self._type(self.name, argument=DICT)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': DICT}

    def test_interpol_resource_attr(self):
        resource = r.aws_instance('RESOURCE')
        self._type(self.name, argument=resource.attr)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': '${aws_instance.RESOURCE.attr}' }

    def test_interpol_data_attr(self):
        data = d.aws_instance('DATA')
        self._type(self.name, argument=data.attr)
        assert CONFIG[self.k1][self.k2][self.k3] == {'argument': '${data.aws_instance.DATA.attr}' }


class TestLongResourceTypes(_BaseTypes):
    _type = r.aws_instance
    k1 = 'resource'
    k2 = 'aws_instance'


class TestShortResourceTypes(_BaseTypes):
    _type = r.instance
    k1 = 'resource'
    k2 = 'aws_instance'


class TestLongDataTypes(_BaseTypes):
    _type = d.aws_instance
    k1 = 'data'
    k2 = 'aws_instance'


class TestShortDataTypes(_BaseTypes):
    _type = d.instance
    k1 = 'data'
    k2 = 'aws_instance'


class TestVariable(object):
    def test_string(self):
        variable('NAME', description='DESCR', type='string', default='DEFAULT')
        assert CONFIG['variable']['NAME'] == {'default': 'DEFAULT', 'type': 'string', 'description': 'DESCR'}

    def test_list(self):
        variable('NAME', description='DESCR', type='list', default=[1,2,3])
        assert CONFIG['variable']['NAME']['default'] == [1,2,3]

    def test_map(self):
        variable('NAME', description='DESCR', type='map', default={'a': 1, 'b': 2})
        assert CONFIG['variable']['NAME']['default'] == {'a': 1, 'b': 2}

    def test_interpol_string(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var)
        assert CONFIG['resource']['aws_instance']['NAME']['argument'] == var
        assert '"${var.NAME}"' in dump()

    def test_interpol_listitem(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var[1])
        assert '"${var.NAME[1]}"' in dump()

    def test_interpol_mapitem(self):
        var = variable('NAME')
        res = r.instance('NAME', argument=var['KEY'])
        assert '"${var.NAME[\\"KEY\\"]}"' in dump()


