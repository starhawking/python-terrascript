# Development

## Git branches

| Git branch       | Description                                            | Accepting Pull Requests |
|------------------|--------------------------------------------------------|-------------------------|
| ``develop``      | Current development, not meant for production          | Yes                     |
| ``develop-0.6``  | Terrascript 0.6.x releases supporting Terraform 0.11.x | Yes                     |
| ``master``       | Equals latest Terrascript release                      | Never                   |
| ``feature/*``    | Development of new "features"                          | Not generally           |

Please make sure to submit the Pull Requests to the correct branch or I will have to reject them. 

## Pull Requests

I am happy to accept Pull Requests against the ``develop`` and ``develop-0.6`` branches.

Before submitting a Pull Request, please... 
* Update [CHANGELOG.md](CHANGELOG.md)
* Add yourself to [CONTRIBUTORS.md](CONTRIBUTORS.md)

## Tests

Please include test cases for your code. The recommended approach is to 
* Create a new [issue](https://github.com/mjuenema/python-terrascript/issues) and note down the number.
* Create a ``tests/test_issue_NNN.py`` file containing your tests, replacing ``NNN`` with the issue number created in the previous step.

Check out the other files in ``tests/`` for examples.

## Examples

I'd love to start a collection of real-life Terrascript examples. I don't have any as I am (curiously enough)
not actually using Terrascript outside of developing its code. 
