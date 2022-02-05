# Development

## Status

Current development is towards the 0.10.0 release. The key change are that starting with this release the
provider modules are being auto-generated from data available from the Terraform Provider Registry. 

Release 0.10.0 will support Terraform 0.13 which introduced the ``required_providers`` statement.
The main outstanding task is to update the dcoumentation and examples to include ``required_providers``.

## Git branches

| Git branch       | Description                                            | Accepting Pull Requests |
|------------------|--------------------------------------------------------|-------------------------|
| ``develop``      | Current development, not meant for production          | Yes                     |
| ``feature/*``    | Development of new "features"                          | Not generally           |
| ``master``       | Equals latest Terrascript release                      | Never                   |
| ``release/*``    | Candidate for upcoming release                         | Not generally           |

Please make sure to submit the Pull Requests to the correct branch or we will have to reject them.  

## Pull Requests

We're happy to accept Pull Requests against the ``develop`` branch.  

Before submitting a Pull Request, please...  
* Update [CHANGELOG.md](CHANGELOG.md)  
* Add yourself to [CONTRIBUTORS.md](CONTRIBUTORS.md)  

When your pull request are approved, please merge it.  

## Tests

Please include test cases for your code. The recommended approach is to  
* Create a new [issue](https://github.com/starhawking/python-terrascript/issues) and note down the number.
* Create a ``tests/test_issue_NNN.py`` file containing your tests, replacing ``NNN`` with the issue number created in the previous step.  

Check out the other files in ``tests/`` for examples.

## Examples

We would love to start a collection of real-life Terrascript examples.  
If you have an example that you think would be a good demonstration of something currently missing, please make a PR.  
