locals {
  service_name = "forum"
  owner        = "Community Team"
}

locals {
  common_tags = {
    Service = local.service_name
    Owner   = local.owner
  }
}
