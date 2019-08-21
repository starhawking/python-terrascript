from nose.tools import *
from shared import assert_equals_json
import json

import terrascript
import terrascript.aws.r

class Test_Output(object):

    def test_output_classes(self):

        output = terrascript.Output("name")
        assert isinstance(output, terrascript.Block)


    def test_output_example1(self):
        # https://www.terraform.io/docs/configuration/outputs.html

        resource = terrascript.Resource('name')
        output = terrascript.Output("ipaddress", value=resource.ipaddress)

        assert_equals_json(output, 'Output_output_example1.json')