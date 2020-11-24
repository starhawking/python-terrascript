import terrascript
import terrascript.provider


class TestVariable:
    def __init__(self):
        self.cfg = terrascript.Terrascript()

    def test_one_variable(self):
        v = terrascript.Variable("name", type="string", default="Hello World")
        assert isinstance(v, terrascript.NamedBlock)
        assert isinstance(v, terrascript.Variable)
        assert v._name == "name"
        assert v["type"] == "string"
        assert v["default"] == "Hello World"

        self.cfg += v
        assert len(self.cfg["variable"].keys()) == 1
        assert self.cfg["variable"]["name"]["type"] == "string"
        assert self.cfg["variable"]["name"]["default"] == "Hello World"

    def test_two_variables(self):
        v1 = terrascript.Variable("name1", type="string", default="Me")
        v2 = terrascript.Variable("name2", type="string", default="You")

        self.cfg += v1
        self.cfg += v2

        assert len(self.cfg["variable"].keys()) == 2
        assert self.cfg["variable"]["name1"]["type"] == "string"
        assert self.cfg["variable"]["name1"]["default"] == "Me"
        assert self.cfg["variable"]["name2"]["type"] == "string"
        assert self.cfg["variable"]["name2"]["default"] == "You"

    def test_duplicate_names(self):
        v1 = terrascript.Variable("name", type="string", default="Me")
        v2 = terrascript.Variable("name", type="string", default="You")

        self.cfg += v1
        self.cfg += v2  # Overwrites v1

        assert len(self.cfg["variable"].keys()) == 1
        assert self.cfg["variable"]["name"]["type"] == "string"
        assert self.cfg["variable"]["name"]["default"] == "You"

    def test_string_interpolation(self):
        var = terrascript.Variable("myvar", type="string", default="myval")

        expected_value = "${var.myvar}"
        assert expected_value == str(
            var
        ), "String interpolation of variable did not return its reference"
        assert expected_value == repr(
            var
        ), "String representation of variable did not return its reference"

        expected_value = "embeded-${var.myvar}"
        assert (
            expected_value == f"embeded-{var}"
        ), "Formatting a string with variable did not insert reference"

    def test_adding_variable_to_block(self):
        """ Variables added to Block should be added as reference """
        var = terrascript.Variable("myvar", type="string", default="value")
        resource = terrascript.Block(variable=var)

        assert (
            "${var.myvar}" == resource["variable"]
        ), "Adding Variable to Block did not insert reference"

    def test_adding_variable_to_resource(self):
        """ Variables added to Resource should be added as reference """
        var = terrascript.Variable("myvar", type="string", default="value")
        resource = terrascript.Resource("Test", var=var)

        assert (
            "${var.myvar}" == resource.var
        ), "Adding Variable to Resource did not insert reference"
