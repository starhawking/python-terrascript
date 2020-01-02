import terrascript
import terrascript.provider

class TestProvider(object):

    def __init__(self):
        self.cfg = terrascript.Terrascript()

    def test_one_provider(self):
        p1 = terrascript.provider.aws(alias='aws1', region='us-west-1')
        assert p1['alias'] == 'aws1'
        assert p1['region'] == 'us-west-1'

        self.cfg += p1
        assert len(self.cfg['provider']) == 1
        assert self.cfg['provider'][0]['alias'] == 'aws1'
        assert self.cfg['provider'][0]['region'] == 'us-west-1'

    def test_two_providers(self):
        p1 = terrascript.provider.aws(alias='aws1', region='us-west-1')
        assert p1['alias'] == 'aws1'
        assert p1['region'] == 'us-west-1'

        p2 = terrascript.provider.aws(alias='aws2', region='us-west-2')
        assert p2['alias'] == 'aws2'
        assert p2['region'] == 'us-west-2'

        self.cfg += p1
        self.cfg += p2
        assert len(self.cfg['provider']) == 2
        assert self.cfg['provider'][0]['alias'] == 'aws1'
        assert self.cfg['provider'][0]['region'] == 'us-west-1'
        assert self.cfg['provider'][1]['alias'] == 'aws2'
        assert self.cfg['provider'][1]['region'] == 'us-west-2'

def test_duplicate_providers(self):
    # Ensure that duplicate providers are only added once.
    pass