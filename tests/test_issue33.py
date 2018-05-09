


from terrascript import Terrascript
from terrascript import provider
from terrascript import output
from terrascript import variable
from terrascript.aws.r import aws_instance


def test_issue33():
    """Issue 33: Suggestion of syntax to terrascript"""

    ts = Terrascript()

    var_access_key = ts.add(variable('access_key'))
    assert isinstance(var_access_key, variable)

    var_secret_key = ts.add(variable('secret_key'))
    assert isinstance(var_secret_key, variable)

    var_region = ts.add(variable('region', default='us-east-1'))
    assert isinstance(var_region, variable)

    ts += provider('aws', access_key=var_access_key, 
                   secret_key=var_secret_key, region=var_region
    )

    resource_aws_instance = ts.add(aws_instance('example', ami='ami-2757f631', instance_type='t2.micro'))
    assert isinstance(resource_aws_instance, aws_instance)

    ts += output('example_public_ip', value=resource_aws_instance.public_ip, 
                 description='Public IP of example')

    assert ts.validate() is True
