# Development

There are currently three streams of development, each if which is represented as a separate Git branch.

| Git branch       | Description                                            | Accepting Pull Requests |
|------------------|--------------------------------------------------------|-------------------------|
| ``develop``      | Terrascript 0.8.x releases supporting Terraform 0.12.x | No (see notes below)    |
| ``master ``      | Equals latest Terrascript 0.6.x release                | Never                   |
| ``develop-0.7``  | Terrascript 0.7.x releases supporting Terraform 0.12.x | Yes                     |
| ``develop-0.6``  | Terrascript 0.6.x releases supporting Terraform 0.11.x | Yes                     |

Please make sure to submit Pull Requests to the correct branch or I will have to reject them. 

The ``develop`` branch is currently undergoing a major re-write of the Python code and is likely to be a bit 
of a mess at this stage. 
