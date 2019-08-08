# Locals

A local value assigns a name to an expression, allowing it to be used multiple times within a module without repeating it.

## When to use local values

Local values can be helpful to avoid repeating the same values or expressions multiple times in a configuration, but if overused they can also make a configuration hard to read by future maintainers by hiding the actual values used.

Use local values only in moderation, in situations where a single value or result is used in many places and that value is likely to be changed in future. The ability to easily change the value in a central place is the key advantage of local values.

## Example

```python
from terrascript import Terrascript
from terrascript import Locals
from terrascript import provider

from terrascript.aws.r import aws_instance

ts = Terrascript()

ts.add(provider('aws', access_key='ACCESS_KEY_HERE', 
         secret_key='SECRET_KEY_HERE', region='us-east-1'))

instances = []
instance_example1 = ts.add(aws_instance('example1', ami='ami-2757f631', instance_type='t2.micro'))
instances.append(instance_example1)

instance_example2 = ts.add(aws_instance('example2', ami='ami-2757f631', instance_type='t2.micro'))
instances.append(instance_example2)

local_values = ts.add(Locals(
  # Ids for multiple sets of EC2 instances, merged together
  instance_ids=','.join([x.ipv4_address for x in instances]),
))

print(ts.dump())
```

Don't forget to run `terraform get` to download the module.

```json
{
  "locals": {
    "instance_ids": "${aws_instance.example1.ipv4_address},${aws_instance.example2.ipv4_address}"
  },
  "provider": {
    "aws": {
      "__DEFAULT__": {
        "access_key": "ACCESS_KEY_HERE",
        "region": "us-east-1",
        "secret_key": "SECRET_KEY_HERE"
      }
    }
  },
  "resource": {
    "aws_instance": {
      "example1": {
        "ami": "ami-2757f631",
        "instance_type": "t2.micro"
      },
      "example2": {
        "ami": "ami-2757f631",
        "instance_type": "t2.micro"
      }
    }
  }
}
```