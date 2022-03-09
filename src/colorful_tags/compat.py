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

_notified_file = Path(__file__).parent / ".compat_notified"


def maybe_notify_anki_update_needed():
    if _notified_file.exists():
        return
    from aqt.utils import showInfo

    showInfo(
        title="Update Anki to enable Colorful Tags",
        text=(
            "Hi there! Thanks for installing Colorful Tags / updating to it from"
            " Hierarchical Tags. It looks like you are using an older version of Anki."
            " To enable tag coloring, please update to Anki 2.1.45 or later. If"
            " you want to continue using hierarchical tag features only, that's"
            " completely fine as well! This window will not show up again."
        ),
    )

    _notified_file.touch()