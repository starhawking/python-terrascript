"""
Test for Github issue 31: Add (test) for vault provider

https://github.com/mjuenema/python-terrascript/issues/31

"""

from terrascript import *

def test_issue31():
    """Issue 31: Add (test) for vault provider"""
    
    ts = Terrascript()
    ts += provider('vault', address='https://address.to.vault.provider:1234', token='TOKEN')
    assert ts.validate() is True
