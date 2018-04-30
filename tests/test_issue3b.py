"""
Test for Github issue 3: Work-around for data/JSON bug 

https://github.com/mjuenema/python-terrascript/issues/3

Test for comment by @nielsonsantana on 29-April-2018

"""

import terrascript

def test_issue3b():
    """Issue 3: Work-around for data/JSON bug (a)"""
    
    ts = terrascript.Terrascript()
    ts += terrascript.provider\
          ("aws",
           region = "us-east-1")

    ts += terrascript.aws.d.aws_vpc('selected', id=vpc_id, default_attrs=False)
    
    # policydict = {
    #     "Version": "2012-10-17",
    #     "Statement": [{"Action": "s3:*", "Resource": "*"}]}
    
    # ts += terrascript.aws.r.iam_policy\
    #       ("jbstest_works",
    #       name = "jbstest_works",
    #       policy = json.dumps(policydict, sort_keys=True))
    
    # ts += terrascript.aws.d.aws_iam_policy_document\
    #       ("jbstest",
    #       statement = [{
    #           "actions": ["s3:*"],
    #           "resources": ["*"]
    #           }]
    #       )
    
    # ts += terrascript.aws.r.iam_policy\
    #       ("jbstest_fails",
    #       name = "jbstest_fails",
    #       policy = "${data.aws_iam_policy_document.jbstest.json}")
           
    assert ts.validate(delete=False) == True