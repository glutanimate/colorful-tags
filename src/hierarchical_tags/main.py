# -*- coding: utf-8 -*-

"""
This file is part of the Hierarchical Tags 2 add-on for Anki.

Main Module, hooks add-on methods into Anki.

Copyright: (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

import os

from aqt import mw
from aqt.browser import Browser
from aqt import tagedit
from aqt.utils import askUser, showInfo

from anki.hooks import addHook, wrap

from .browser import userTagTree, onTagClick
from .tagedit import CustomTagCompleter, CustomTagEdit

from .consts import anki21
from .config import local_conf


def uninstallHierarchicalTags(htags_path=None):
    if anki21:
        mw.addonManager.deleteAddon("1835859645")
        showInfo("Uninstall successful. Please restart Anki.")
    elif htags_path:
        mw.addonManager.onRem(htags_path)


def setupAddon():

    if anki21:
        name = "1835859645"
    else:
        name = "HierarchicalTags.py"
    htags_path = os.path.join(mw.addonManager.addonsFolder(), name)

    if os.path.exists(htags_path):
        choice = askUser(
            "It seems like you still have an old version of the "
            "<i>Hierarchical Tags</i> add-on installed. "
            "In order for <i>Hierarchical Tags 2</i> to work properly it is "
            "important that you remove that version first."
            "<br><br><b>Would you like Anki to do this for you now?</b>",
            title="Hierarchical Tags 2 Installation",
            parent=mw
        )
        if choice:
            uninstallHierarchicalTags(htags_path)



# Patches

Browser.onTagClick = onTagClick
# Patch browser sidebar
Browser._userTagTree = wrap(Browser._userTagTree, userTagTree, 'around')

if local_conf["completerEnable"]:
    tagedit.TagEdit = CustomTagEdit
    tagedit.TagCompleter = CustomTagCompleter

# Hooks

addHook("profileLoaded", setupAddon)
