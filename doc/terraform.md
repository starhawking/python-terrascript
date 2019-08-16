# Terraform Settings

```python
from terrascript import Terrascript, Terraform

ts = Terrascript()
consul_backend = Terraform(
    required_version=">= 0.12.0"
).backend(
    "consul",
    address='demo.consul.io',
    path='getting-started-RANDOMSTRING',
    lock=False
)

ts += consul_backend        

print(str(ts))
```

The JSON configuration will tell Terraform to use the Consul key-value store as backend.

```json
{
  "terraform": {
    "required_version": ">= 0.12.0",
    "backend": {
      "consul": {
        "address": "demo.consul.io",
        "lock": false,
        "path": "getting-started-RANDOMSTRING"
      }
    }
  }
}
```
