import terrascript
import terrascript.data

class TestDatasource(object):
    
    def __init__(self):
        self.cfg = terrascript.Terrascript()
        
    def test_one_datasource(self):
        d = terrascript.data.aws_eip('external_ip', public_ip="1.2.3.4")
        assert isinstance(d, terrascript.NamedBlock)
        assert isinstance(d, terrascript.Data)
        assert d._name == 'external_ip'
        assert d['public_ip'] == "1.2.3.4"
        
        self.cfg += d
        assert self.cfg['data']['aws_eip']['external_ip']['public_ip'] == "1.2.3.4"

    def test_datasource_attributes(self):
        d = terrascript.data.aws_eip('external_ip', public_ip="1.2.3.4")
        assert d.public_ip == "1.2.3.4"

        assert isinstance(d.unknown, terrascript.Attribute)
        assert isinstance(d.unknown.unknown, terrascript.Attribute)

        assert d.unknown == 'data.aws_eip.external_ip.unknown'
        assert d.unknown.unknown == 'data.aws_eip.external_ip.unknown.unknown'

      