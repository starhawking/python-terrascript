# Locals

A local value assigns a name to an expression, allowing it to be used multiple times within a module without repeating it.

## When to use local values

Local values can be helpful to avoid repeating the same values or expressions multiple times in a configuration, but if overused they can also make a configuration hard to read by future maintainers by hiding the actual values used.

Use local values only in moderation, in situations where a single value or result is used in many places and that value is likely to be changed in future. The ability to easily change the value in a central place is the key advantage of local values.

## Example

```python
from terrascript import Terrascript
from terrascript import Locals
from terrascript import Provider

from terrascript.aws.r import aws_instance

ts = Terrascript()

ts += Provider('aws', access_key='ACCESS_KEY_HERE',
         secret_key='SECRET_KEY_HERE', region='us-east-1')

locals1 = Locals(instance_type='t2.micro')
locals2 = Locals(ami='ami-2757f631')
resource = aws_instance('instance1', instance_type=locals1.instance_type, ami=locals2.ami)

ts += locals1
ts += locals2
ts += resource

print(ts.dump())
```

Don't forget to run `terraform get` to download the module.

```json
{
    "provider": {
        "aws": {
            "access_key": "ACCESS_KEY_HERE",
            "secret_key": "SECRET_KEY_HERE",
            "region": "us-east-1"
        }
    },
    "locals": {
        "instance_type": "t2.micro",
        "ami": "ami-2757f631"
    },
    "resource": {
        "aws_instance": {
            "instance1": {
                "instance_type": "${locals.instance_type}",
                "ami": "${locals.ami}"
            }
        }
    }
}
```
