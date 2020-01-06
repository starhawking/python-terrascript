import terrascript
import terrascript.provider
import terrascript.resource

config = terrascript.Terrascript()

config += terrafor.provider.aws(region='us-east-1')
    
i = terrascript.resource.aws_instance('myinstance', foo='bar')
config += i
    
# AWS Instance resource does not have a `foo` but accepts it anyway.
assert i.foor == 'bar'
