"""Issue 33: Suggestion of syntax to terrascript

   terrascript.Terrascript.add() method.
"""


import terrascript
import terrascript.provider
import terrascript.resource

def test_issue_33():
 
    ts = terrascript.Terrascript()

    var_access_key = ts.add(terrascript.Variable('access_key'))
    assert isinstance(var_access_key, terrascript.Variable)

    var_secret_key = ts.add(terrascript.Variable('secret_key'))
    assert isinstance(var_secret_key, terrascript.Variable)

    var_region = ts.add(terrascript.Variable('region', default='us-east-1'))
    assert isinstance(var_region, terrascript.Variable)

    ts += terrascript.provider.aws(access_key=var_access_key, 
                                   secret_key=var_secret_key, 
                                   region=var_region
    )

    assert ts['provider']['aws'][0]['access_key'] == 'var.access_key'
    assert ts['provider']['aws'][0]['secret_key'] == 'var.secret_key'
    assert ts['provider']['aws'][0]['region'] == 'var.region'

    # {
    #    "variable": {
    #    "access_key": {},
    #    "secret_key": {},
    #    "region": {
    #      "default": "us-east-1"
    #    }
    #  },
    #  "provider": {
    #    "aws": [
    #      {
    #        "access_key": "var.access_key",
    #        "secret_key": "var.secret_key",
    #        "region": "var.region"
    #      }
    #    ]
    #  }
    # }

