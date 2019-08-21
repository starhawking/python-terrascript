# Just some basic test

from importlib import import_module as importm

class _Base(object):
    provider = 'aws'

    def test_resources(self):
        r = importm(self.import_r)
        for k in dir(r):
            if k.startswith(self.provider):
                # Find short name 'aws_instance' -> 'instance'
                assert k[len(self.provider)+1:] in dir(r)

    def test_data(self):
        d = importm(self.import_d)
        for k in dir(d):
            if k.startswith(self.provider):
                # Find short name 'aws_instance' -> 'instance'
                assert k[len(self.provider)+1:] in dir(d)


class TestTerraform(object):
    def test(self):
        from terrascript.terraform.d import terraform_remote_state, remote_state

class TestAlicloud(_Base):
    provider = 'alicloud'
    import_r = 'terrascript.alicloud.r'
    import_d = 'terrascript.alicloud.d'

class TestArchive(_Base):
    provider = 'archive'
    import_r = 'terrascript.archive.r'
    import_d = 'terrascript.archive.d'

class TestArukas(_Base):
    provider = 'arukas'
    import_r = 'terrascript.arukas.r'
    import_d = 'terrascript.arukas.d'

class TestAws(_Base):
    provider = 'aws'
    import_r = 'terrascript.aws.r'
    import_d = 'terrascript.aws.d'

class TestBitbucket(_Base):
    provider = 'bitbucket'
    import_r = 'terrascript.bitbucket.r'
    import_d = 'terrascript.bitbucket.d'

class TestClc(_Base):
    provider = 'clc'
    import_r = 'terrascript.clc.r'
    import_d = 'terrascript.clc.d'

class TestChef(_Base):
    provider = 'chef'
    import_r = 'terrascript.chef.r'
    import_d = 'terrascript.chef.d'

class TestCirconus(_Base):
    provider = 'circonus'
    import_r = 'terrascript.circonus.r'
    import_d = 'terrascript.circonus.d'

class TestCloudflare(_Base):
    provider = 'cloudflare'
    import_r = 'terrascript.cloudflare.r'
    import_d = 'terrascript.cloudflare.d'

class TestCloudscale(_Base):
    provider = 'cloudscale'
    import_r = 'terrascript.cloudscale.r'
    import_d = 'terrascript.cloudscale.d'

class TestCloudstack(_Base):
    provider = 'cloudstack'
    import_r = 'terrascript.cloudstack.r'
    import_d = 'terrascript.cloudstack.d'

class TestCobbler(_Base):
    provider = 'cobbler'
    import_r = 'terrascript.cobbler.r'
    import_d = 'terrascript.cobbler.d'

class TestDatadog(_Base):
    provider = 'datadog'
    import_r = 'terrascript.datadog.r'
    import_d = 'terrascript.datadog.d'

class TestDns(_Base):
    provider = 'dns'
    import_r = 'terrascript.dns.r'
    import_d = 'terrascript.dns.d'

class TestDme(_Base):
    provider = 'dme'
    import_r = 'terrascript.dme.r'
    import_d = 'terrascript.dme.d'

class TestDnsimple(_Base):
    provider = 'dnsimple'
    import_r = 'terrascript.dnsimple.r'
    import_d = 'terrascript.dnsimple.d'

class TestDocker(_Base):
    provider = 'docker'
    import_r = 'terrascript.docker.r'
    import_d = 'terrascript.docker.d'

class TestDyn(_Base):
    provider = 'dyn'
    import_r = 'terrascript.dyn.r'
    import_d = 'terrascript.dyn.d'

class TestExternal(_Base):
    provider = 'external'
    import_r = 'terrascript.external.r'
    import_d = 'terrascript.external.d'

class TestFastly(_Base):
    provider = 'fastly'
    import_r = 'terrascript.fastly.r'
    import_d = 'terrascript.fastly.d'

class TestGithub(_Base):
    provider = 'github'
    import_r = 'terrascript.github.r'
    import_d = 'terrascript.github.d'

class TestGitlab(_Base):
    provider = 'gitlab'
    import_r = 'terrascript.gitlab.r'
    import_d = 'terrascript.gitlab.d'

class TestGoogle(_Base):
    provider = 'google'
    import_r = 'terrascript.google.r'
    import_d = 'terrascript.google.d'

class TestGrafana(_Base):
    provider = 'grafana'
    import_r = 'terrascript.grafana.r'
    import_d = 'terrascript.grafana.d'

class TestHeroku(_Base):
    provider = 'heroku'
    import_r = 'terrascript.heroku.r'
    import_d = 'terrascript.heroku.d'

class TestHttp(_Base):
    provider = 'http'
    import_r = 'terrascript.http.r'
    import_d = 'terrascript.http.d'

class TestIcinga2(_Base):
    provider = 'icinga2'
    import_r = 'terrascript.icinga2.r'
    import_d = 'terrascript.icinga2.d'

class TestIgnition(_Base):
    provider = 'ignition'
    import_r = 'terrascript.ignition.r'
    import_d = 'terrascript.ignition.d'

class TestInfluxdb(_Base):
    provider = 'influxdb'
    import_r = 'terrascript.influxdb.r'
    import_d = 'terrascript.influxdb.d'

class TestKubernetes(_Base):
    provider = 'kubernetes'
    import_r = 'terrascript.kubernetes.r'
    import_d = 'terrascript.kubernetes.d'

class TestLibrato(_Base):
    provider = 'librato'
    import_r = 'terrascript.librato.r'
    import_d = 'terrascript.librato.d'

class TestLocal(_Base):
    provider = 'local'
    import_r = 'terrascript.local.r'
    import_d = 'terrascript.local.d'

class TestLogentries(_Base):
    provider = 'logentries'
    import_r = 'terrascript.logentries.r'
    import_d = 'terrascript.logentries.d'

class TestLogicmonitor(_Base):
    provider = 'logicmonitor'
    import_r = 'terrascript.logicmonitor.r'
    import_d = 'terrascript.logicmonitor.d'

class TestMailgun(_Base):
    provider = 'mailgun'
    import_r = 'terrascript.mailgun.r'
    import_d = 'terrascript.mailgun.d'

class TestAzurerm(_Base):
    provider = 'azurerm'
    import_r = 'terrascript.azurerm.r'
    import_d = 'terrascript.azurerm.d'

class TestAzure(_Base):
    provider = 'azure'
    import_r = 'terrascript.azure.r'
    import_d = 'terrascript.azure.d'

class TestMysql(_Base):
    provider = 'mysql'
    import_r = 'terrascript.mysql.r'
    import_d = 'terrascript.mysql.d'

class TestNewrelic(_Base):
    provider = 'newrelic'
    import_r = 'terrascript.newrelic.r'
    import_d = 'terrascript.newrelic.d'

class TestNomad(_Base):
    provider = 'nomad'
    import_r = 'terrascript.nomad.r'
    import_d = 'terrascript.nomad.d'

class TestNs1(_Base):
    provider = 'ns1'
    import_r = 'terrascript.ns1.r'
    import_d = 'terrascript.ns1.d'

class TestOneandone(_Base):
    provider = 'oneandone'
    import_r = 'terrascript.oneandone.r'
    import_d = 'terrascript.oneandone.d'

class TestOpc(_Base):
    provider = 'opc'
    import_r = 'terrascript.opc.r'
    import_d = 'terrascript.opc.d'

class TestOpenstack(_Base):
    provider = 'openstack'
    import_r = 'terrascript.openstack.r'
    import_d = 'terrascript.openstack.d'

class TestOpsgenie(_Base):
    provider = 'opsgenie'
    import_r = 'terrascript.opsgenie.r'
    import_d = 'terrascript.opsgenie.d'

class TestOvh(_Base):
    provider = 'ovh'
    import_r = 'terrascript.ovh.r'
    import_d = 'terrascript.ovh.d'

class TestPacket(_Base):
    provider = 'packet'
    import_r = 'terrascript.packet.r'
    import_d = 'terrascript.packet.d'

class TestPagerduty(_Base):
    provider = 'pagerduty'
    import_r = 'terrascript.pagerduty.r'
    import_d = 'terrascript.pagerduty.d'

class TestPostgresql(_Base):
    provider = 'postgresql'
    import_r = 'terrascript.postgresql.r'
    import_d = 'terrascript.postgresql.d'

class TestPowerdns(_Base):
    provider = 'powerdns'
    import_r = 'terrascript.powerdns.r'
    import_d = 'terrascript.powerdns.d'

class TestProfitbricks(_Base):
    provider = 'profitbricks'
    import_r = 'terrascript.profitbricks.r'
    import_d = 'terrascript.profitbricks.d'

class TestRabbitmq(_Base):
    provider = 'rabbitmq'
    import_r = 'terrascript.rabbitmq.r'
    import_d = 'terrascript.rabbitmq.d'

class TestRancher(_Base):
    provider = 'rancher'
    import_r = 'terrascript.rancher.r'
    import_d = 'terrascript.rancher.d'

class TestRandom(_Base):
    provider = 'random'
    import_r = 'terrascript.random.r'
    import_d = 'terrascript.random.d'

class TestRundeck(_Base):
    provider = 'rundeck'
    import_r = 'terrascript.rundeck.r'
    import_d = 'terrascript.rundeck.d'

class TestScaleway(_Base):
    provider = 'scaleway'
    import_r = 'terrascript.scaleway.r'
    import_d = 'terrascript.scaleway.d'

class TestSoftlayer(_Base):
    provider = 'softlayer'
    import_r = 'terrascript.softlayer.r'
    import_d = 'terrascript.softlayer.d'

class TestStatuscake(_Base):
    provider = 'statuscake'
    import_r = 'terrascript.statuscake.r'
    import_d = 'terrascript.statuscake.d'

class TestSpotinst(_Base):
    provider = 'spotinst'
    import_r = 'terrascript.spotinst.r'
    import_d = 'terrascript.spotinst.d'

class TestTemplate(_Base):
    provider = 'template'
    import_r = 'terrascript.template.r'
    import_d = 'terrascript.template.d'

class TestTls(_Base):
    provider = 'tls'
    import_r = 'terrascript.tls.r'
    import_d = 'terrascript.tls.d'

class TestTriton(_Base):
    provider = 'triton'
    import_r = 'terrascript.triton.r'
    import_d = 'terrascript.triton.d'

class TestUltradns(_Base):
    provider = 'ultradns'
    import_r = 'terrascript.ultradns.r'
    import_d = 'terrascript.ultradns.d'

class TestVault(_Base):
    provider = 'vault'
    import_r = 'terrascript.vault.r'
    import_d = 'terrascript.vault.d'

class TestVcd(_Base):
    provider = 'vcd'
    import_r = 'terrascript.vcd.r'
    import_d = 'terrascript.vcd.d'

class TestVsphere(_Base):
    provider = 'vsphere'
    import_r = 'terrascript.vsphere.r'
    import_d = 'terrascript.vsphere.d'

class TestConsul(_Base):
    provider = 'consul'
    import_r = 'terrascript.consul.r'
    import_d = 'terrascript.consul.d'

