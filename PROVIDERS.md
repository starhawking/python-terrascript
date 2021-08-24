## List of providers
    
This document lists the *Terraform* providers that are currently supported by *Terrascript*.

- [Official providers](#official-providers)
- [Partner providers](#partner-providers)
- [Community providers](#community-providers)
- [Unsupported providers](#unsupported-providers)
    
### Official providers

Official providers can be imported with or without namespace.

```python
# With namespace
import provider.hashicorp.aws
import resource.hashicorp.aws
import data.hashicorp.aws

# Without namespace
import provider.aws
import resource.aws
import data.aws
```
    
*Terrascript* currently supports the following official *Terraform* providers.
- [ad](https://registry.terraform.io/providers/hashicorp/ad/0.4.3) (hashicorp/ad/0.4.3)
- [alicloud](https://registry.terraform.io/providers/hashicorp/alicloud/1.132.0) (hashicorp/alicloud/1.132.0)
- [archive](https://registry.terraform.io/providers/hashicorp/archive/2.2.0) (hashicorp/archive/2.2.0)
- [aws](https://registry.terraform.io/providers/hashicorp/aws/3.55.0) (hashicorp/aws/3.55.0)
- [azuread](https://registry.terraform.io/providers/hashicorp/azuread/1.6.0) (hashicorp/azuread/1.6.0)
- [azurerm](https://registry.terraform.io/providers/hashicorp/azurerm/2.73.0) (hashicorp/azurerm/2.73.0)
- [azurestack](https://registry.terraform.io/providers/hashicorp/azurestack/0.10.0) (hashicorp/azurestack/0.10.0)
- [boundary](https://registry.terraform.io/providers/hashicorp/boundary/1.0.4) (hashicorp/boundary/1.0.4)
- [ciscoasa](https://registry.terraform.io/providers/hashicorp/ciscoasa/1.2.0) (hashicorp/ciscoasa/1.2.0)
- [cloudinit](https://registry.terraform.io/providers/hashicorp/cloudinit/2.2.0) (hashicorp/cloudinit/2.2.0)
- [consul](https://registry.terraform.io/providers/hashicorp/consul/2.13.0) (hashicorp/consul/2.13.0)
- [dns](https://registry.terraform.io/providers/hashicorp/dns/3.2.1) (hashicorp/dns/3.2.1)
- [external](https://registry.terraform.io/providers/hashicorp/external/2.1.0) (hashicorp/external/2.1.0)
- [fakewebservices](https://registry.terraform.io/providers/hashicorp/fakewebservices/0.2.1) (hashicorp/fakewebservices/0.2.1)
- [github](https://registry.terraform.io/providers/hashicorp/github/4.13.0) (hashicorp/github/4.13.0)
- [google](https://registry.terraform.io/providers/hashicorp/google/3.81.0) (hashicorp/google/3.81.0)
- [google-beta](https://registry.terraform.io/providers/hashicorp/google-beta/3.81.0) (hashicorp/google-beta/3.81.0)
- [googleworkspace](https://registry.terraform.io/providers/hashicorp/googleworkspace/0.4.1) (hashicorp/googleworkspace/0.4.1)
- [hcp](https://registry.terraform.io/providers/hashicorp/hcp/0.14.0) (hashicorp/hcp/0.14.0)
- [hcs](https://registry.terraform.io/providers/hashicorp/hcs/0.3.0) (hashicorp/hcs/0.3.0)
- [helm](https://registry.terraform.io/providers/hashicorp/helm/2.2.0) (hashicorp/helm/2.2.0)
- [http](https://registry.terraform.io/providers/hashicorp/http/2.1.0) (hashicorp/http/2.1.0)
- [kubernetes](https://registry.terraform.io/providers/hashicorp/kubernetes/2.4.1) (hashicorp/kubernetes/2.4.1)
- [kubernetes-alpha](https://registry.terraform.io/providers/hashicorp/kubernetes-alpha/0.6.0) (hashicorp/kubernetes-alpha/0.6.0)
- [local](https://registry.terraform.io/providers/hashicorp/local/2.1.0) (hashicorp/local/2.1.0)
- [nomad](https://registry.terraform.io/providers/hashicorp/nomad/1.4.15) (hashicorp/nomad/1.4.15)
- [null](https://registry.terraform.io/providers/hashicorp/null/3.1.0) (hashicorp/null/3.1.0)
- [oci](https://registry.terraform.io/providers/hashicorp/oci/4.40.0) (hashicorp/oci/4.40.0)
- [opc](https://registry.terraform.io/providers/hashicorp/opc/1.4.1) (hashicorp/opc/1.4.1)
- [oraclepaas](https://registry.terraform.io/providers/hashicorp/oraclepaas/1.5.3) (hashicorp/oraclepaas/1.5.3)
- [random](https://registry.terraform.io/providers/hashicorp/random/3.1.0) (hashicorp/random/3.1.0)
- [template](https://registry.terraform.io/providers/hashicorp/template/2.2.0) (hashicorp/template/2.2.0)
- [terraform](https://registry.terraform.io/providers/hashicorp/terraform/1.0.2) (hashicorp/terraform/1.0.2)
- [tfe](https://registry.terraform.io/providers/hashicorp/tfe/0.25.3) (hashicorp/tfe/0.25.3)
- [time](https://registry.terraform.io/providers/hashicorp/time/0.7.2) (hashicorp/time/0.7.2)
- [tls](https://registry.terraform.io/providers/hashicorp/tls/3.1.0) (hashicorp/tls/3.1.0)
- [vault](https://registry.terraform.io/providers/hashicorp/vault/2.23.0) (hashicorp/vault/2.23.0)
- [vsphere](https://registry.terraform.io/providers/hashicorp/vsphere/2.0.2) (hashicorp/vsphere/2.0.2)

### Partner providers

Partner providers can be imported with or without namespace.

```python
# With namespace
import provider.akamai.akamai
import resource.akamai.akamai
import data.akamai.akamai

# Without namespace
import provider.akamai
import resource.akamai
import data.akamai
```

*Terrascript* currently supports the following partner *Terraform* providers.
- [akamai](https://registry.terraform.io/providers/akamai/akamai/1.7.0) (akamai/akamai/1.7.0)
- [alicloud](https://registry.terraform.io/providers/aliyun/alicloud/1.132.0) (aliyun/alicloud/1.132.0)
- [amixr](https://registry.terraform.io/providers/alertmixer/amixr/0.2.3) (alertmixer/amixr/0.2.3)
- [avi](https://registry.terraform.io/providers/vmware/avi/21.1.1) (vmware/avi/21.1.1)
- [aviatrix](https://registry.terraform.io/providers/AviatrixSystems/aviatrix/2.20.0) (AviatrixSystems/aviatrix/2.20.0)
- [azurecaf](https://registry.terraform.io/providers/aztfmod/azurecaf/1.2.5) (aztfmod/azurecaf/1.2.5)
- [bigip](https://registry.terraform.io/providers/F5Networks/bigip/1.11.0) (F5Networks/bigip/1.11.0)
- [brightbox](https://registry.terraform.io/providers/brightbox/brightbox/2.0.6) (brightbox/brightbox/2.0.6)
- [circonus](https://registry.terraform.io/providers/circonus-labs/circonus/0.12.0) (circonus-labs/circonus/0.12.0)
- [cloudflare](https://registry.terraform.io/providers/cloudflare/cloudflare/2.25.0) (cloudflare/cloudflare/2.25.0)
- [cloudsmith](https://registry.terraform.io/providers/cloudsmith-io/cloudsmith/0.0.6) (cloudsmith-io/cloudsmith/0.0.6)
- [databricks](https://registry.terraform.io/providers/databrickslabs/databricks/0.3.7) (databrickslabs/databricks/0.3.7)
- [datadog](https://registry.terraform.io/providers/DataDog/datadog/3.2.0) (DataDog/datadog/3.2.0)
- [digitalocean](https://registry.terraform.io/providers/digitalocean/digitalocean/2.11.1) (digitalocean/digitalocean/2.11.1)
- [exoscale](https://registry.terraform.io/providers/exoscale/exoscale/0.28.0) (exoscale/exoscale/0.28.0)
- [fastly](https://registry.terraform.io/providers/fastly/fastly/0.34.0) (fastly/fastly/0.34.0)
- [fortimanager](https://registry.terraform.io/providers/fortinetdev/fortimanager/1.3.4) (fortinetdev/fortimanager/1.3.4)
- [fortios](https://registry.terraform.io/providers/fortinetdev/fortios/1.13.1) (fortinetdev/fortios/1.13.1)
- [gridscale](https://registry.terraform.io/providers/gridscale/gridscale/1.12.0) (gridscale/gridscale/1.12.0)
- [hcloud](https://registry.terraform.io/providers/hetznercloud/hcloud/1.30.0) (hetznercloud/hcloud/1.30.0)
- [heroku](https://registry.terraform.io/providers/heroku/heroku/4.6.0) (heroku/heroku/4.6.0)
- [launchdarkly](https://registry.terraform.io/providers/launchdarkly/launchdarkly/1.7.0) (launchdarkly/launchdarkly/1.7.0)
- [linode](https://registry.terraform.io/providers/linode/linode/1.20.2) (linode/linode/1.20.2)
- [mongodbatlas](https://registry.terraform.io/providers/mongodb/mongodbatlas/1.0.0) (mongodb/mongodbatlas/1.0.0)
- [ncloud](https://registry.terraform.io/providers/NaverCloudPlatform/ncloud/2.1.1) (NaverCloudPlatform/ncloud/2.1.1)
- [netapp-cloudmanager](https://registry.terraform.io/providers/NetApp/netapp-cloudmanager/21.8.1) (NetApp/netapp-cloudmanager/21.8.1)
- [netapp-elementsw](https://registry.terraform.io/providers/NetApp/netapp-elementsw/20.11.0) (NetApp/netapp-elementsw/20.11.0)
- [netapp-gcp](https://registry.terraform.io/providers/NetApp/netapp-gcp/21.5.0) (NetApp/netapp-gcp/21.5.0)
- [newrelic](https://registry.terraform.io/providers/newrelic/newrelic/2.25.0) (newrelic/newrelic/2.25.0)
- [ns1](https://registry.terraform.io/providers/ns1-terraform/ns1/1.11.0) (ns1-terraform/ns1/1.11.0)
- [nsxt](https://registry.terraform.io/providers/vmware/nsxt/3.2.3) (vmware/nsxt/3.2.3)
- [oktaasa](https://registry.terraform.io/providers/oktadeveloper/oktaasa/1.0.1) (oktadeveloper/oktaasa/1.0.1)
- [onelogin](https://registry.terraform.io/providers/onelogin/onelogin/0.1.23) (onelogin/onelogin/0.1.23)
- [opsgenie](https://registry.terraform.io/providers/opsgenie/opsgenie/0.6.5) (opsgenie/opsgenie/0.6.5)
- [pagerduty](https://registry.terraform.io/providers/PagerDuty/pagerduty/1.10.1) (PagerDuty/pagerduty/1.10.1)
- [pnap](https://registry.terraform.io/providers/phoenixnap/pnap/0.6.0) (phoenixnap/pnap/0.6.0)
- [rancher2](https://registry.terraform.io/providers/rancher/rancher2/1.17.1) (rancher/rancher2/1.17.1)
- [rke](https://registry.terraform.io/providers/rancher/rke/1.2.3) (rancher/rke/1.2.3)
- [scaleway](https://registry.terraform.io/providers/scaleway/scaleway/2.1.0) (scaleway/scaleway/2.1.0)
- [sdm](https://registry.terraform.io/providers/strongdm/sdm/1.0.27) (strongdm/sdm/1.0.27)
- [sematext](https://registry.terraform.io/providers/sematext/sematext/0.4.0) (sematext/sematext/0.4.0)
- [signalfx](https://registry.terraform.io/providers/splunk-terraform/signalfx/6.7.6) (splunk-terraform/signalfx/6.7.6)
- [stackpath](https://registry.terraform.io/providers/stackpath/stackpath/1.3.3) (stackpath/stackpath/1.3.3)
- [sumologic](https://registry.terraform.io/providers/SumoLogic/sumologic/2.9.9) (SumoLogic/sumologic/2.9.9)
- [tencentcloud](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/1.58.4) (tencentcloudstack/tencentcloud/1.58.4)
- [transloadit](https://registry.terraform.io/providers/transloadit/transloadit/0.4.0) (transloadit/transloadit/0.4.0)
- [turbot](https://registry.terraform.io/providers/turbot/turbot/1.8.2) (turbot/turbot/1.8.2)
- [vcd](https://registry.terraform.io/providers/vmware/vcd/3.3.1) (vmware/vcd/3.3.1)
- [vmc](https://registry.terraform.io/providers/vmware/vmc/1.7.0) (vmware/vmc/1.7.0)
- [vra](https://registry.terraform.io/providers/vmware/vra/0.3.9) (vmware/vra/0.3.9)
- [vra7](https://registry.terraform.io/providers/vmware/vra7/3.0.2) (vmware/vra7/3.0.2)
- [vultr](https://registry.terraform.io/providers/vultr/vultr/2.4.1) (vultr/vultr/2.4.1)
- [wavefront](https://registry.terraform.io/providers/vmware/wavefront/3.0.0) (vmware/wavefront/3.0.0)

### Community providers

Community providers must be imported with namespace.

```python
# With namespace
import provider.innovationnorway.git
```

*Terrascript* currently supports the following community *Terraform* providers.
- [activedirectory](https://registry.terraform.io/providers/PortOfPortland/activedirectory/0.5.1-pre) (PortOfPortland/activedirectory/0.5.1-pre)
- [airtable](https://registry.terraform.io/providers/paultyng/airtable/0.1.0) (paultyng/airtable/0.1.0)
- [ansiblevault](https://registry.terraform.io/providers/MeilleursAgents/ansiblevault/2.2.0) (MeilleursAgents/ansiblevault/2.2.0)
- [appdynamics](https://registry.terraform.io/providers/HarryEMartland/appdynamics/0.1.0) (HarryEMartland/appdynamics/0.1.0)
- [artifactory](https://registry.terraform.io/providers/cappyzawa/artifactory/2.2.15) (cappyzawa/artifactory/2.2.15)
- [asana](https://registry.terraform.io/providers/davidji99/asana/0.1.2) (davidji99/asana/0.1.2)
- [awslambda](https://registry.terraform.io/providers/dedunumax/awslambda/1.0.6) (dedunumax/awslambda/1.0.6)
- [awsx](https://registry.terraform.io/providers/phzietsman/awsx/1.0.0) (phzietsman/awsx/1.0.0)
- [awx](https://registry.terraform.io/providers/mrcrilly/awx/0.1.2) (mrcrilly/awx/0.1.2)
- [azure-preview](https://registry.terraform.io/providers/innovationnorway/azure-preview/0.1.0-alpha.3) (innovationnorway/azure-preview/0.1.0-alpha.3)
- [azuredevops](https://registry.terraform.io/providers/ellisdon-oss/azuredevops/0.0.2) (ellisdon-oss/azuredevops/0.0.2)
- [berglas](https://registry.terraform.io/providers/sethvargo/berglas/0.2.0) (sethvargo/berglas/0.2.0)
- [bitbucketserver](https://registry.terraform.io/providers/gavinbunney/bitbucketserver/1.5.0) (gavinbunney/bitbucketserver/1.5.0)
- [bless](https://registry.terraform.io/providers/chanzuckerberg/bless/0.5.0) (chanzuckerberg/bless/0.5.0)
- [cheesecake](https://registry.terraform.io/providers/joerx/cheesecake/0.2.3) (joerx/cheesecake/0.2.3)
- [christmas-tree](https://registry.terraform.io/providers/cappyzawa/christmas-tree/0.5.2) (cappyzawa/christmas-tree/0.5.2)
- [circleci](https://registry.terraform.io/providers/TomTucka/circleci/0.4.0) (TomTucka/circleci/0.4.0)
- [cloudknox](https://registry.terraform.io/providers/cloudknox/cloudknox/0.6.0) (cloudknox/cloudknox/0.6.0)
- [concourse](https://registry.terraform.io/providers/cappyzawa/concourse/0.1.2) (cappyzawa/concourse/0.1.2)
- [confluentcloud](https://registry.terraform.io/providers/Mongey/confluentcloud/0.0.12) (Mongey/confluentcloud/0.0.12)
- [cosmic](https://registry.terraform.io/providers/MissionCriticalCloud/cosmic/0.5.0) (MissionCriticalCloud/cosmic/0.5.0)
- [cronitor](https://registry.terraform.io/providers/nauxliu/cronitor/1.0.8) (nauxliu/cronitor/1.0.8)
- [ct](https://registry.terraform.io/providers/poseidon/ct/0.9.0) (poseidon/ct/0.9.0)
- [dbussecretservice](https://registry.terraform.io/providers/abergmeier/dbussecretservice/0.0.6) (abergmeier/dbussecretservice/0.0.6)
- [dmsnitch](https://registry.terraform.io/providers/plukevdh/dmsnitch/0.1.2) (plukevdh/dmsnitch/0.1.2)
- [dns](https://registry.terraform.io/providers/someara/dns/2.3.0-pre) (someara/dns/2.3.0-pre)
- [dnsimple](https://registry.terraform.io/providers/bgpat/dnsimple/0.5.1) (bgpat/dnsimple/0.5.1)
- [domeneshop](https://registry.terraform.io/providers/innovationnorway/domeneshop/0.1.0) (innovationnorway/domeneshop/0.1.0)
- [ecloud](https://registry.terraform.io/providers/ukfast/ecloud/2.0.0-alpha9) (ukfast/ecloud/2.0.0-alpha9)
- [eksctl](https://registry.terraform.io/providers/mumoshu/eksctl/0.16.2) (mumoshu/eksctl/0.16.2)
- [elasticsearch](https://registry.terraform.io/providers/phillbaker/elasticsearch/1.6.2) (phillbaker/elasticsearch/1.6.2)
- [errorcheck](https://registry.terraform.io/providers/jb-abbadie/errorcheck/2.0.4) (jb-abbadie/errorcheck/2.0.4)
- [esxi](https://registry.terraform.io/providers/josenk/esxi/1.8.2) (josenk/esxi/1.8.2)
- [exasol](https://registry.terraform.io/providers/abergmeier/exasol/0.0.23) (abergmeier/exasol/0.0.23)
- [filesystem](https://registry.terraform.io/providers/sethvargo/filesystem/0.2.0) (sethvargo/filesystem/0.2.0)
- [fortiadc](https://registry.terraform.io/providers/Ouest-France/fortiadc/0.3.2) (Ouest-France/fortiadc/0.3.2)
- [freeipa](https://registry.terraform.io/providers/camptocamp/freeipa/0.7.0) (camptocamp/freeipa/0.7.0)
- [geoserver](https://registry.terraform.io/providers/camptocamp/geoserver/0.0.3) (camptocamp/geoserver/0.0.3)
- [git](https://registry.terraform.io/providers/innovationnorway/git/0.1.3) (innovationnorway/git/0.1.3)
- [git](https://registry.terraform.io/providers/paultyng/git/0.1.0) (paultyng/git/0.1.0)
- [gpg](https://registry.terraform.io/providers/invidian/gpg/0.3.0) (invidian/gpg/0.3.0)
- [graylog](https://registry.terraform.io/providers/terraform-provider-graylog/graylog/1.0.4) (terraform-provider-graylog/graylog/1.0.4)
- [grid5000](https://registry.terraform.io/providers/pmorillon/grid5000/0.0.7) (pmorillon/grid5000/0.0.7)
- [gsuite](https://registry.terraform.io/providers/DeviaVir/gsuite/0.1.62) (DeviaVir/gsuite/0.1.62)
- [gsuite](https://registry.terraform.io/providers/paultyng/gsuite/0.2.2) (paultyng/gsuite/0.2.2)
- [guacamole](https://registry.terraform.io/providers/techBeck03/guacamole/1.2.4) (techBeck03/guacamole/1.2.4)
- [harbor](https://registry.terraform.io/providers/Ouest-France/harbor/0.2.0) (Ouest-France/harbor/0.2.0)
- [hashicups](https://registry.terraform.io/providers/hashicorp/hashicups/0.3.1) (hashicorp/hashicups/0.3.1)
- [hdns](https://registry.terraform.io/providers/alxrem/hdns/0.2.0) (alxrem/hdns/0.2.0)
- [hellosign](https://registry.terraform.io/providers/Mongey/hellosign/0.0.2) (Mongey/hellosign/0.0.2)
- [helmfile](https://registry.terraform.io/providers/mumoshu/helmfile/0.14.0) (mumoshu/helmfile/0.14.0)
- [herokux](https://registry.terraform.io/providers/davidji99/herokux/0.30.1) (davidji99/herokux/0.30.1)
- [hetznerdns](https://registry.terraform.io/providers/timohirt/hetznerdns/1.1.1) (timohirt/hetznerdns/1.1.1)
- [honeycombio](https://registry.terraform.io/providers/kvrhdn/honeycombio/0.1.4) (kvrhdn/honeycombio/0.1.4)
- [hsdp](https://registry.terraform.io/providers/philips-software/hsdp/0.18.8) (philips-software/hsdp/0.18.8)
- [idm](https://registry.terraform.io/providers/DTherHtun/idm/0.0.2) (DTherHtun/idm/0.0.2)
- [infoblox](https://registry.terraform.io/providers/techBeck03/infoblox/2.0.5) (techBeck03/infoblox/2.0.5)
- [iptables](https://registry.terraform.io/providers/jeremmfr/iptables/1.2.0) (jeremmfr/iptables/1.2.0)
- [itop](https://registry.terraform.io/providers/Ouest-France/itop/0.6.1) (Ouest-France/itop/0.6.1)
- [javascript](https://registry.terraform.io/providers/apparentlymart/javascript/0.0.1) (apparentlymart/javascript/0.0.1)
- [jenkins](https://registry.terraform.io/providers/taiidani/jenkins/0.8.0) (taiidani/jenkins/0.8.0)
- [jetstream](https://registry.terraform.io/providers/nats-io/jetstream/0.0.24) (nats-io/jetstream/0.0.24)
- [jsonnet](https://registry.terraform.io/providers/alxrem/jsonnet/1.0.3) (alxrem/jsonnet/1.0.3)
- [junos](https://registry.terraform.io/providers/jeremmfr/junos/1.19.0) (jeremmfr/junos/1.19.0)
- [jwt](https://registry.terraform.io/providers/camptocamp/jwt/0.0.3) (camptocamp/jwt/0.0.3)
- [k8s](https://registry.terraform.io/providers/banzaicloud/k8s/0.9.1) (banzaicloud/k8s/0.9.1)
- [kafka](https://registry.terraform.io/providers/Mongey/kafka/0.3.3) (Mongey/kafka/0.3.3)
- [kafka-connect](https://registry.terraform.io/providers/Mongey/kafka-connect/0.2.3) (Mongey/kafka-connect/0.2.3)
- [kibana](https://registry.terraform.io/providers/mayjak/kibana/0.7.1) (mayjak/kibana/0.7.1)
- [kind](https://registry.terraform.io/providers/unicell/kind/0.0.2-u2) (unicell/kind/0.0.2-u2)
- [kubectl](https://registry.terraform.io/providers/gavinbunney/kubectl/1.11.3) (gavinbunney/kubectl/1.11.3)
- [kubectl](https://registry.terraform.io/providers/mumoshu/kubectl/0.2.0) (mumoshu/kubectl/0.2.0)
- [kubeflowpipelines](https://registry.terraform.io/providers/datarootsio/kubeflowpipelines/0.0.10) (datarootsio/kubeflowpipelines/0.0.10)
- [lastpass](https://registry.terraform.io/providers/nrkno/lastpass/0.5.3) (nrkno/lastpass/0.5.3)
- [ldap](https://registry.terraform.io/providers/Ouest-France/ldap/0.7.1) (Ouest-France/ldap/0.7.1)
- [libvirt](https://registry.terraform.io/providers/invidian/libvirt/0.6.10-rc1) (invidian/libvirt/0.6.10-rc1)
- [loadbalancer](https://registry.terraform.io/providers/ukfast/loadbalancer/1.0.0-alpha1) (ukfast/loadbalancer/1.0.0-alpha1)
- [lvslb](https://registry.terraform.io/providers/jeremmfr/lvslb/1.1.0) (jeremmfr/lvslb/1.1.0)
- [lvsnetwork](https://registry.terraform.io/providers/jeremmfr/lvsnetwork/1.2.0) (jeremmfr/lvsnetwork/1.2.0)
- [matchbox](https://registry.terraform.io/providers/poseidon/matchbox/0.4.1) (poseidon/matchbox/0.4.1)
- [middesk](https://registry.terraform.io/providers/Mongey/middesk/0.0.2) (Mongey/middesk/0.0.2)
- [mikrotik](https://registry.terraform.io/providers/ddelnano/mikrotik/0.7.0) (ddelnano/mikrotik/0.7.0)
- [msgraph](https://registry.terraform.io/providers/yaegashi/msgraph/0.0.5) (yaegashi/msgraph/0.0.5)
- [mssql](https://registry.terraform.io/providers/drarko/mssql/0.0.4) (drarko/mssql/0.0.4)
- [netbox](https://registry.terraform.io/providers/e-breuninger/netbox/0.2.2) (e-breuninger/netbox/0.2.2)
- [netbox](https://registry.terraform.io/providers/innovationnorway/netbox/0.1.0-alpha.2) (innovationnorway/netbox/0.1.0-alpha.2)
- [njalla](https://registry.terraform.io/providers/Sighery/njalla/0.9.1) (Sighery/njalla/0.9.1)
- [nomadutility](https://registry.terraform.io/providers/AdrienneCohea/nomadutility/0.0.14) (AdrienneCohea/nomadutility/0.0.14)
- [null](https://registry.terraform.io/providers/mildred/null/1.1.0) (mildred/null/1.1.0)
- [null](https://registry.terraform.io/providers/paultyng/null/0.1.1) (paultyng/null/0.1.1)
- [null](https://registry.terraform.io/providers/ptyng/null/0.1.1) (ptyng/null/0.1.1)
- [okta](https://registry.terraform.io/providers/chanzuckerberg/okta/3.10.3) (chanzuckerberg/okta/3.10.3)
- [oktafork](https://registry.terraform.io/providers/gavinbunney/oktafork/3.12.9) (gavinbunney/oktafork/3.12.9)
- [openshift](https://registry.terraform.io/providers/llomgui/openshift/1.1.0) (llomgui/openshift/1.1.0)
- [opnsense](https://registry.terraform.io/providers/kradalby/opnsense/0.0.2-pre) (kradalby/opnsense/0.0.2-pre)
- [orion](https://registry.terraform.io/providers/stobias123/orion/0.3.2) (stobias123/orion/0.3.2)
- [outlook](https://registry.terraform.io/providers/magodo/outlook/0.0.4) (magodo/outlook/0.0.4)
- [ovh](https://registry.terraform.io/providers/invidian/ovh/0.9.3) (invidian/ovh/0.9.3)
- [petstore](https://registry.terraform.io/providers/DTherHtun/petstore/1.0.1) (DTherHtun/petstore/1.0.1)
- [phpipam](https://registry.terraform.io/providers/Ouest-France/phpipam/0.6.0) (Ouest-France/phpipam/0.6.0)
- [pingaccess](https://registry.terraform.io/providers/iwarapter/pingaccess/0.7.0) (iwarapter/pingaccess/0.7.0)
- [pingdom](https://registry.terraform.io/providers/nauxliu/pingdom/1.1.2) (nauxliu/pingdom/1.1.2)
- [pingfederate](https://registry.terraform.io/providers/iwarapter/pingfederate/0.0.19) (iwarapter/pingfederate/0.0.19)
- [po](https://registry.terraform.io/providers/greg-gajda/po/1.0.0) (greg-gajda/po/1.0.0)
- [postgresql](https://registry.terraform.io/providers/cyrilgdn/postgresql/1.14.0) (cyrilgdn/postgresql/1.14.0)
- [puppetca](https://registry.terraform.io/providers/camptocamp/puppetca/1.3.0) (camptocamp/puppetca/1.3.0)
- [puppetdb](https://registry.terraform.io/providers/camptocamp/puppetdb/1.2.0) (camptocamp/puppetdb/1.2.0)
- [pypi](https://registry.terraform.io/providers/jeffwecan/pypi/0.0.9) (jeffwecan/pypi/0.0.9)
- [qingcloud](https://registry.terraform.io/providers/shaowenchen/qingcloud/1.2.6) (shaowenchen/qingcloud/1.2.6)
- [rabbitmq](https://registry.terraform.io/providers/cyrilgdn/rabbitmq/1.5.1) (cyrilgdn/rabbitmq/1.5.1)
- [rancher](https://registry.terraform.io/providers/eLobeto/rancher/1.5.1) (eLobeto/rancher/1.5.1)
- [restapi](https://registry.terraform.io/providers/gavinbunney/restapi/1.15.4) (gavinbunney/restapi/1.15.4)
- [rollbar](https://registry.terraform.io/providers/davidji99/rollbar/1.5.1) (davidji99/rollbar/1.5.1)
- [sakuracloud](https://registry.terraform.io/providers/sacloud/sakuracloud/2.12.0) (sacloud/sakuracloud/2.12.0)
- [scaffolding](https://registry.terraform.io/providers/iwarapter/scaffolding/0.0.1) (iwarapter/scaffolding/0.0.1)
- [scaffolding](https://registry.terraform.io/providers/unicell/scaffolding/0.0.2) (unicell/scaffolding/0.0.2)
- [selectel](https://registry.terraform.io/providers/selectel/selectel/3.6.2) (selectel/selectel/3.6.2)
- [sendgrid](https://registry.terraform.io/providers/davidji99/sendgrid/0.1.1) (davidji99/sendgrid/0.1.1)
- [sendgrid](https://registry.terraform.io/providers/Trois-Six/sendgrid/0.1.6) (Trois-Six/sendgrid/0.1.6)
- [sentry](https://registry.terraform.io/providers/jianyuan/sentry/0.6.0) (jianyuan/sentry/0.6.0)
- [seq](https://registry.terraform.io/providers/innovationnorway/seq/0.1.0-alpha.5) (innovationnorway/seq/0.1.0-alpha.5)
- [shell](https://registry.terraform.io/providers/scottwinkler/shell/1.7.7) (scottwinkler/shell/1.7.7)
- [shellescape](https://registry.terraform.io/providers/bgpat/shellescape/0.0.2) (bgpat/shellescape/0.0.2)
- [snowflake](https://registry.terraform.io/providers/chanzuckerberg/snowflake/0.25.17) (chanzuckerberg/snowflake/0.25.17)
- [sops](https://registry.terraform.io/providers/carlpett/sops/0.6.3) (carlpett/sops/0.6.3)
- [spinnaker](https://registry.terraform.io/providers/mercari/spinnaker/0.3.0) (mercari/spinnaker/0.3.0)
- [split](https://registry.terraform.io/providers/davidji99/split/0.2.0) (davidji99/split/0.2.0)
- [sql](https://registry.terraform.io/providers/paultyng/sql/0.4.0) (paultyng/sql/0.4.0)
- [sshcommand](https://registry.terraform.io/providers/invidian/sshcommand/0.2.2) (invidian/sshcommand/0.2.2)
- [statuspage](https://registry.terraform.io/providers/yannh/statuspage/0.1.7) (yannh/statuspage/0.1.7)
- [stdlib](https://registry.terraform.io/providers/invidian/stdlib/0.1.1) (invidian/stdlib/0.1.1)
- [sys](https://registry.terraform.io/providers/mildred/sys/1.3.25) (mildred/sys/1.3.25)
- [systemd](https://registry.terraform.io/providers/mildred/systemd/0.0.1) (mildred/systemd/0.0.1)
- [teamcity](https://registry.terraform.io/providers/jeffwecan/teamcity/1.0.1-jeffwecan-fork) (jeffwecan/teamcity/1.0.1-jeffwecan-fork)
- [testing](https://registry.terraform.io/providers/apparentlymart/testing/0.0.2) (apparentlymart/testing/0.0.2)
- [tfvars](https://registry.terraform.io/providers/innovationnorway/tfvars/0.0.1) (innovationnorway/tfvars/0.0.1)
- [tls](https://registry.terraform.io/providers/invidian/tls/2.2.1) (invidian/tls/2.2.1)
- [tls](https://registry.terraform.io/providers/someara/tls/2.3.0-pre) (someara/tls/2.3.0-pre)
- [transip](https://registry.terraform.io/providers/aequitas/transip/0.1.9) (aequitas/transip/0.1.9)
- [travis](https://registry.terraform.io/providers/bgpat/travis/0.1.6) (bgpat/travis/0.1.6)
- [triton](https://registry.terraform.io/providers/joyent/triton/0.8.1) (joyent/triton/0.8.1)
- [twitter](https://registry.terraform.io/providers/paultyng/twitter/0.1.0) (paultyng/twitter/0.1.0)
- [ucloud](https://registry.terraform.io/providers/ucloud/ucloud/1.29.0) (ucloud/ucloud/1.29.0)
- [ucodecov](https://registry.terraform.io/providers/at-wat/ucodecov/0.1.2) (at-wat/ucodecov/0.1.2)
- [ultradns](https://registry.terraform.io/providers/davidji99/ultradns/2.1.0) (davidji99/ultradns/2.1.0)
- [unifi](https://registry.terraform.io/providers/paultyng/unifi/0.28.1) (paultyng/unifi/0.28.1)
- [utravis](https://registry.terraform.io/providers/kamatama41/utravis/0.5.0) (kamatama41/utravis/0.5.0)
- [vault](https://registry.terraform.io/providers/cyrilgdn/vault/2.22.5) (cyrilgdn/vault/2.22.5)
- [vault](https://registry.terraform.io/providers/jeffwecan/vault/2.11.0-withsleep) (jeffwecan/vault/2.11.0-withsleep)
- [vaultutility](https://registry.terraform.io/providers/AdrienneCohea/vaultutility/0.0.3) (AdrienneCohea/vaultutility/0.0.3)
- [vinyldns](https://registry.terraform.io/providers/vinyldns/vinyldns/0.9.5) (vinyldns/vinyldns/0.9.5)
- [virtualbox](https://registry.terraform.io/providers/terra-farm/virtualbox/0.2.1-alpha.1) (terra-farm/virtualbox/0.2.1-alpha.1)
- [vsphere](https://registry.terraform.io/providers/techBeck03/vsphere/1.24.3-patch) (techBeck03/vsphere/1.24.3-patch)
- [windns](https://registry.terraform.io/providers/PortOfPortland/windns/0.5.3) (PortOfPortland/windns/0.5.3)
- [xenorchestra](https://registry.terraform.io/providers/terra-farm/xenorchestra/0.21.0) (terra-farm/xenorchestra/0.21.0)
- [zerotier](https://registry.terraform.io/providers/bltavares/zerotier/0.3.0) (bltavares/zerotier/0.3.0)

### Unsupported providers

The following providers are not supported.
- [aiven](https://registry.terraform.io/providers/juniorz/aiven/0.1.0) (juniorz/aiven/0.1.0) - Failed to initialise provider
- [appd](https://registry.terraform.io/providers/maskerade/appd/0.0.5) (maskerade/appd/0.0.5) - Failed to initialise provider
- [flexkube](https://registry.terraform.io/providers/invidian/flexkube/0.3.3) (invidian/flexkube/0.3.3) - Failed to initialise provider
- [googlecalendar](https://registry.terraform.io/providers/sethvargo/googlecalendar/0.3.1) (sethvargo/googlecalendar/0.3.1) - Failed to initialise provider
- [grafana](https://registry.terraform.io/providers/58231/grafana/0.0.2) (58231/grafana/0.0.2) - 58231 is not a valid Python identifier
- [ipam](https://registry.terraform.io/providers/beauknowssoftware/ipam/0.2.6) (beauknowssoftware/ipam/0.2.6) - Failed to initialise provider
- [k8s](https://registry.terraform.io/providers/mingfang/k8s/1.0.2) (mingfang/k8s/1.0.2) - Failed to process provider
- [kind1](https://registry.terraform.io/providers/unicell/kind1/0.0.2-u2) (unicell/kind1/0.0.2-u2) - Failed to initialise provider
- [lxd](https://registry.terraform.io/providers/arren-ru/lxd/1.4.0) (arren-ru/lxd/1.4.0) - Failed to initialise provider
- [okta](https://registry.terraform.io/providers/gavinbunney/okta/3.12.7) (gavinbunney/okta/3.12.7) - Failed to initialise provider
- [okta](https://registry.terraform.io/providers/oktadeveloper/okta/3.13.7) (oktadeveloper/okta/3.13.7) - Failed to initialise provider
- [pass](https://registry.terraform.io/providers/camptocamp/pass/2.0.0) (camptocamp/pass/2.0.0) - pass is a Python keyword
- [safedns](https://registry.terraform.io/providers/ukfast/safedns/1.1.2) (ukfast/safedns/1.1.2) - Failed to process provider
- [shakenfist](https://registry.terraform.io/providers/shakenfist/shakenfist/0.2.5) (shakenfist/shakenfist/0.2.5) - Failed to initialise provider
- [tozny](https://registry.terraform.io/providers/tozny/tozny/0.12.0) (tozny/tozny/0.12.0) - Failed to initialise provider
- [unofficial-travis](https://registry.terraform.io/providers/kamatama41/unofficial-travis/0.5.0) (kamatama41/unofficial-travis/0.5.0) - Failed to initialise provider
- [vmworkstation](https://registry.terraform.io/providers/elsudano/vmworkstation/0.2.3) (elsudano/vmworkstation/0.2.3) - Failed to process provider
- [zerotier](https://registry.terraform.io/providers/someara/zerotier/0.1.47) (someara/zerotier/0.1.47) - Failed to initialise provider
