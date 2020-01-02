from terrascript import Locals, Terrascript
from terrascript.aws.r import aws_instance


class Test_Locals:
    def setup(self):
        self.config = Terrascript()

    def test_locals(self):
        locals1 = Locals(instance_type='t2.micro')
        locals2 = Locals(ami='ami-2757f631')
        resource = aws_instance('instance1', instance_type=locals1.instance_type, ami=locals2.ami)
        self.config += locals1
        self.config += locals2
        self.config += resource

        assert dict(self.config) == {
            'locals': {
                'instance_type': 't2.micro',
                'ami': 'ami-2757f631'
            },
            'resource': {
                'aws_instance': {
                    'instance1': {
                        'ami': '${locals.ami}',
                        'instance_type': '${locals.instance_type}'
                    }
                }
            }
        }
