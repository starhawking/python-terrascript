# Just some basic test

from importlib import import_module as importm

class _Base(object):
    provider = 'aws'

    def test_resources(self):
        r = importm(self.import_r)
        for k in dir(r):
            if k.startswith(self.provider):
                # Find short name 'aws_instance' -> 'instance'
                assert k[len(self.provider)+1:] in dir(r)

    def test_data(self):
        d = importm(self.import_d)
        for k in dir(d):
            if k.startswith(self.provider):
                # Find short name 'aws_instance' -> 'instance'
                assert k[len(self.provider)+1:] in dir(d)


class TestAWS(_Base):
    provider = 'aws'
    import_r = 'terrascript.aws.r'
    import_d = 'terrascript.aws.d'


class TestGoogle(_Base):
    provider = 'google'
    import_r = 'terrascript.google.r'
    import_d = 'terrascript.google.d'


class TestTerraform(object):

    def test(self):
        from terrascript.terraform.d import terraform_remote_state, remote_state


class TestTemplate(_Base):
    provider = 'template'
    import_r = 'terrascript.template.r'
    import_d = 'terrascript.template.d'


class TestOpenstack(_Base):
    provider = 'openstack'
    import_r = 'terrascript.openstack.r'
    import_d = 'terrascript.openstack.d'


class TestKubernetes(_Base):
    provider = 'kubernetes'
    import_r = 'terrascript.kubernetes.r'
    import_d = 'terrascript.kubernetes.d'


class TestDocker(_Base):
    provider = 'docker'
    import_r = 'terrascript.docker.r'
    import_d = 'terrascript.docker.d'
