"""
Test for Github issue 3: Work-around for data/JSON bug 

https://github.com/mjuenema/python-terrascript/issues/3

Test for comment by @nielsonsantana on 29-April-2018

"""

import terrascript
import terrascript.aws.d

def test_issue3b():
    """Issue 3(b): Work-around for data/JSON bug"""
    
    ts = terrascript.Terrascript()
    ts += terrascript.provider("aws", region = "us-east-1")

    ts += terrascript.aws.d.aws_vpc('selected', id=1)

    assert ts.validate() == True