# Example: Webserver Cluster Module

This example is loosely based on an example from chapter 4 of the book
[Terraform: Up and Running](http://www.terraformupandrunning.com/) by Yevgenij Brikman.
The original code can be found in the
[book's Github repository](https://github.com/brikis98/terraform-up-and-running-code/tree/master/code/terraform/04-terraform-module/module-example).

This **Terrascript** adaption makes the following changes.

* The `webserver-cluster` Terraform module is implemented as a Python function which accepts the inputs as
  arguments and returns some resources as a tuple.
* The `user_data` of the `launch_configuration` is rendered with Python's `format()`
  method instead of Terraform's `template_file` data source. For more advanced
  scenarios one could even use [Jinja2](https://pypi.python.org/pypi/Jinja2).
* All code is contained in a single file. General purpose modules/functions should
  probably go into a separate Python module.
* The backend database has been omitted.

The file [main.tf.json](main.tf.json) was created by running [main.py](main.py).
