from terrascript import Terrascript, provisioner, provider
from terrascript.aws.r import aws_instance


def test_issue32():
    """Issue 32: provisioner return one line with provisioner.file instead a dictionary."""

    ts = Terrascript()

    ts += provider('aws', region='ap-southeast-2')

    p = provisioner('local-exec', command='date > $(mktemp tmpXXXXXXX.terrascript)')

    ts += aws_instance('I1', ami='ami-60a26a02', instance_type='t2.nano', provisioner=p)

    j = ts.dump()

    assert 'mktemp' in j

    assert ts.validate() is True

