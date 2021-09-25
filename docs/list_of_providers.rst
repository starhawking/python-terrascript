
List of providers
-----------------

This document lists the *Terraform* providers that are currently supported by *Terrascript*.


* `Official providers <#official-providers>`_
* `Partner providers <#partner-providers>`_
* `Community providers <#community-providers>`_
* `Unsupported providers <#unsupported-providers>`_

Official providers
^^^^^^^^^^^^^^^^^^

Official providers can be imported with or without namespace.

.. code-block:: python

   # With namespace
   import provider.hashicorp.aws
   import resource.hashicorp.aws
   import data.hashicorp.aws

   # Without namespace
   import provider.aws
   import resource.aws
   import data.aws

*Terrascript* currently supports the following official *Terraform* providers.


* `ad <https://registry.terraform.io/providers/hashicorp/ad/0.4.3>`_ (hashicorp/ad/0.4.3)
* `alicloud <https://registry.terraform.io/providers/hashicorp/alicloud/1.136.0>`_ (hashicorp/alicloud/1.136.0)
* `archive <https://registry.terraform.io/providers/hashicorp/archive/2.2.0>`_ (hashicorp/archive/2.2.0)
* `aws <https://registry.terraform.io/providers/hashicorp/aws/3.60.0>`_ (hashicorp/aws/3.60.0)
* `azuread <https://registry.terraform.io/providers/hashicorp/azuread/2.4.0>`_ (hashicorp/azuread/2.4.0)
* `azurerm <https://registry.terraform.io/providers/hashicorp/azurerm/2.78.0>`_ (hashicorp/azurerm/2.78.0)
* `azurestack <https://registry.terraform.io/providers/hashicorp/azurestack/0.10.0>`_ (hashicorp/azurestack/0.10.0)
* `boundary <https://registry.terraform.io/providers/hashicorp/boundary/1.0.5>`_ (hashicorp/boundary/1.0.5)
* `ciscoasa <https://registry.terraform.io/providers/hashicorp/ciscoasa/1.2.0>`_ (hashicorp/ciscoasa/1.2.0)
* `cloudinit <https://registry.terraform.io/providers/hashicorp/cloudinit/2.2.0>`_ (hashicorp/cloudinit/2.2.0)
* `consul <https://registry.terraform.io/providers/hashicorp/consul/2.13.0>`_ (hashicorp/consul/2.13.0)
* `dns <https://registry.terraform.io/providers/hashicorp/dns/3.2.1>`_ (hashicorp/dns/3.2.1)
* `external <https://registry.terraform.io/providers/hashicorp/external/2.1.0>`_ (hashicorp/external/2.1.0)
* `fakewebservices <https://registry.terraform.io/providers/hashicorp/fakewebservices/0.2.1>`_ (hashicorp/fakewebservices/0.2.1)
* `github <https://registry.terraform.io/providers/hashicorp/github/4.15.1>`_ (hashicorp/github/4.15.1)
* `google <https://registry.terraform.io/providers/hashicorp/google/3.85.0>`_ (hashicorp/google/3.85.0)
* `google-beta <https://registry.terraform.io/providers/hashicorp/google-beta/3.85.0>`_ (hashicorp/google-beta/3.85.0)
* `googleworkspace <https://registry.terraform.io/providers/hashicorp/googleworkspace/0.4.1>`_ (hashicorp/googleworkspace/0.4.1)
* `hcp <https://registry.terraform.io/providers/hashicorp/hcp/0.17.0>`_ (hashicorp/hcp/0.17.0)
* `hcs <https://registry.terraform.io/providers/hashicorp/hcs/0.5.0>`_ (hashicorp/hcs/0.5.0)
* `helm <https://registry.terraform.io/providers/hashicorp/helm/2.3.0>`_ (hashicorp/helm/2.3.0)
* `http <https://registry.terraform.io/providers/hashicorp/http/2.1.0>`_ (hashicorp/http/2.1.0)
* `kubernetes <https://registry.terraform.io/providers/hashicorp/kubernetes/2.5.0>`_ (hashicorp/kubernetes/2.5.0)
* `kubernetes-alpha <https://registry.terraform.io/providers/hashicorp/kubernetes-alpha/0.6.0>`_ (hashicorp/kubernetes-alpha/0.6.0)
* `local <https://registry.terraform.io/providers/hashicorp/local/2.1.0>`_ (hashicorp/local/2.1.0)
* `nomad <https://registry.terraform.io/providers/hashicorp/nomad/1.4.15>`_ (hashicorp/nomad/1.4.15)
* `null <https://registry.terraform.io/providers/hashicorp/null/3.1.0>`_ (hashicorp/null/3.1.0)
* `oci <https://registry.terraform.io/providers/hashicorp/oci/4.45.0>`_ (hashicorp/oci/4.45.0)
* `opc <https://registry.terraform.io/providers/hashicorp/opc/1.4.1>`_ (hashicorp/opc/1.4.1)
* `oraclepaas <https://registry.terraform.io/providers/hashicorp/oraclepaas/1.5.3>`_ (hashicorp/oraclepaas/1.5.3)
* `random <https://registry.terraform.io/providers/hashicorp/random/3.1.0>`_ (hashicorp/random/3.1.0)
* `template <https://registry.terraform.io/providers/hashicorp/template/2.2.0>`_ (hashicorp/template/2.2.0)
* `terraform <https://registry.terraform.io/providers/hashicorp/terraform/1.0.2>`_ (hashicorp/terraform/1.0.2)
* `tfe <https://registry.terraform.io/providers/hashicorp/tfe/0.26.1>`_ (hashicorp/tfe/0.26.1)
* `time <https://registry.terraform.io/providers/hashicorp/time/0.7.2>`_ (hashicorp/time/0.7.2)
* `tls <https://registry.terraform.io/providers/hashicorp/tls/3.1.0>`_ (hashicorp/tls/3.1.0)
* `vault <https://registry.terraform.io/providers/hashicorp/vault/2.24.0>`_ (hashicorp/vault/2.24.0)
* `vsphere <https://registry.terraform.io/providers/hashicorp/vsphere/2.0.2>`_ (hashicorp/vsphere/2.0.2)

Partner providers
^^^^^^^^^^^^^^^^^

Partner providers can be imported with or without namespace.

.. code-block:: python

   # With namespace
   import provider.akamai.akamai
   import resource.akamai.akamai
   import data.akamai.akamai

   # Without namespace
   import provider.akamai
   import resource.akamai
   import data.akamai

*Terrascript* currently supports the following partner *Terraform* providers.


* `akamai <https://registry.terraform.io/providers/akamai/akamai/1.7.0>`_ (akamai/akamai/1.7.0)
* `alicloud <https://registry.terraform.io/providers/aliyun/alicloud/1.136.0>`_ (aliyun/alicloud/1.136.0)
* `amixr <https://registry.terraform.io/providers/alertmixer/amixr/0.2.3>`_ (alertmixer/amixr/0.2.3)
* `avi <https://registry.terraform.io/providers/vmware/avi/21.1.1>`_ (vmware/avi/21.1.1)
* `aviatrix <https://registry.terraform.io/providers/AviatrixSystems/aviatrix/2.20.0>`_ (AviatrixSystems/aviatrix/2.20.0)
* `azurecaf <https://registry.terraform.io/providers/aztfmod/azurecaf/1.2.6>`_ (aztfmod/azurecaf/1.2.6)
* `bigip <https://registry.terraform.io/providers/F5Networks/bigip/1.11.1>`_ (F5Networks/bigip/1.11.1)
* `brightbox <https://registry.terraform.io/providers/brightbox/brightbox/2.0.6>`_ (brightbox/brightbox/2.0.6)
* `circonus <https://registry.terraform.io/providers/circonus-labs/circonus/0.12.2>`_ (circonus-labs/circonus/0.12.2)
* `cloudflare <https://registry.terraform.io/providers/cloudflare/cloudflare/3.1.0>`_ (cloudflare/cloudflare/3.1.0)
* `cloudsmith <https://registry.terraform.io/providers/cloudsmith-io/cloudsmith/0.0.6>`_ (cloudsmith-io/cloudsmith/0.0.6)
* `databricks <https://registry.terraform.io/providers/databrickslabs/databricks/0.3.7>`_ (databrickslabs/databricks/0.3.7)
* `datadog <https://registry.terraform.io/providers/DataDog/datadog/3.4.0>`_ (DataDog/datadog/3.4.0)
* `digitalocean <https://registry.terraform.io/providers/digitalocean/digitalocean/2.12.0>`_ (digitalocean/digitalocean/2.12.0)
* `exoscale <https://registry.terraform.io/providers/exoscale/exoscale/0.29.0>`_ (exoscale/exoscale/0.29.0)
* `fastly <https://registry.terraform.io/providers/fastly/fastly/0.35.0>`_ (fastly/fastly/0.35.0)
* `fortimanager <https://registry.terraform.io/providers/fortinetdev/fortimanager/1.3.4>`_ (fortinetdev/fortimanager/1.3.4)
* `fortios <https://registry.terraform.io/providers/fortinetdev/fortios/1.13.1>`_ (fortinetdev/fortios/1.13.1)
* `gridscale <https://registry.terraform.io/providers/gridscale/gridscale/1.13.0>`_ (gridscale/gridscale/1.13.0)
* `hcloud <https://registry.terraform.io/providers/hetznercloud/hcloud/1.31.1>`_ (hetznercloud/hcloud/1.31.1)
* `heroku <https://registry.terraform.io/providers/heroku/heroku/4.6.0>`_ (heroku/heroku/4.6.0)
* `launchdarkly <https://registry.terraform.io/providers/launchdarkly/launchdarkly/2.0.1>`_ (launchdarkly/launchdarkly/2.0.1)
* `linode <https://registry.terraform.io/providers/linode/linode/1.21.0>`_ (linode/linode/1.21.0)
* `mongodbatlas <https://registry.terraform.io/providers/mongodb/mongodbatlas/1.0.1>`_ (mongodb/mongodbatlas/1.0.1)
* `ncloud <https://registry.terraform.io/providers/NaverCloudPlatform/ncloud/2.1.2>`_ (NaverCloudPlatform/ncloud/2.1.2)
* `netapp-cloudmanager <https://registry.terraform.io/providers/NetApp/netapp-cloudmanager/21.9.2>`_ (NetApp/netapp-cloudmanager/21.9.2)
* `netapp-elementsw <https://registry.terraform.io/providers/NetApp/netapp-elementsw/20.11.0>`_ (NetApp/netapp-elementsw/20.11.0)
* `netapp-gcp <https://registry.terraform.io/providers/NetApp/netapp-gcp/21.9.0>`_ (NetApp/netapp-gcp/21.9.0)
* `newrelic <https://registry.terraform.io/providers/newrelic/newrelic/2.25.0>`_ (newrelic/newrelic/2.25.0)
* `ns1 <https://registry.terraform.io/providers/ns1-terraform/ns1/1.12.1>`_ (ns1-terraform/ns1/1.12.1)
* `nsxt <https://registry.terraform.io/providers/vmware/nsxt/3.2.4>`_ (vmware/nsxt/3.2.4)
* `oktaasa <https://registry.terraform.io/providers/oktadeveloper/oktaasa/1.0.1>`_ (oktadeveloper/oktaasa/1.0.1)
* `onelogin <https://registry.terraform.io/providers/onelogin/onelogin/0.1.23>`_ (onelogin/onelogin/0.1.23)
* `pagerduty <https://registry.terraform.io/providers/PagerDuty/pagerduty/1.11.0>`_ (PagerDuty/pagerduty/1.11.0)
* `pnap <https://registry.terraform.io/providers/phoenixnap/pnap/0.8.0>`_ (phoenixnap/pnap/0.8.0)
* `rancher2 <https://registry.terraform.io/providers/rancher/rancher2/1.20.0>`_ (rancher/rancher2/1.20.0)
* `rke <https://registry.terraform.io/providers/rancher/rke/1.2.3>`_ (rancher/rke/1.2.3)
* `scaleway <https://registry.terraform.io/providers/scaleway/scaleway/2.1.0>`_ (scaleway/scaleway/2.1.0)
* `sdm <https://registry.terraform.io/providers/strongdm/sdm/1.0.28>`_ (strongdm/sdm/1.0.28)
* `sematext <https://registry.terraform.io/providers/sematext/sematext/0.4.0>`_ (sematext/sematext/0.4.0)
* `signalfx <https://registry.terraform.io/providers/splunk-terraform/signalfx/6.7.7>`_ (splunk-terraform/signalfx/6.7.7)
* `stackpath <https://registry.terraform.io/providers/stackpath/stackpath/1.3.3>`_ (stackpath/stackpath/1.3.3)
* `sumologic <https://registry.terraform.io/providers/SumoLogic/sumologic/2.10.0>`_ (SumoLogic/sumologic/2.10.0)
* `tencentcloud <https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/1.59.4>`_ (tencentcloudstack/tencentcloud/1.59.4)
* `transloadit <https://registry.terraform.io/providers/transloadit/transloadit/0.4.0>`_ (transloadit/transloadit/0.4.0)
* `triton <https://registry.terraform.io/providers/joyent/triton/0.8.2>`_ (joyent/triton/0.8.2)
* `turbot <https://registry.terraform.io/providers/turbot/turbot/1.8.2>`_ (turbot/turbot/1.8.2)
* `vcd <https://registry.terraform.io/providers/vmware/vcd/3.3.1>`_ (vmware/vcd/3.3.1)
* `vmc <https://registry.terraform.io/providers/vmware/vmc/1.7.0>`_ (vmware/vmc/1.7.0)
* `vra <https://registry.terraform.io/providers/vmware/vra/0.3.11>`_ (vmware/vra/0.3.11)
* `vra7 <https://registry.terraform.io/providers/vmware/vra7/3.0.2>`_ (vmware/vra7/3.0.2)
* `vultr <https://registry.terraform.io/providers/vultr/vultr/2.4.2>`_ (vultr/vultr/2.4.2)
* `wavefront <https://registry.terraform.io/providers/vmware/wavefront/3.0.0>`_ (vmware/wavefront/3.0.0)

Community providers
^^^^^^^^^^^^^^^^^^^

Community providers must be imported with namespace.

.. code-block:: python

   # With namespace
   import provider.innovationnorway.git

*Terrascript* currently supports the following community *Terraform* providers.


* `activedirectory <https://registry.terraform.io/providers/PortOfPortland/activedirectory/0.5.1-pre>`_ (PortOfPortland/activedirectory/0.5.1-pre)
* `ad <https://registry.terraform.io/providers/techBeck03/ad/0.4.3-patch>`_ (techBeck03/ad/0.4.3-patch)
* `airtable <https://registry.terraform.io/providers/paultyng/airtable/0.1.0>`_ (paultyng/airtable/0.1.0)
* `ansiblevault <https://registry.terraform.io/providers/MeilleursAgents/ansiblevault/2.2.0>`_ (MeilleursAgents/ansiblevault/2.2.0)
* `appdynamics <https://registry.terraform.io/providers/HarryEMartland/appdynamics/0.1.0>`_ (HarryEMartland/appdynamics/0.1.0)
* `artifactory <https://registry.terraform.io/providers/cappyzawa/artifactory/2.2.15>`_ (cappyzawa/artifactory/2.2.15)
* `asana <https://registry.terraform.io/providers/davidji99/asana/0.1.2>`_ (davidji99/asana/0.1.2)
* `awslambda <https://registry.terraform.io/providers/dedunumax/awslambda/1.0.6>`_ (dedunumax/awslambda/1.0.6)
* `awsx <https://registry.terraform.io/providers/phzietsman/awsx/1.0.0>`_ (phzietsman/awsx/1.0.0)
* `awx <https://registry.terraform.io/providers/mrcrilly/awx/0.1.2>`_ (mrcrilly/awx/0.1.2)
* `azure-preview <https://registry.terraform.io/providers/innovationnorway/azure-preview/0.1.0-alpha.3>`_ (innovationnorway/azure-preview/0.1.0-alpha.3)
* `azuredevops <https://registry.terraform.io/providers/ellisdon-oss/azuredevops/0.0.2>`_ (ellisdon-oss/azuredevops/0.0.2)
* `berglas <https://registry.terraform.io/providers/sethvargo/berglas/0.2.0>`_ (sethvargo/berglas/0.2.0)
* `bitbucketserver <https://registry.terraform.io/providers/gavinbunney/bitbucketserver/1.5.0>`_ (gavinbunney/bitbucketserver/1.5.0)
* `bless <https://registry.terraform.io/providers/chanzuckerberg/bless/0.5.0>`_ (chanzuckerberg/bless/0.5.0)
* `cheesecake <https://registry.terraform.io/providers/joerx/cheesecake/0.2.3>`_ (joerx/cheesecake/0.2.3)
* `christmas-tree <https://registry.terraform.io/providers/cappyzawa/christmas-tree/0.5.2>`_ (cappyzawa/christmas-tree/0.5.2)
* `circleci <https://registry.terraform.io/providers/TomTucka/circleci/0.4.0>`_ (TomTucka/circleci/0.4.0)
* `cloudknox <https://registry.terraform.io/providers/cloudknox/cloudknox/0.6.0>`_ (cloudknox/cloudknox/0.6.0)
* `concourse <https://registry.terraform.io/providers/cappyzawa/concourse/0.1.2>`_ (cappyzawa/concourse/0.1.2)
* `confluentcloud <https://registry.terraform.io/providers/Mongey/confluentcloud/0.0.12>`_ (Mongey/confluentcloud/0.0.12)
* `cosmic <https://registry.terraform.io/providers/MissionCriticalCloud/cosmic/0.5.0>`_ (MissionCriticalCloud/cosmic/0.5.0)
* `cronitor <https://registry.terraform.io/providers/nauxliu/cronitor/1.0.8>`_ (nauxliu/cronitor/1.0.8)
* `ct <https://registry.terraform.io/providers/poseidon/ct/0.9.0>`_ (poseidon/ct/0.9.0)
* `dbussecretservice <https://registry.terraform.io/providers/abergmeier/dbussecretservice/0.0.6>`_ (abergmeier/dbussecretservice/0.0.6)
* `dmsnitch <https://registry.terraform.io/providers/plukevdh/dmsnitch/0.1.2>`_ (plukevdh/dmsnitch/0.1.2)
* `dns <https://registry.terraform.io/providers/someara/dns/2.3.0-pre>`_ (someara/dns/2.3.0-pre)
* `dnsimple <https://registry.terraform.io/providers/bgpat/dnsimple/0.5.1>`_ (bgpat/dnsimple/0.5.1)
* `domeneshop <https://registry.terraform.io/providers/innovationnorway/domeneshop/0.1.0>`_ (innovationnorway/domeneshop/0.1.0)
* `ecloud <https://registry.terraform.io/providers/ukfast/ecloud/2.0.0>`_ (ukfast/ecloud/2.0.0)
* `eksctl <https://registry.terraform.io/providers/mumoshu/eksctl/0.16.2>`_ (mumoshu/eksctl/0.16.2)
* `elasticsearch <https://registry.terraform.io/providers/phillbaker/elasticsearch/2.0.0-beta.1>`_ (phillbaker/elasticsearch/2.0.0-beta.1)
* `errorcheck <https://registry.terraform.io/providers/jb-abbadie/errorcheck/2.0.4>`_ (jb-abbadie/errorcheck/2.0.4)
* `esxi <https://registry.terraform.io/providers/josenk/esxi/1.8.3>`_ (josenk/esxi/1.8.3)
* `exasol <https://registry.terraform.io/providers/abergmeier/exasol/0.0.23>`_ (abergmeier/exasol/0.0.23)
* `filesystem <https://registry.terraform.io/providers/sethvargo/filesystem/0.2.0>`_ (sethvargo/filesystem/0.2.0)
* `fortiadc <https://registry.terraform.io/providers/Ouest-France/fortiadc/0.3.2>`_ (Ouest-France/fortiadc/0.3.2)
* `freeipa <https://registry.terraform.io/providers/camptocamp/freeipa/0.7.0>`_ (camptocamp/freeipa/0.7.0)
* `geoserver <https://registry.terraform.io/providers/camptocamp/geoserver/0.0.3>`_ (camptocamp/geoserver/0.0.3)
* `git <https://registry.terraform.io/providers/innovationnorway/git/0.1.3>`_ (innovationnorway/git/0.1.3)
* `git <https://registry.terraform.io/providers/paultyng/git/0.1.0>`_ (paultyng/git/0.1.0)
* `gpg <https://registry.terraform.io/providers/invidian/gpg/0.3.0>`_ (invidian/gpg/0.3.0)
* `graylog <https://registry.terraform.io/providers/terraform-provider-graylog/graylog/1.0.4>`_ (terraform-provider-graylog/graylog/1.0.4)
* `grid5000 <https://registry.terraform.io/providers/pmorillon/grid5000/0.0.7>`_ (pmorillon/grid5000/0.0.7)
* `gsuite <https://registry.terraform.io/providers/DeviaVir/gsuite/0.1.62>`_ (DeviaVir/gsuite/0.1.62)
* `gsuite <https://registry.terraform.io/providers/paultyng/gsuite/0.2.2>`_ (paultyng/gsuite/0.2.2)
* `guacamole <https://registry.terraform.io/providers/techBeck03/guacamole/1.2.7>`_ (techBeck03/guacamole/1.2.7)
* `harbor <https://registry.terraform.io/providers/Ouest-France/harbor/0.2.0>`_ (Ouest-France/harbor/0.2.0)
* `hashicups <https://registry.terraform.io/providers/hashicorp/hashicups/0.3.1>`_ (hashicorp/hashicups/0.3.1)
* `hdns <https://registry.terraform.io/providers/alxrem/hdns/0.2.0>`_ (alxrem/hdns/0.2.0)
* `hellosign <https://registry.terraform.io/providers/Mongey/hellosign/0.0.2>`_ (Mongey/hellosign/0.0.2)
* `helmfile <https://registry.terraform.io/providers/mumoshu/helmfile/0.14.1>`_ (mumoshu/helmfile/0.14.1)
* `herokux <https://registry.terraform.io/providers/davidji99/herokux/0.30.3>`_ (davidji99/herokux/0.30.3)
* `hetznerdns <https://registry.terraform.io/providers/timohirt/hetznerdns/1.1.1>`_ (timohirt/hetznerdns/1.1.1)
* `honeycombio <https://registry.terraform.io/providers/kvrhdn/honeycombio/0.1.4>`_ (kvrhdn/honeycombio/0.1.4)
* `hsdp <https://registry.terraform.io/providers/philips-software/hsdp/0.20.5>`_ (philips-software/hsdp/0.20.5)
* `idm <https://registry.terraform.io/providers/DTherHtun/idm/0.0.2>`_ (DTherHtun/idm/0.0.2)
* `infoblox <https://registry.terraform.io/providers/techBeck03/infoblox/2.0.7>`_ (techBeck03/infoblox/2.0.7)
* `iptables <https://registry.terraform.io/providers/jeremmfr/iptables/1.2.0>`_ (jeremmfr/iptables/1.2.0)
* `itop <https://registry.terraform.io/providers/Ouest-France/itop/0.6.1>`_ (Ouest-France/itop/0.6.1)
* `javascript <https://registry.terraform.io/providers/apparentlymart/javascript/0.0.1>`_ (apparentlymart/javascript/0.0.1)
* `jenkins <https://registry.terraform.io/providers/taiidani/jenkins/0.9.0>`_ (taiidani/jenkins/0.9.0)
* `jetstream <https://registry.terraform.io/providers/nats-io/jetstream/0.0.26>`_ (nats-io/jetstream/0.0.26)
* `jsonnet <https://registry.terraform.io/providers/alxrem/jsonnet/1.0.3>`_ (alxrem/jsonnet/1.0.3)
* `junos <https://registry.terraform.io/providers/jeremmfr/junos/1.20.0>`_ (jeremmfr/junos/1.20.0)
* `jwt <https://registry.terraform.io/providers/camptocamp/jwt/0.0.3>`_ (camptocamp/jwt/0.0.3)
* `k8s <https://registry.terraform.io/providers/banzaicloud/k8s/0.9.1>`_ (banzaicloud/k8s/0.9.1)
* `kafka <https://registry.terraform.io/providers/Mongey/kafka/0.4.1>`_ (Mongey/kafka/0.4.1)
* `kafka-connect <https://registry.terraform.io/providers/Mongey/kafka-connect/0.2.3>`_ (Mongey/kafka-connect/0.2.3)
* `kibana <https://registry.terraform.io/providers/mayjak/kibana/0.7.1>`_ (mayjak/kibana/0.7.1)
* `kind <https://registry.terraform.io/providers/unicell/kind/0.0.2-u2>`_ (unicell/kind/0.0.2-u2)
* `kubectl <https://registry.terraform.io/providers/gavinbunney/kubectl/1.11.3>`_ (gavinbunney/kubectl/1.11.3)
* `kubectl <https://registry.terraform.io/providers/mumoshu/kubectl/0.2.0>`_ (mumoshu/kubectl/0.2.0)
* `kubeflowpipelines <https://registry.terraform.io/providers/datarootsio/kubeflowpipelines/0.0.10>`_ (datarootsio/kubeflowpipelines/0.0.10)
* `lastpass <https://registry.terraform.io/providers/nrkno/lastpass/0.5.3>`_ (nrkno/lastpass/0.5.3)
* `ldap <https://registry.terraform.io/providers/Ouest-France/ldap/0.7.2>`_ (Ouest-France/ldap/0.7.2)
* `libvirt <https://registry.terraform.io/providers/invidian/libvirt/0.6.10-rc1>`_ (invidian/libvirt/0.6.10-rc1)
* `loadbalancer <https://registry.terraform.io/providers/ukfast/loadbalancer/1.0.0-alpha1>`_ (ukfast/loadbalancer/1.0.0-alpha1)
* `lvslb <https://registry.terraform.io/providers/jeremmfr/lvslb/1.1.0>`_ (jeremmfr/lvslb/1.1.0)
* `lvsnetwork <https://registry.terraform.io/providers/jeremmfr/lvsnetwork/1.2.0>`_ (jeremmfr/lvsnetwork/1.2.0)
* `matchbox <https://registry.terraform.io/providers/poseidon/matchbox/0.4.1>`_ (poseidon/matchbox/0.4.1)
* `middesk <https://registry.terraform.io/providers/Mongey/middesk/0.0.2>`_ (Mongey/middesk/0.0.2)
* `mikrotik <https://registry.terraform.io/providers/ddelnano/mikrotik/0.8.0>`_ (ddelnano/mikrotik/0.8.0)
* `msgraph <https://registry.terraform.io/providers/yaegashi/msgraph/0.0.5>`_ (yaegashi/msgraph/0.0.5)
* `mssql <https://registry.terraform.io/providers/drarko/mssql/0.0.4>`_ (drarko/mssql/0.0.4)
* `netbox <https://registry.terraform.io/providers/e-breuninger/netbox/0.2.4>`_ (e-breuninger/netbox/0.2.4)
* `netbox <https://registry.terraform.io/providers/innovationnorway/netbox/0.1.0-alpha.2>`_ (innovationnorway/netbox/0.1.0-alpha.2)
* `njalla <https://registry.terraform.io/providers/Sighery/njalla/0.9.1>`_ (Sighery/njalla/0.9.1)
* `nomadutility <https://registry.terraform.io/providers/AdrienneCohea/nomadutility/0.0.14>`_ (AdrienneCohea/nomadutility/0.0.14)
* `null <https://registry.terraform.io/providers/mildred/null/1.1.0>`_ (mildred/null/1.1.0)
* `okta <https://registry.terraform.io/providers/chanzuckerberg/okta/3.10.3>`_ (chanzuckerberg/okta/3.10.3)
* `oktafork <https://registry.terraform.io/providers/gavinbunney/oktafork/3.12.9>`_ (gavinbunney/oktafork/3.12.9)
* `openshift <https://registry.terraform.io/providers/llomgui/openshift/1.1.0>`_ (llomgui/openshift/1.1.0)
* `opnsense <https://registry.terraform.io/providers/kradalby/opnsense/0.0.2-pre>`_ (kradalby/opnsense/0.0.2-pre)
* `opsgenie <https://registry.terraform.io/providers/opsgenie/opsgenie/0.6.5>`_ (opsgenie/opsgenie/0.6.5)
* `orion <https://registry.terraform.io/providers/stobias123/orion/0.3.2>`_ (stobias123/orion/0.3.2)
* `outlook <https://registry.terraform.io/providers/magodo/outlook/0.0.4>`_ (magodo/outlook/0.0.4)
* `ovh <https://registry.terraform.io/providers/invidian/ovh/0.9.3>`_ (invidian/ovh/0.9.3)
* `petstore <https://registry.terraform.io/providers/DTherHtun/petstore/1.0.1>`_ (DTherHtun/petstore/1.0.1)
* `phpipam <https://registry.terraform.io/providers/Ouest-France/phpipam/0.6.0>`_ (Ouest-France/phpipam/0.6.0)
* `pingaccess <https://registry.terraform.io/providers/iwarapter/pingaccess/0.8.0>`_ (iwarapter/pingaccess/0.8.0)
* `pingdom <https://registry.terraform.io/providers/nauxliu/pingdom/1.1.2>`_ (nauxliu/pingdom/1.1.2)
* `pingfederate <https://registry.terraform.io/providers/iwarapter/pingfederate/0.0.21>`_ (iwarapter/pingfederate/0.0.21)
* `po <https://registry.terraform.io/providers/greg-gajda/po/1.0.0>`_ (greg-gajda/po/1.0.0)
* `postgresql <https://registry.terraform.io/providers/cyrilgdn/postgresql/1.14.0>`_ (cyrilgdn/postgresql/1.14.0)
* `puppetca <https://registry.terraform.io/providers/camptocamp/puppetca/1.3.0>`_ (camptocamp/puppetca/1.3.0)
* `puppetdb <https://registry.terraform.io/providers/camptocamp/puppetdb/1.2.0>`_ (camptocamp/puppetdb/1.2.0)
* `pypi <https://registry.terraform.io/providers/jeffwecan/pypi/0.0.9>`_ (jeffwecan/pypi/0.0.9)
* `qingcloud <https://registry.terraform.io/providers/shaowenchen/qingcloud/1.2.6>`_ (shaowenchen/qingcloud/1.2.6)
* `rabbitmq <https://registry.terraform.io/providers/cyrilgdn/rabbitmq/1.6.0>`_ (cyrilgdn/rabbitmq/1.6.0)
* `rancher <https://registry.terraform.io/providers/eLobeto/rancher/1.5.1>`_ (eLobeto/rancher/1.5.1)
* `restapi <https://registry.terraform.io/providers/gavinbunney/restapi/1.15.4>`_ (gavinbunney/restapi/1.15.4)
* `rollbar <https://registry.terraform.io/providers/davidji99/rollbar/1.5.1>`_ (davidji99/rollbar/1.5.1)
* `sakuracloud <https://registry.terraform.io/providers/sacloud/sakuracloud/2.12.0>`_ (sacloud/sakuracloud/2.12.0)
* `scaffolding <https://registry.terraform.io/providers/iwarapter/scaffolding/0.0.1>`_ (iwarapter/scaffolding/0.0.1)
* `scaffolding <https://registry.terraform.io/providers/unicell/scaffolding/0.0.2>`_ (unicell/scaffolding/0.0.2)
* `selectel <https://registry.terraform.io/providers/selectel/selectel/3.6.2>`_ (selectel/selectel/3.6.2)
* `sendgrid <https://registry.terraform.io/providers/davidji99/sendgrid/0.1.1>`_ (davidji99/sendgrid/0.1.1)
* `sendgrid <https://registry.terraform.io/providers/Trois-Six/sendgrid/0.1.6>`_ (Trois-Six/sendgrid/0.1.6)
* `sentry <https://registry.terraform.io/providers/jianyuan/sentry/0.6.0>`_ (jianyuan/sentry/0.6.0)
* `seq <https://registry.terraform.io/providers/innovationnorway/seq/0.1.0-alpha.5>`_ (innovationnorway/seq/0.1.0-alpha.5)
* `shell <https://registry.terraform.io/providers/scottwinkler/shell/1.7.7>`_ (scottwinkler/shell/1.7.7)
* `shellescape <https://registry.terraform.io/providers/bgpat/shellescape/0.0.2>`_ (bgpat/shellescape/0.0.2)
* `snowflake <https://registry.terraform.io/providers/chanzuckerberg/snowflake/0.25.19>`_ (chanzuckerberg/snowflake/0.25.19)
* `sops <https://registry.terraform.io/providers/carlpett/sops/0.6.3>`_ (carlpett/sops/0.6.3)
* `spinnaker <https://registry.terraform.io/providers/mercari/spinnaker/0.3.0>`_ (mercari/spinnaker/0.3.0)
* `split <https://registry.terraform.io/providers/davidji99/split/0.2.0>`_ (davidji99/split/0.2.0)
* `sql <https://registry.terraform.io/providers/paultyng/sql/0.4.0>`_ (paultyng/sql/0.4.0)
* `sshcommand <https://registry.terraform.io/providers/invidian/sshcommand/0.2.2>`_ (invidian/sshcommand/0.2.2)
* `statuspage <https://registry.terraform.io/providers/yannh/statuspage/0.1.7>`_ (yannh/statuspage/0.1.7)
* `stdlib <https://registry.terraform.io/providers/invidian/stdlib/0.1.1>`_ (invidian/stdlib/0.1.1)
* `sys <https://registry.terraform.io/providers/mildred/sys/1.3.25>`_ (mildred/sys/1.3.25)
* `systemd <https://registry.terraform.io/providers/mildred/systemd/0.0.1>`_ (mildred/systemd/0.0.1)
* `teamcity <https://registry.terraform.io/providers/jeffwecan/teamcity/1.0.1-jeffwecan-fork>`_ (jeffwecan/teamcity/1.0.1-jeffwecan-fork)
* `testing <https://registry.terraform.io/providers/apparentlymart/testing/0.0.2>`_ (apparentlymart/testing/0.0.2)
* `tfvars <https://registry.terraform.io/providers/innovationnorway/tfvars/0.0.1>`_ (innovationnorway/tfvars/0.0.1)
* `tls <https://registry.terraform.io/providers/invidian/tls/2.2.1>`_ (invidian/tls/2.2.1)
* `tls <https://registry.terraform.io/providers/someara/tls/2.3.0-pre>`_ (someara/tls/2.3.0-pre)
* `tozny <https://registry.terraform.io/providers/tozny/tozny/0.14.0>`_ (tozny/tozny/0.14.0)
* `transip <https://registry.terraform.io/providers/aequitas/transip/0.1.11>`_ (aequitas/transip/0.1.11)
* `travis <https://registry.terraform.io/providers/bgpat/travis/0.1.6>`_ (bgpat/travis/0.1.6)
* `twitter <https://registry.terraform.io/providers/paultyng/twitter/0.1.0>`_ (paultyng/twitter/0.1.0)
* `ucloud <https://registry.terraform.io/providers/ucloud/ucloud/1.29.0>`_ (ucloud/ucloud/1.29.0)
* `ucodecov <https://registry.terraform.io/providers/at-wat/ucodecov/0.1.2>`_ (at-wat/ucodecov/0.1.2)
* `ultradns <https://registry.terraform.io/providers/davidji99/ultradns/2.1.0>`_ (davidji99/ultradns/2.1.0)
* `unifi <https://registry.terraform.io/providers/paultyng/unifi/0.34.0>`_ (paultyng/unifi/0.34.0)
* `uptimerobot <https://registry.terraform.io/providers/invidian/uptimerobot/0.5.1-gb83a310>`_ (invidian/uptimerobot/0.5.1-gb83a310)
* `utravis <https://registry.terraform.io/providers/kamatama41/utravis/0.5.0>`_ (kamatama41/utravis/0.5.0)
* `vault <https://registry.terraform.io/providers/cyrilgdn/vault/2.23.1>`_ (cyrilgdn/vault/2.23.1)
* `vault <https://registry.terraform.io/providers/jeffwecan/vault/2.11.0-withsleep>`_ (jeffwecan/vault/2.11.0-withsleep)
* `vaultutility <https://registry.terraform.io/providers/AdrienneCohea/vaultutility/0.0.3>`_ (AdrienneCohea/vaultutility/0.0.3)
* `vinyldns <https://registry.terraform.io/providers/vinyldns/vinyldns/0.9.5>`_ (vinyldns/vinyldns/0.9.5)
* `virtualbox <https://registry.terraform.io/providers/terra-farm/virtualbox/0.2.2-alpha.1>`_ (terra-farm/virtualbox/0.2.2-alpha.1)
* `vsphere <https://registry.terraform.io/providers/techBeck03/vsphere/1.24.3-patch>`_ (techBeck03/vsphere/1.24.3-patch)
* `windns <https://registry.terraform.io/providers/PortOfPortland/windns/0.5.3>`_ (PortOfPortland/windns/0.5.3)
* `xenorchestra <https://registry.terraform.io/providers/terra-farm/xenorchestra/0.21.0>`_ (terra-farm/xenorchestra/0.21.0)
* `zerotier <https://registry.terraform.io/providers/bltavares/zerotier/0.3.0>`_ (bltavares/zerotier/0.3.0)

Unsupported providers
^^^^^^^^^^^^^^^^^^^^^

The following providers are not supported.


* `aiven <https://registry.terraform.io/providers/juniorz/aiven/0.1.0>`_ (juniorz/aiven/0.1.0) - Failed to initialise provider
* `appd <https://registry.terraform.io/providers/maskerade/appd/0.0.5>`_ (maskerade/appd/0.0.5) - Failed to initialise provider
* `flexkube <https://registry.terraform.io/providers/invidian/flexkube/0.3.3>`_ (invidian/flexkube/0.3.3) - Failed to initialise provider
* `googlecalendar <https://registry.terraform.io/providers/sethvargo/googlecalendar/0.3.1>`_ (sethvargo/googlecalendar/0.3.1) - Failed to initialise provider
* `grafana <https://registry.terraform.io/providers/58231/grafana/0.0.2>`_ (58231/grafana/0.0.2) - 58231 is not a valid Python identifier
* `ipam <https://registry.terraform.io/providers/beauknowssoftware/ipam/0.2.6>`_ (beauknowssoftware/ipam/0.2.6) - Failed to initialise provider
* `k8s <https://registry.terraform.io/providers/mingfang/k8s/1.0.2>`_ (mingfang/k8s/1.0.2) - Failed to process provider
* `kind1 <https://registry.terraform.io/providers/unicell/kind1/0.0.2-u2>`_ (unicell/kind1/0.0.2-u2) - Failed to initialise provider
* `lxd <https://registry.terraform.io/providers/arren-ru/lxd/1.4.0>`_ (arren-ru/lxd/1.4.0) - Failed to initialise provider
* `null <https://registry.terraform.io/providers/paultyng/null/0.1.1>`_ (paultyng/null/0.1.1) - Failed to initialise provider
* `null <https://registry.terraform.io/providers/ptyng/null/0.1.1>`_ (ptyng/null/0.1.1) - Failed to initialise provider
* `okta <https://registry.terraform.io/providers/gavinbunney/okta/3.12.7>`_ (gavinbunney/okta/3.12.7) - Failed to initialise provider
* `okta <https://registry.terraform.io/providers/oktadeveloper/okta/3.13.13>`_ (oktadeveloper/okta/3.13.13) - Failed to initialise provider
* `pass <https://registry.terraform.io/providers/camptocamp/pass/2.0.0>`_ (camptocamp/pass/2.0.0) - pass is a Python keyword
* `safedns <https://registry.terraform.io/providers/ukfast/safedns/1.1.2>`_ (ukfast/safedns/1.1.2) - Failed to process provider
* `shakenfist <https://registry.terraform.io/providers/shakenfist/shakenfist/0.2.5>`_ (shakenfist/shakenfist/0.2.5) - Failed to initialise provider
* `unofficial-travis <https://registry.terraform.io/providers/kamatama41/unofficial-travis/0.5.0>`_ (kamatama41/unofficial-travis/0.5.0) - Failed to initialise provider
* `vmworkstation <https://registry.terraform.io/providers/elsudano/vmworkstation/0.2.3>`_ (elsudano/vmworkstation/0.2.3) - Failed to process provider
* `zerotier <https://registry.terraform.io/providers/someara/zerotier/0.1.47>`_ (someara/zerotier/0.1.47) - Failed to initialise provider
