from nose.tools import *
from shared import *
import json

import terrascript
import terrascript.aws.r

class Test_Variable(object):

    def test_variable_example1(self):
        # https://www.terraform.io/docs/configuration/variables.html

        variable = terrascript.Variable('image_id')

        assert_equals_json(variable, 'Variable_variable_example1.json')


    def test_variable_example2(self):
        # https://www.terraform.io/docs/configuration/variables.html

        variable = terrascript.Variable('availability_zone_names',
                                        type="list(string)",
                                        default=["us-west-1a"]
                                        )

        assert_equals_json(variable, 'Variable_variable_example2.json')


    def test_variable_in_resource(self):
        # https://www.terraform.io/docs/configuration/variables.html

        ami = terrascript.Variable('image_id')

        aws_instance = terrascript.aws.r.aws_instance("example",
                                                      instance_type="t2.micro",
                                                      ami=ami)

        assert_equals_json(aws_instance, 'Variable_variable_in_resource.json')