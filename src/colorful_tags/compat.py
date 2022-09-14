# -*- coding: utf-8 -*-

# Hierarchical Tags 2 for Anki
#
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
# Copyright (C) 2018-2022  Aristotelis P. <https//glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path

try:
    # be super defensive
    try:
        from anki.buildinfo import version as anki_version
    except (ImportError, ModuleNotFoundError):
        from anki import version as anki_version  # type: ignore

    anki_version_tuple = tuple(int(i) for i in anki_version.split("."))
except Exception:
    # if version comparison fails, e.g. if future version format changes,
    # fall back to a high version number
    anki_version_tuple = (9999, 0, 0)

_user_files_path = Path(__file__).parent / "user_files"
if not _user_files_path.exists():
    _user_files_path.mkdir(exist_ok=True)

_notified_file = _user_files_path / ".compat_notified"


def maybe_notify_anki_update_needed():
    if _notified_file.exists():
        return
    from aqt.utils import showInfo

    showInfo(
        title="Update Anki to Enable Colorful Tags",
        text=(
            "Hi there, thanks for installing <b>Colorful Tags</b> or updating to it"
            " from Hierarchical Tags!<br><br>It looks like you are using an older"
            " version of Anki. To enable tag coloring, please update to Anki 2.1.45 or"
            " later.<br><br>If you want to continue using hierarchical tag features"
            " only, that's completely fine as well! The add-on will continue working as"
            " you are used to and this notification will not show up again.<br><br>–"
            " Glutanimate"
        ),
    )

    _notified_file.touch()
