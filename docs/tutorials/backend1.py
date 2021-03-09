import terrascript

config = terrascript.Terrascript()

backend = terrascript.Backend(
    "local",
    path="example_app/terraform_state",
)

config += terrascript.Terraform(backend=backend)
