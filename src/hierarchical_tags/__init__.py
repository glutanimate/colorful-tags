# -*- coding: utf-8 -*-

# Hierarchical Tags 2 for Anki
#
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
# Copyright (C) 2018-2020  Aristotelis P. <https//glutanimate.com/>
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

import os

from aqt import mw
from aqt.browser import Browser
from aqt.utils import askUser, showInfo

from anki.hooks import addHook, wrap

from .browser import userTagTree, onTagClick, userTagTreeOld, onTagClickOld
from .consts import old_anki


def uninstallHierarchicalTags(htags_path=None):
    mw.addonManager.deleteAddon("1835859645")
    showInfo("Uninstall successful. Please restart Anki.")


def setupAddon():
    name = "1835859645"
    htags_path = os.path.join(mw.addonManager.addonsFolder(), name)

    if os.path.exists(htags_path):
        choice = askUser(
            "It seems like you still have an old version of the "
            "<i>Hierarchical Tags</i> add-on installed. "
            "In order for <i>Hierarchical Tags 2</i> to work properly it is "
            "important that you remove that version first."
            "<br><br><b>Would you like Anki to do this for you now?</b>",
            title="Hierarchical Tags 2 Installation",
            parent=mw,
        )
        if choice:
            uninstallHierarchicalTags(htags_path)

    if not old_anki:
        Browser.onTagClick = onTagClick
        Browser._userTagTree = wrap(Browser._userTagTree, userTagTree, "around")
    else:
        Browser.onTagClick = onTagClickOld
        Browser._userTagTree = wrap(Browser._userTagTree, userTagTreeOld, "around")


addHook("profileLoaded", setupAddon)