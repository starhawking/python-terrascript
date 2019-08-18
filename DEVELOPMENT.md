# Development

* There are currently three main streams of development, which are represented as a separate Git ``develop*`` branches. 
* The ``master`` branch is not used for development. 
* Any ``feature/*`` branches are my own lines of development. I only push them to Github as a means of working on multiple computers.

| Git branch       | Description                                            | Accepting Pull Requests |
|------------------|--------------------------------------------------------|-------------------------|
| ``develop``      | Terrascript 0.8.x releases supporting Terraform 0.12.x | Not at the moment (*)   |
| ``develop-0.7``  | Terrascript 0.7.x releases supporting Terraform 0.12.x | Yes                     |
| ``develop-0.6``  | Terrascript 0.6.x releases supporting Terraform 0.11.x | Yes                     |
| ``master``       | Equals latest Terrascript 0.6.x release                | Never                   |
| ``feature/*``    | Development of new "features"                          | Not generally           |

Please make sure to submit the Pull Requests to the correct branch or I will have to reject them. 

(*) The ``develop`` branch is currently undergoing a major re-write of the Python code and is likely to be a bit 
of a mess at this stage. In fact, it is likely to not work at all.

## Pull Requests

I am happy to accept Pull Requests against the ``develop-0.6`` and ``develop-0.7`` branches. 

Before submitting a Pull Request, please ensure that you have updated the following files.
* [CHANGELOG.md](CHANGELOG.md)
* [CONTRIBUTORS.md](CONTRIBUTORS.md)

I will manually merge them into the ``develop`` branch.

## Tests

Please include test cases for your code. The recommended approach is to 
* Create a new [issue](https://github.com/mjuenema/python-terrascript/issues) and note down the number.
* Create a ``tests/test_issueNN.py`` file containing your tests, replacing ``NN`` with the issue number created in the previous step.
* If applicable, create **valid** Terraform configurations in JSON format as ``tests/configs/issueNN-DESCRIPTION.tf.json``, replacing ``NN`` with the issue number.

Check out the other files in ``tests/`` for examples.
