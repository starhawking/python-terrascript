# Why no error checking?

**Terrascript** does not perform any error checking whatsoever! This was a deliberate design decision to keep 
the code simple. Therefore it is perfectly possible to generate JSON output that Terraform will later reject.

```python
from terrascript import dump, function
from terrascript.aws.r import aws_instance

aws_instance('myinstance', foo=function.bar('hello world'))

print(dump())

```

Terraform will reject the generated JSON as the `aws_instance` resource does not accept a `foo` argument and
there is also no function `bar()`.

```json
{
  "resource": {
    "aws_instance": {
      "myinstance": {
        "foo": "${bar(\"hello world\")}"
      }
    }
  }
}
```

At an early stage I contemplated parsing the Terraform Go source code and auto-create Python
code that does indeed verify whether the generated JSON configuration is valid Terraform input. This attempt
proved much too difficult so I abandonded that approach.
