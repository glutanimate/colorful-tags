# -*- coding: utf-8 -*-

# Colorful Tags for Anki
#
# Copyright (C) 2018-2022  Aristotelis P. <https//glutanimate.com/>
# Copyright (C) 2021  RumovZ <gp5glkw78@relay.firefox.com>
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
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

from aqt import mw

from ._version import __version__  # noqa: F401
from .compat import anki_version_tuple

if anki_version_tuple >= (2, 1, 45):
    from .sidebar import patch_sidebar

    patch_sidebar()
else:
    from aqt.gui_hooks import profile_did_open

    from .compat import maybe_notify_anki_update_needed

    if anki_version_tuple < (2, 1, 41):
        # 2.1.41 - 2.1.44 are in a limbo state where neither the old nor new patches
        # work. So skip them.

        from .sidebar_legacy import patch_sidebar

        patch_sidebar()

    def delayed_notification():
        mw.progress.timer(  # type: ignore
            500, maybe_notify_anki_update_needed, False, False
        )

    profile_did_open.append(delayed_notification)
