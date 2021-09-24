#
# Test that the providers available in Terraform 0.9.x are
# still available.
#
# Some providers in here are on the Terraform Provider Registry but are
# either not included in the API search results (bug?) or are community
# providers for which importing without namespace is not supported.
#
import terrascript.provider

terrascript.provider.alicloud
terrascript.provider.archive
# terrascript.provider.arukas        # Not in registry (1)
terrascript.provider.aws
terrascript.provider.azure  # Not included in https://registry.terraform.io/v1/providers/hashicorp?limit=100 (2)
terrascript.provider.azurerm
# terrascript.provider.bitbucket     # (2)
# terrascript.provider.chef          # (2)
terrascript.provider.circonus
# terrascript.provider.clc           # (2)
terrascript.provider.cloudflare
# terrascript.provider.cloudscale
# terrascript.provider.cloudstack
# terrascript.provider.cobbler
# terrascript.provider.datadog
terrascript.provider.digitalocean
# terrascript.provider.dme
terrascript.provider.dns
terrascript.provider.dnsimple
# terrascript.provider.docker
# terrascript.provider.dyn
terrascript.provider.external
terrascript.provider.fastly
terrascript.provider.github
# terrascript.provider.gitlab
terrascript.provider.google
terrascript.provider.google_beta
# terrascript.provider.grafana
terrascript.provider.helm
terrascript.provider.heroku
terrascript.provider.http
# terrascript.provider.icinga2
# terrascript.provider.ignition
# terrascript.provider.influxdb
terrascript.provider.kubernetes
# terrascript.provider.librato
terrascript.provider.local
# terrascript.provider.logentries
# terrascript.provider.logicmonitor
# terrascript.provider.mailgun
terrascript.provider.matchbox
# terrascript.provider.mysql
terrascript.provider.newrelic
terrascript.provider.nomad
terrascript.provider.ns1
terrascript.provider.oci
# terrascript.provider.oneandone
terrascript.provider.opc
# terrascript.provider.openstack
terrascript.provider.opsgenie
terrascript.provider.ovh
# terrascript.provider.packet
terrascript.provider.pagerduty
terrascript.provider.pingdom
terrascript.provider.postgresql
# terrascript.provider.powerdns
# terrascript.provider.profitbricks
terrascript.provider.rabbitmq
terrascript.provider.rancher
terrascript.provider.random
# terrascript.provider.rundeck
terrascript.provider.scaleway
terrascript.provider.shell
terrascript.provider.signalfx
# terrascript.provider.softlayer
# terrascript.provider.spotinst
# terrascript.provider.statuscake
terrascript.provider.template
terrascript.provider.tls
# terrascript.provider.triton
terrascript.provider.ultradns
terrascript.provider.vault
terrascript.provider.vcd
terrascript.provider.vsphere
