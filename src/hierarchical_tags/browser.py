# -*- coding: utf-8 -*-

# Hierarchical Tags 2 for Anki
#
# Copyright (C) Ankitects Pty Ltd and contributors
# Coypright (C) 2014  Patrice Neff <http://patrice.ch/>
# Copyright (C) 2018-2020  Aristotelis P. <https//glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from aqt.browser import SidebarItem

from .config import getConfig

SEPARATOR = getConfig()["Separator"]

# < 2.1.17

def userTagTreeOld(self, root, _old):
    tags = sorted(self.col.tags.all())
    tags_tree = {}

    for t in tags:
        if t.lower() == "marked" or t.lower() == "leech":
            continue

        components = t.split(SEPARATOR)
        for idx, c in enumerate(components):
            partial_tag = SEPARATOR.join(components[0:idx + 1])
            if not tags_tree.get(partial_tag):
                if idx == 0:
                    parent = root
                else:
                    parent_tag = SEPARATOR.join(components[0:idx])
                    parent = tags_tree[parent_tag]

                item = self.CallbackItem(
                    parent, c, None)
                item.onclick = lambda i=item, t=partial_tag: self.onTagClick(
                    i, t)
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable |
                            Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
                item.setIcon(0, QIcon(":/icons/anki-tag.png"))

                tags_tree[partial_tag] = item


def onTagClickOld(self, item, tag):
    if item.childCount():  # has children
        self.setFilter('("tag:{0}" or "tag:{0}::*")'.format(tag))
    else:
        self.setFilter("tag", tag)

# >= 2.1.17

def userTagTree(self, root, _old):
    tags = sorted(self.col.tags.all())
    tags_tree = {}

    for t in tags:
        if t.lower() == "marked" or t.lower() == "leech":
            continue

        components = t.split(SEPARATOR)
        for idx, c in enumerate(components):
            partial_tag = SEPARATOR.join(components[0 : idx + 1])
            if not tags_tree.get(partial_tag):
                if idx == 0:
                    parent = root
                else:
                    parent_tag = SEPARATOR.join(components[0:idx])
                    parent = tags_tree[parent_tag]

                item = SidebarItem(c, ":/icons/tag.svg")
                item.onClick = lambda i=item, t=partial_tag: self.onTagClick(i, t)

                tags_tree[partial_tag] = item

                parent.addChild(item)

def onTagClick(self, item, tag):
    if item.children:  # has children
        self.setFilter('("tag:{0}" or "tag:{0}::*")'.format(tag))
    else:
        self.setFilter("tag", tag)
