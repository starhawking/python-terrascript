
from terrascript import Terrascript
from terrascript import provider
from terrascript import variable
from terrascript.aws.r import aws_instance


def test_update_override_value():
    ts = Terrascript()
    ts2 = Terrascript()

    ts.add(variable('access_key'))
    ts.add(variable('secret_key'))

    var_region = ts.add(variable('region', default='us-east-1'))
    var_region2 = ts2.add(variable('region', default='ca-central-1'))

    assert var_region._kwargs['default'] != var_region2._kwargs['default']

    # ts2 override variable "region" in ts
    ts.update(ts2)
    assert isinstance(ts, Terrascript)
    assert isinstance(ts2, Terrascript)

    ts_variables = ts.config.get('variable', {})
    assert len(ts_variables.items()) == 3  # ensure that only three

    ts_var_region = ts_variables.get('region', {})
    assert ts_var_region.get('default', '') == var_region2._kwargs.get('default')

    assert ts.validate(delete=False) is True


def test_update_add_value():
    ts = Terrascript()
    ts2 = Terrascript()

    var_access_key = ts.add(variable('access_key'))
    var_secret_key = ts.add(variable('secret_key'))
    var_region = ts.add(variable('region', default='us-east-1'))

    ts += provider('aws', access_key=var_access_key,
                   secret_key=var_secret_key, region=var_region)

    resource_aws_instance = ts.add(aws_instance(
        'example', ami='ami-2757f631', instance_type='t2.micro'
    ))
    resource_aws_instance_2 = ts2.add(aws_instance(
        'example_second', ami='ami-2757f631', instance_type='t2.micro'
    ))
    assert isinstance(resource_aws_instance, aws_instance)
    assert isinstance(resource_aws_instance_2, aws_instance)

    # ts2 add resource "example_second" to ts
    ts.update(ts2)
    assert isinstance(ts, Terrascript)
    assert isinstance(ts2, Terrascript)

    ts_resources = ts.config.get('resource', {})
    assert len(ts_resources.items()) == 1
    ts_aws_instances = ts_resources.get('aws_instance')
    assert len(ts_aws_instances.items()) == 2

    assert resource_aws_instance._name in ts_aws_instances.keys()
    assert resource_aws_instance_2._name in ts_aws_instances.keys()

    assert ts.validate(delete=False) is True


def test_update_raise_error():
    ts = Terrascript()
    var_region = variable('region')
    exception_raised = False
    try:
        ts.update(var_region)
    except TypeError as e:
        exception_raised = True

    assert exception_raised is True
