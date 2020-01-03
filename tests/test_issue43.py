"""
https://github.com/mjuenema/python-terrascript/issues/43

I have a script like this:

    s3_backend = terrascript.backend(
        "s3",
        bucket = "mybucket",
        key = "my.tfstate",
        region = "us-east-1"
        )

    ts = terrascript.Terrascript()
    ts += terrascript.terraform(backend = s3_backend)

    ts += terrascript.terraform.d.remote_state(
        "another",
        backend = "s3",
        config = {
            'bucket': "mybucket",
            'key': "another.tfstate",
            'region': "us-east-1"
            }
        )

If I run this, I get an error:

    Traceback (most recent call last):
    File "terrascript-modules.py", line 15, in <module>
        ts += terrascript.terraform.d.remote_state(
    AttributeError: type object 'terraform' has no attribute 'd'


"""

# The following code has been adapted to Terrascript release 0.8.0.
# Any changes have been commented in the code.

def test_issue43():

    import terrascript
    import terrascript.data                           # <=== Use new module layout.

    s3_backend = terrascript.backend(                 # <=== or, terrascript.Backend()
        "s3",
        bucket = "mybucket",
        key = "my.tfstate",
        region = "us-east-1"
        )

    ts = terrascript.Terrascript()
    ts += terrascript.terraform(backend = s3_backend)

    ts += terrascript.data.terraform_remote_state(    # <=== Use new module layout.
        "another",
        backend = "s3",
        config = {
            'bucket': "mybucket",
            'key': "another.tfstate",
            'region': "us-east-1"
            }
        )