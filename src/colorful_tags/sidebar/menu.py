# -*- coding: utf-8 -*-

# Colorful Tags for Anki
#
# Copyright (C) 2018-2021  Aristotelis P. <https//glutanimate.com/>
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

from typing import TYPE_CHECKING

from aqt.browser import SidebarItemType
from aqt.qt import *

from .item import PatchedSideBarItem
from ..data import save, tag_data

if TYPE_CHECKING:
    from aqt.browser import SidebarTreeView


def maybe_add_context_actions(
    sidebar: "SidebarTreeView", menu: QMenu, item: PatchedSideBarItem, index: QModelIndex
):
    if item.item_type == SidebarItemType.TAG:
        menu.addSeparator()
        pin_action = "Unpin" if item.is_pinned else "Pin"
        menu.addAction(pin_action, lambda: _toggle_pin(sidebar, item))
        menu.addAction("Assign Color", lambda: _assign_color(sidebar, item))
        if item.color:
            menu.addAction("Remove Color", lambda: _remove_color(sidebar, item))


def _toggle_pin(sidebar: "SidebarTreeView", item: PatchedSideBarItem):
    if tag := tag_data().get(item.full_name, None):
        if tag.get("pin", False):
            del tag["pin"]
            if not len(tag):
                del tag_data()[item.full_name]
        else:
            tag["pin"] = True
    else:
        tag_data()[item.full_name] = {"pin": True}
    save()
    sidebar.refresh()


def _assign_color(sidebar: "SidebarTreeView", item: PatchedSideBarItem):
    color = QColor(item.color or "#000000")
    dialog = QColorDialog(color, parent=sidebar)
    color = dialog.getColor(color)
    if color.isValid():
        if not (tag := tag_data().get(item.full_name, None)):
            tag = tag_data()[item.full_name] = {}
        tag["color"] = color.name()
        save()
        sidebar.refresh()


def _remove_color(sidebar: "SidebarTreeView", item: PatchedSideBarItem):
    if tag := tag_data().get(item.full_name, None):
        if "color" in tag:
            del tag["color"]
            if not len(tag):
                del tag_data()[item.full_name]
            save()
            sidebar.refresh()
