# Changelog

## [Unreleased]

### [ 0.5.1] - 2018-May-10
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
