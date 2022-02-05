"""
Test for Github issue 31: Add (test) for vault provider

https://github.com/starhawking/python-terrascript/issues/31

"""

import terrascript
import terrascript.provider.hashicorp.vault


def test_issue_31():

    ts = terrascript.Terrascript()
    ts += terrascript.provider.hashicorp.vault.vault(
        address="https://address.to.vault.provider:1234", token="TOKEN"
    )
    assert ts["provider"]["vault"][0]["token"] == "TOKEN"
