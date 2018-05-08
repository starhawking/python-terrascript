from terrascript import Terrascript, provisioner, provider
from terrascript.aws.r import aws_instance

def test_issue32():
    """Issue 32: provisioner return one line with provisioner.file instead a dictionary."""

    ts = Terrascript()

    ts += provider('aws', region='us-east-1')

    p = provisioner('file', source='pgbouncer-config', destination='/tmp/pgbouncer')

    ts += aws_instance('I1', ami='ami-4bf3d731', instance_type='t2.large', provisioner=p)

    j = ts.dump()

    assert 'file' in j
    assert 'pgbouncer' in j

    assert ts.validate(delete=False) is True

