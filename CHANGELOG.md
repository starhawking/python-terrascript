# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased] - 2020-11-23

## [0.9.0] - 2020-11-23
**This release requires Python 3.6 or later, and Terraform 0.12 or later.**  
**Be aware of embedded variable bugfix, which could break workarounds.**  
### Added
* Automatically push of built tags to pypi
* Created ``terrascript.Terrascript.__iter__()`` method for iterating over resources, data sources, etc.  (issue #98).
* Make target and code to fail builds unless python code format passes Black
* Provider `google-beta`
* Release instruction for documentation
* RTD theme no longer bundled with Sphinx added as dev requirement
### Fixed
* Documentation generation, tests and examples cleaned up
* Missing dev requirement Black added
* Re-introduced ``terrascript.Terrascript.update()`` method (issue #98).
* String interpolation of variable should now properly result in a var.name reference (issue #109)
* terrascript module should now pass pep8 validation and have no lint errors
* Tool for generating providers now outputs code (almost) compliant with black
### Changed
* All Python code is now automatically formatted using [Black](https://pypi.org/project/black/).
* Code for providers updated to conform with black
* Contributors are now sorted in alphabetical order
* Documentation for creating releases are now updated to reflect expected flow
* Documentation link from readme now points toward develop build on readthedocs.io to avoid 404
* Documentation on variable usage updated to reflect changes in issue #109
* Makefiles cleaned up, and help target contents now dynamically generated from comments
* Requirements files are now sorted alphabetically and duplicate entries are removed
* Terraform version supported updated from 0.12.15-19 to 0.12.29 + 0.13.4-5
* Updated code for providers generated
### Deleted
* Python 3.5 no longer supported as the official support are dropped: https://devguide.python.org/#status-of-python-branches
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
