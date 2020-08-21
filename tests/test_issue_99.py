"""
https://github.com/mjuenema/python-terrascript/issues/99

"""

# The test case


def test_issue_99_copy():

    import terrascript.resource
    import copy

    resource = terrascript.resource.aws_vpc("example", cidr_block="10.0.0.0/16")
    resource2 = copy.copy(resource)

    assert isinstance(resource2, terrascript.resource.aws_vpc)
    assert resource2.cidr_block == "10.0.0.0/16"
    assert str(resource) == str(resource2)


def test_issue_99_deepcopy():

    import terrascript.resource
    import copy

    resource = terrascript.resource.aws_vpc("example", cidr_block="10.0.0.0/16")
    resource2 = copy.deepcopy(resource)

    assert isinstance(resource2, terrascript.resource.aws_vpc)
    assert resource2.cidr_block == "10.0.0.0/16"
    assert str(resource) == str(resource2)


def test_issue_99_pickle():

    import terrascript.resource
    import pickle

    resource = terrascript.resource.aws_vpc("example", cidr_block="10.0.0.0/16")

    # pickle does not raise an exception
    pickle.dumps(resource)
