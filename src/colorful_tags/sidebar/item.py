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

from aqt.browser import SidebarItemType, SidebarItem

from ..data import tag_data


def add_sidebar_item_child(self: SidebarItem, child: SidebarItem) -> None:
    child._parent_item = self
    if child.item_type == SidebarItemType.TAG:
        child.is_pinned = False
        child.color = None
        if child_data := tag_data().get(child.full_name):
            child.color = child_data.get("color", None)
            if child_data.get("pin", False):
                child.is_pinned = True
                pinned_children = getattr(self, "pinned_children", 0)
                self.children.insert(pinned_children, child)
                self.pinned_children = pinned_children + 1
                return
    self.children.append(child)
