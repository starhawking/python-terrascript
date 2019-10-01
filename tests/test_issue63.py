# https://github.com/mjuenema/python-terrascript/issues/63
# https://www.terraform.io/docs/providers/oci/index.html

import terrascript
import terrascript.oci

from shared import assert_equals_json


def test():
    """Issue #63 - Add support for OCI provider

       Example based on https://www.terraform.io/docs/providers/oci/index.html

            # Configure the Oracle Cloud Infrastructure provider with an API Key
            provider "oci" {
                tenancy_ocid = "${var.tenancy_ocid}"
                user_ocid = "${var.user_ocid}"
                fingerprint = "${var.fingerprint}"
                private_key_path = "${var.private_key_path}"
                region = "${var.region}"
            }

            # Get a list of Availability Domains
            data "oci_identity_availability_domains" "ads" {
                compartment_id = "${var.tenancy_ocid}"
            }

            # Output the result
            output "show-ads" {
                value = "${data.oci_identity_availability_domains.ads.availability_domains}"
            }

    """

    config = terrascript.Terrascript()

    tenancy_ocid = terrascript.Variable('tenancy_ocid')
    config += tenancy_ocid

    user_ocid = terrascript.Variable('user_ocid')
    config += user_ocid

    fingerprint = terrascript.Variable('fingerprint')
    config += fingerprint

    private_key_path = terrascript.Variable('private_key_path')
    config += private_key_path

    region = terrascript.Variable('region')
    config += region

    config += terrascript.oci.oci(tenancy_ocid=tenancy_ocid,
                                  user_ocid=user_ocid,
                                  fingerprint=fingerprint,
                                  private_key_path=private_key_path,
                                  region=region)

    assert_equals_json(config, 'test_issue63.tf.json')
