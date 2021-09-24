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

The root cause of the problem is that ```terraform``` is a top-level block and
also a provider with the ```terraform_remote_state```. 

"""

# The following code has been adapted to Terrascript release 0.10


def test_issue_43():

    import terrascript
    import terrascript.data.hashicorp.terraform
    import terrascript.provider.hashicorp.terraform

    s3_backend = terrascript.backend(
        "s3", bucket="mybucket", key="my.tfstate", region="us-east-1"
    )

    ts = terrascript.Terrascript()
    ts += terrascript.provider.hashicorp.terraform.terraform(backend=s3_backend)

    ts += terrascript.data.hashicorp.terraform.terraform_remote_state(
        "another",
        backend="s3",
        config={"bucket": "mybucket", "key": "another.tfstate", "region": "us-east-1"},
    )

    # The resulting JSON structure is
    #
    #   {
    #     "provider": {
    #       "terraform": [
    #         {
    #           "backend": {
    #             "bucket": "mybucket",
    #             "key": "my.tfstate",
    #             "region": "us-east-1"
    #           }
    #         }
    #       ]
    #     },
    #     "data": {
    #       "terraform_remote_state": {
    #         "another": {
    #           "backend": "s3",
    #           "config": {
    #             "bucket": "mybucket",
    #             "key": "another.tfstate",
    #             "region": "us-east-1"
    #           }
    #         }
    #       }
    #     }
    #   }
