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

from aqt.browser import SidebarItem, SidebarModel  # type: ignore
from aqt.gui_hooks import browser_sidebar_will_show_context_menu

from .item import add_sidebar_item_child
from .menu import maybe_add_context_actions
from .model import model_data


def patch_sidebar():
    SidebarItem.add_child = add_sidebar_item_child  # type: ignore[assignment]
    SidebarModel.data = model_data  # type: ignore[assignment]
    browser_sidebar_will_show_context_menu.append(maybe_add_context_actions)
