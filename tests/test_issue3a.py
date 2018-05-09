"""
Test for Github issue 3: Work-around for data/JSON bug 

https://github.com/mjuenema/python-terrascript/issues/3

Test for comment by @jbscare on 28-April-2018

"""

import json
import terrascript
import terrascript.aws.d
import terrascript.aws.r

def test_issue3a():
    """Issue 3(a): Work-around for data/JSON bug"""
    
    ts = terrascript.Terrascript()
    ts += terrascript.provider\
          ("aws",
           region = "us-east-1")
    
    policydict = {
        "Version": "2012-10-17",
        "Statement": [{"Action": "s3:*", "Resource": "*"}]}
    
    ts += terrascript.aws.r.iam_policy\
          ("jbstest_works",
           name = "jbstest_works",
           policy = json.dumps(policydict, sort_keys=True))
    
    ts += terrascript.aws.d.aws_iam_policy_document\
          ("jbstest",
           statement = [{
               "actions": ["s3:*"],
               "resources": ["*"]
               }]
           )
    
    ts += terrascript.aws.r.iam_policy\
          ("jbstest_fails",
           name = "jbstest_fails",
           policy = "${data.aws_iam_policy_document.jbstest.json}")
           
    assert ts.validate() == True
