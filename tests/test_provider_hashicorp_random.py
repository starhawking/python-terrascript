# tests/test_provider_hashicorp_random.py
# Automatically generated by tools/makecode.py (24-Sep-2021 15:25:40 UTC)


def test_provider_import():
    import terrascript.provider.hashicorp.random


def test_resource_import():
    from terrascript.resource.hashicorp.random import random_id

    from terrascript.resource.hashicorp.random import random_integer

    from terrascript.resource.hashicorp.random import random_password

    from terrascript.resource.hashicorp.random import random_pet

    from terrascript.resource.hashicorp.random import random_shuffle

    from terrascript.resource.hashicorp.random import random_string

    from terrascript.resource.hashicorp.random import random_uuid


# TODO: Shortcut imports without namespace for official and supported providers.

# TODO: This has to be moved into a required_providers block.
# def test_version_source():
#
#      import terrascript.provider.hashicorp.random
#
#      t = terrascript.provider.hashicorp.random.random()
#      s = str(t)
#
#      assert 'https://github.com/hashicorp/terraform-provider-random' in s
#      assert '3.1.0' in s
