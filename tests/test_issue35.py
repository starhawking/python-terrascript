from terrascript import Terrascript
import terrascript.vsphere.d as d
import terrascript.vsphere.r as r


def test_issue35():
    """Issue 35: missing some vSphere data sources and resources."""

    ts = Terrascript()

    ts += r.vsphere_custom_attribute('attribute', name='terraform-test-attribute',
                                     managed_object_type='VirtualMachine')

    ts += r.vsphere_datastore_cluster('datastore_cluster', name='terraform-datastore-cluster-test',
                                      datacenter_id='ID', sdrs_enabled=True)

    ts += r.vsphere_storage_drs_vm_override('drs_vm_override', datastore_cluster_id= 'ID1',
                                            virtual_machine_id='IS2', sdrs_enabled=False)

    ts += d.vsphere_custom_attribute('attribute',name='terraform-test-attribute')

    ts += d.vsphere_datastore_cluster('datastore_cluster', name='datastore-cluster1',
                                      datacenter_id='ID')

    assert ts.validate() is True
