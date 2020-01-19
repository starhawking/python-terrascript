# Changelog

## [0.9.0] - Not yet released
### Deprecated
* Individual modules for each provider (Example: ``terrascript.aws.r``) are now deprecated in favour of
  single modules as added in release 0.8.0. 

## [0.8.0] - 2020-01-20
**This release requires Terraform 0.12 or later.**
### Added
* Almost complete rewrite to align it with Terraform 0.12 JSON syntax. 
* Providers, resources and data sources are now accessible through single modules instead of 
  individual modules for each provider.
* The module ``terrascript.providers`` contains **all** providers, e.g. ``terrascript.providers.google``.
* The module ``terrascript.resources`` contains **all** resource, e.g. ``terrascript.resources.aws_instance``.
* The module ``terrascript.datasources`` contains **all** resource, e.g. ``terrascript.datasources.alicloud_images``.
* [Oracle Cloud Infrastructure Provider](https://www.terraform.io/docs/providers/oci/index.html) (issue #63)

## [0.7.0] - Skipped

## [0.6.1] - 2019-08-17
### Added
* Locals resouce (pull #71)
* null provider resouces (pull #69)
* aws_rds_cluster_endpoint (pull #60)
* aws_kms_grant resource (pull #61)
* aws_config_configuration_aggregator resource (pull #61)
* Added many resources (pull #67)
### Updated
* Updated all terraform provider resources (pull #67)
* Updated DigitalOcean resources (pull #58)
### Fixed
* Added missing escape quote to the result json dump (pull #57)
* Remove temp directory after validation (pull #64)
### Removed
* Support for all Terraform versions prior to release 0.12.
## [0.6.0] - 2018-09-28
### Added
* vSphere data sources/resources (pull #52)
* Added new aws resources (pull #51)
* Update azurerm resource and the function `interpolated` (pull #53)
* Added support for update terrascript from another terrascript. Same behavior as dict().update (pull #37)
* Added new cloudflare resources and data (pull #54)
* Added tests for Terraform 0.11.8
## [0.5.1] - 2018-05-10
### Fixed
* Work-around for data/JSON bug  (issue #3).
* Fixed `provisioner` (issue #32)
### Added
* `Terrascript.add()` method (issue #33).
* Missing vSphere data sources and resources (issue #35).
### Removed
* Dropped support for Terraform < 0.10.6 (issue #38).

## [0.5.0] - 2018-Mar-18
### Fixed
* Problem when using resource in a loop (issue #26)
### Added
* Added `terrascript.Terrascript` class wich makes this release
  incompatible with earlier ones.
* Allow multiple providers (issue #22)

## [0.4.0] - 2017-11-21
### Added
* Added all other providers.

## [0.3.0] - 2017-11-17
### Added
* Added more providers (please report any bugs)
* Added note about how to create provider modules in README.

## [0.2.1] - 2017-08-02
### Fixed
* Added `MANIFEST.in` which I completely forgot.
* Allow data sources without any keyword arguments.
### Added
* Webserver Cluster example based on chapter 4 of "Terraform: Up and Running"

## [0.2.0] - 2017-07-26
### Added
* `google` provider.
* `azurerm` provider.
* `terraform` provider.
* `template` provider.
* `openstack` provider.
* `kubernetes` provider.
* `docker` provider.

## [0.1.0] - 2017-07-25
* First release.
* Supports only AWS provider.

Follows [keep a changelog](http://keepachangelog.com) format.
