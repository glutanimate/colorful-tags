# Changelog

All notable changes to Colorful Tags will be documented here. You can click on each release number to be directed to a detailed log of all code commits for that particular release. The download links will direct you to the GitHub release page, allowing you to manually install a release if you want.

## [Unreleased]

## [3.0.0] - 2022-09-15

### [Download](https://github.com/glutanimate/colorful-tags-temp/releases/tag/v3.0.0)

### Added

- Ability to **color** and **pin** tags
- Support for modern Anki versions, including 2.1.54+

### Changed

- Renamed the add-on to *Colorful Tags (+Hierarchical Tags)*
- Fully rewrote the add-on with future Anki releases in mind
- Reworked project structure to simplify collaboration on new features and fixes

Thanks to Rumo and RisingOrange for their contributions towards this release!

## [2.0.4] - 2021-03-07

### [Download](https://github.com/glutanimate/hierarchical-tags/releases/tag/v2.0.4)

**NOTE**: Anki versions 2.1.41 and up now ship with a native version of hierarchical tags. The "Hierarchical Tags 2" add-on will continue to be offered for users on earlier versions of Anki, and might be extended with features built on top of Anki's native functionality in the future. Stay tuned for more on that in the future!

### Fixed

- Fixed start-up error on Anki 2.1.41 by disabling the add-on

## [2.0.3] - 2020-04-11

### [Download](https://github.com/glutanimate/hierarchical-tags/releases/tag/v2.0.3)

### Fixed

- Make sure to use custom separator in searches (if set)
- Fix "marked" and "leech" tags missing from sidebar (thanks to @Weyaaron for the report!). To make them appear as they used to in Anki 2.0, I recommend installing the [Customize Sidebar add-on](https://ankiweb.net/shared/info/1988760596)

### Changed

- Improve config description and add a config schema to check for invalid configurations

## [2.0.2] - 2020-01-29

### [Download](https://github.com/glutanimate/hierarchical-tags/releases/tag/v2.0.2)

### Fixed

- Fix incompatibility introduced by latest Night Mode update

## [2.0.1] - 2020-01-21

### [Download](https://github.com/glutanimate/hierarchical-tags/releases/tag/v2.0.1)

### Changed

- Improved in-app config documentation

## [2.0.0] - 2020-01-11

### [Download](https://github.com/glutanimate/hierarchical-tags/releases/tag/v2.0.0)

### Added

- Initial release of Hierarchical Tags 2
- Support for Anki >=2.1.17

## [1.0.0] - 2014-04

### Added

- Initial release of "[Hierachical Tags](https://ankiweb.net/shared/info/1089921461)" by [Patrice Neff](https://patrice.ch/)

[Unreleased]: https://github.com/glutanimate/hierarchical-tags/compare/v2.0.4...HEAD
[2.0.4]: https://github.com/glutanimate/hierarchical-tags/compare/v2.0.3...v2.0.4
[2.0.3]: https://github.com/glutanimate/hierarchical-tags/compare/v2.0.2...v2.0.3
[2.0.2]: https://github.com/glutanimate/hierarchical-tags/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/glutanimate/hierarchical-tags/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/glutanimate/hierarchical-tags/compare/d36fc72178a4962713ced27910d1c4039810c8f4...v2.0.0
[1.0.0]: https://github.com/glutanimate/hierarchical-tags/commit/d36fc72178a4962713ced27910d1c4039810c8f4

-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).