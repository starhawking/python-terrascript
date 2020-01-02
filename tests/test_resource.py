import terrascript
import terrascript.resource

class TestResource(object):
    
    def __init__(self):
        self.cfg = terrascript.Terrascript()
        
    def test_one_resource(self):
        r = terrascript.resource.aws_instance('instance1', instance_type="t2.micro")
        assert r['instance_type'] == "t2.micro"
        
        self.cfg += r
        assert self.cfg['resource']['aws_instance']['instance1']['instance_type'] == "t2.micro"
        
    def test_two_resources(self):
        r1 = terrascript.resource.aws_instance('instance1', instance_type="t2.micro")
        r2 = terrascript.resource.aws_instance('instance2', instance_type="t2.small")
        
        assert r1['instance_type'] == "t2.micro"
        assert r2['instance_type'] == "t2.small"
        
        self.cfg += r1
        self.cfg += r2
        assert self.cfg['resource']['aws_instance']['instance1']['instance_type'] == "t2.micro"
        assert self.cfg['resource']['aws_instance']['instance2']['instance_type'] == "t2.small"