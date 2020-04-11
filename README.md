<p align="center"><img src="screenshots/screenshot.png"></p>

<h2 align="center">Hierarchical Tags 2 for Anki</h2>

<p align="center">
<a title="Latest (pre-)release" href="https://github.com/glutanimate/hierarchical-tags/releases"><img src ="https://img.shields.io/github/release-pre/glutanimate/hierarchical-tags.svg?colorB=brightgreen"></a>
<a title="License: GNU AGPLv3" href="https://github.com/glutanimate/hierarchical-tags/blob/master/LICENSE"><img  src="https://img.shields.io/badge/license-GNU AGPLv3-green.svg"></a>
<a title="Rate on AnkiWeb" href="https://ankiweb.net/shared/info/1722658993"><img src="https://glutanimate.com/logos/ankiweb-rate.svg"></a>
<br>
<a title="Follow me on Twitter" href="https://twitter.com/intent/user?screen_name=glutanimate"><img src="https://img.shields.io/twitter/follow/glutanimate.svg"></a>
</p>

> Brings some structure to your Anki tags!

An add-on for the spaced-repetition flashcard app [Anki](https://apps.ankiweb.net/) that allows structuring your tags in hierarchies. Based on [Patrice Neff](https://patrice.ch/)'s original [Hierarchical Tags](https://ankiweb.net/shared/info/1089921461), with a number of small improvements and tweaks to make it work on newer Anki releases.

### Table of Contents

<!-- MarkdownTOC -->

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Documentation](#documentation)
- [Building](#building)
- [Contributing](#contributing)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Installation

#### AnkiWeb <!-- omit in toc -->

The easiest way to install Hierarchical Tags 2 is through [AnkiWeb](https://ankiweb.net/shared/info/594329229).

#### Manual installation <!-- omit in toc -->

Please click on the entry corresponding to your Anki version:

<details>

<summary><i>Anki 2.1</i></summary>

1. Make sure you have the [latest version](https://apps.ankiweb.net/#download) of Anki 2.1 installed. Earlier releases (e.g. found in various Linux distros) do not support `.ankiaddon` packages.
2. Download the latest `.ankiaddon` package from the [releases tab](https://github.com/glutanimate/hierarchical-tags/releases) (you might need to click on *Assets* below the description to reveal the download links)
3. From Anki's main window, head to *Tools* → *Add-ons*
4. Drag-and-drop the `.ankiaddon` package onto the add-ons list
5. Restart Anki

</details>

### Documentation

For further information on the use of this add-on please check out [the description text](docs/description.md) for AnkiWeb.

### Building

With [Anki add-on builder](https://github.com/glutanimate/anki-addon-builder/) installed:

    git clone https://github.com/glutanimate/hierarchical-tags.git
    cd hierarchical-tags
    aab build

For more information on the build process please refer to [`aab`'s documentation](https://github.com/glutanimate/anki-addon-builder/#usage).

### Contributing

Contributions are welcome! Please review the [contribution guidelines](./CONTRIBUTING.md) on how to:

- Report issues
- File pull requests
- Support the project as a non-developer

### License and Credits

*Hierarchical Tags 2* is

- *Copyright © 2014 [Patrice Neff](http://patrice.ch/)*

- *Copyright © 2018-2020 [Aristotelis P.](https://glutanimate.com/) (Glutanimate)*

Hierarchical Tags 2 is free and open-source software. The add-on code that runs within Anki is released under the GNU AGPLv3 license. For more information please see the [LICENSE](https://github.com/glutanimate/hierarchical-tags/blob/master/LICENSE) file that accompanied this program.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.
