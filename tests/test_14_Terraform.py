import json

from terrascript import *


class Test_Terraform:
    def setup(self):
        self.config = Terrascript()

    def test_terraform(self):
        self.config += Terraform(required_version=">= 0.12.0", backend={
            's3': {
                'region': 'us-west-2',
                'bucket': 'acme-terraform-states'
            }
        })
        assert str(self.config) == json.dumps({
            "terraform": {
                "required_version": ">= 0.12.0",
                "backend": {
                    "s3": {
                        "region": "us-west-2",
                        "bucket": "acme-terraform-states"
                    }
                }
            }
        })

    def test_backend(self):
        new_config = Terrascript()
        new_config += Terraform().backend(
            's3',
            region='us-west-2',
            bucket='acme-terraform-states'
        )
        self.config += Terraform(backend={
            's3': {
                'region': 'us-west-2',
                'bucket': 'acme-terraform-states'
            }
        })
        assert str(self.config) == str(new_config)
