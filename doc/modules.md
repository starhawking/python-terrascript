# Modules

The ``module`` class is used to reference Terraform modules. This is probably most useful to include
third-party modules as one could use Python functions to emulate modules.

```python
from terrascript import provider, dump, module

provider('aws', access_key='ACCESS_KEY_HERE', 
         secret_key='SECRET_KEY_HERE', region='us-east-1')

module("consul", source='github.com/hashicorp/consul/terraform/aws',
       key_name='AWS SSH KEY NAME', key_path='PATH TO ABOVE PRIVATE KEY',
       region='us-east-1', servers=3)
       
print(dump())
```

Don't forget to run `terraform get` to download the module.

```json
{
  "module": {
    "consul": {
      "key_name": "AWS SSH KEY NAME",
      "key_path": "PATH TO ABOVE PRIVATE KEY",
      "region": "us-east-1",
      "servers": 3,
      "source": "github.com/hashicorp/consul/terraform/aws"
    }
  },
  "provider": {
    "aws": {
      "access_key": "ACCESS_KEY_HERE",
      "region": "us-east-1",
      "secret_key": "SECRET_KEY_HERE"
    }
  }
}
```