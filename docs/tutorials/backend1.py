import terrascript

config = terrascript.Terrascript()

backend = terrascript.Backend(
    "consul",
    address="demo.consul.io",
    scheme="https",
    path="example_app/terraform_state",
)

config += terrascript.Terraform(backend=backend)
