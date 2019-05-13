# Backends

```python
from terrascript import terraform, backend, Terrascript

ts = Terrascript()
consul_backend = backend("consul",
                         address='demo.consul.io',
                         path='getting-started-RANDOMSTRING',
                         lock=False)
                         
ts += terraform(backend=consul_backend)

print(ts.dump())
```

The JSON configuration will tell Terraform to use the Consul key-value store as backend.

```json
{
  "terraform": {
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

