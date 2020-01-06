import terrascript

def test_lowercase():
    # Except locals, resource, data and provider.
    assert terrascript.Variable == terrascript.variable
    assert terrascript.Module == terrascript.module
    assert terrascript.Terraform == terrascript.terraform
    assert terrascript.Provisioner == terrascript.provisioner
    assert terrascript.Connection == terrascript.connection
    assert terrascript.Backend == terrascript.backend
    assert terrascript.Function == terrascript.function
