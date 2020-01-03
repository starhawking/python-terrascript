import terrascript
import terrascript.provider

class TestModule(object):

    def __init__(self):
        self.cfg = terrascript.Terrascript()

    def test_one_module(self):
        m = terrascript.Module('name', source='source.tf', parameter=1)
        assert isinstance(m, terrascript.NamedBlock)
        assert isinstance(m, terrascript.Module)
        assert m._name == 'name'
        assert m['source'] == 'source.tf'
        assert m['parameter'] == 1

        self.cfg += m
        assert len(self.cfg['module'].keys()) == 1
        assert self.cfg['module']['name']['source'] == 'source.tf'
        assert self.cfg['module']['name']['parameter'] == 1

    def test_two_modules(self):
        m1 = terrascript.Module('name1', source='source1.tf', parameter=1)
        m2 = terrascript.Module('name2', source='source2.tf', parameter=2)

        self.cfg += m1
        self.cfg += m2

        assert len(self.cfg['module'].keys()) == 2
        assert self.cfg['module']['name1']['source'] == 'source1.tf'
        assert self.cfg['module']['name1']['parameter'] == 1
        assert self.cfg['module']['name2']['source'] == 'source2.tf'
        assert self.cfg['module']['name2']['parameter'] == 2

    def test_duplicate_names(self):
        m1 = terrascript.Module('name', source='source1.tf', parameter=1)
        m2 = terrascript.Module('name', source='source2.tf', parameter=2)

        self.cfg += m1
        self.cfg += m2      # Overwrites m1

        assert len(self.cfg['module'].keys()) == 1
        assert self.cfg['module']['name']['source'] == 'source2.tf'
        assert self.cfg['module']['name']['parameter'] == 2

    