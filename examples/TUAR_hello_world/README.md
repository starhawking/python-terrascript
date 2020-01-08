# Terraform: Up & Running - Hello World

[Hello World](https://github.com/brikis98/terraform-up-and-running-code/tree/master/code/terraform/00-preface/hello-world)
example adapted from Yevgeniy Brikman's book [Terraform: Up & Running](https://www.terraformupandrunning.com/).

```json
{
  "provider": {
    "aws": [
      {
        "region": "us-east-2",
        "version": "~>2.0"
      }
    ]
  },
  "resource": {
    "aws_instance": {
      "example": {
        "ami": "ami-0c55b159cbfafe1f0",
        "instance_type": "t2.micro"
      }
    }
  }
}
```
