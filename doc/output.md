# Terraform Outputs

```python
from terrascript import Terrascript, Output

ts = Terrascript()
my_output = Output('name', 'my_value')

ts += my_output        

print(str(ts))
```

The Terraform JSON configuration:

```json
{
  "output": {
    "name": {
      "value": "my_value"
    }
  }
}
```
