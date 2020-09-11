import terrascript
import terrascript.provider

config = terrascript.Terrascript()

# Amazon Web Service with aliases
config += terrascript.provider.aws(alias="east", region="us-east-1")
config += terrascript.provider.aws(alias="west", region="us-west-1")
