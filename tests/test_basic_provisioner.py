import terrascript
import terrascript.resource

class TestProvisioner(object):
    
    def __init__(self):
        self.cfg = terrascript.Terrascript()
        
    def test_one_provisioner(self):
        p = terrascript.Provisioner("local-exec", when="destroy", command="echo 'Destroy-time provisioner'")

        assert p['local-exec']['when'] == 'destroy'

        self.cfg += terrascript.resource.aws_instance('instance1', instance_type="t2.micro",
                                                      provisioner=p)

        assert len(self.cfg['resource']['aws_instance']['instance1']['provisioner']) == 1
        assert self.cfg['resource']['aws_instance']['instance1']['provisioner']['local-exec']['when'] == 'destroy'


    def test_multiple_provisioners(self):
        create = terrascript.Provisioner("local-exec", command="echo 'Create'")
        destroy = terrascript.Provisioner("local-exec", when="destroy", command="echo 'Destroy'")

        self.cfg += terrascript.resource.aws_instance('instance1', instance_type="t2.micro",
                                                      provisioner=[create, destroy])

        assert len(self.cfg['resource']['aws_instance']['instance1']['provisioner']) == 2
        assert self.cfg['resource']['aws_instance']['instance1']['provisioner'][0]['local-exec']['command'] == "echo 'Create'"
        assert self.cfg['resource']['aws_instance']['instance1']['provisioner'][1]['local-exec']['command'] == "echo 'Destroy'"

        # {
        #  "resource": {
        #    "aws_instance": {
        #      "instance1": {
        #        "instance_type": "t2.micro",
        #        "provisioner": [
        #          {
        #            "local-exec": {
        #              "command": "echo 'Create'"
        #            }
        #          },
        #          {
        #            "local-exec": {
        #              "when": "destroy",
        #              "command": "echo 'Destroy'"
        #            }
        #          }
        #        ]
        #      }
        #    }
        #  }
        # }

