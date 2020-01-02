import terrascript
import terrascript.provider

class TestProvider(object):

    def __init__(self):
        self.cfg = terrascript.Terrascript()

    def test_one_provider(self):
        p = terrascript.provider.aws(alias='aws1', region='us-west-1')
        assert isinstance(p, terrascript.Block)
        assert isinstance(p, terrascript.Provider)
        assert p['alias'] == 'aws1'
        assert p['region'] == 'us-west-1'

        self.cfg += p
        assert len(self.cfg['provider']['aws']) == 1
        assert self.cfg['provider']['aws'][0]['alias'] == 'aws1'
        assert self.cfg['provider']['aws'][0]['region'] == 'us-west-1'

    def test_two_providers(self):
        p1 = terrascript.provider.aws(alias='aws1', region='us-west-1')
        assert p1['alias'] == 'aws1'
        assert p1['region'] == 'us-west-1'

        p2 = terrascript.provider.aws(alias='aws2', region='us-west-2')
        assert p2['alias'] == 'aws2'
        assert p2['region'] == 'us-west-2'

        self.cfg += p1
        self.cfg += p2
        assert len(self.cfg['provider']['aws']) == 2
        assert self.cfg['provider']['aws'][0]['alias'] == 'aws1'
        assert self.cfg['provider']['aws'][0]['region'] == 'us-west-1'
        assert self.cfg['provider']['aws'][1]['alias'] == 'aws2'
        assert self.cfg['provider']['aws'][1]['region'] == 'us-west-2'
        
    def test_example1(self):
        # https://www.terraform.io/docs/providers/aws/index.html
        
        p = terrascript.provider.aws(
                version="~> 2.0",
                region="region",
                access_key="access_key",
                secret_key="my-secret-key"
            )
        
        self.cfg += p
        
        assert self.cfg['provider']['aws'][0]['version'] == "~> 2.0"
        assert self.cfg['provider']['aws'][0]['region'] == "region"
        assert self.cfg['provider']['aws'][0]['access_key'] == "access_key"
        assert self.cfg['provider']['aws'][0]['secret_key'] == "my-secret-key"