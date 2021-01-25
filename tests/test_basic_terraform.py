import terrascript
import terrascript.resource


class TestTerraform:
    def __init__(self):
        self.cfg = terrascript.Terrascript()

    def test_one_setting(self):
        assert "terraform" not in self.cfg

        self.cfg += terrascript.terraform(backend=terrascript.backend("azurerm"))

        assert self.cfg.get("terraform") == {"backend": {"azurerm": {}}}

    def test_multiple_settings__added_at_once(self):
        assert "terraform" not in self.cfg

        self.cfg += terrascript.terraform(
            backend=terrascript.backend("azurerm"), required_version="0.14.0"
        )

        print(self.cfg["terraform"])
        assert self.cfg.get("terraform") == {
            "backend": {"azurerm": {}},
            "required_version": "0.14.0",
        }

    def test_multiple_settings__append_to_existing(self):
        expected_result = {"backend": {"azurerm": {}}, "required_version": "0.14.0"}

        assert "terraform" not in self.cfg

        self.cfg += terrascript.terraform(backend=terrascript.backend("azurerm"))
        self.cfg += terrascript.terraform(
            required_version=expected_result["required_version"]
        )

        print(self.cfg["terraform"])
        assert self.cfg.get("terraform") == expected_result

    def test_multiple_settings__append_to_nested_existing(self):
        expected_result = {
            "required_providers": {
                "aws": {"source": "hashicorp/aws", "version": "~> 3.0"}
            }
        }

        assert "terraform" not in self.cfg

        self.cfg += terrascript.terraform(
            required_providers={"aws": {"source": "hashicorp/aws"}}
        )
        self.cfg += terrascript.terraform(
            required_providers={"aws": {"version": "~> 3.0"}}
        )

        print(self.cfg["terraform"])
        assert self.cfg.get("terraform") == expected_result
