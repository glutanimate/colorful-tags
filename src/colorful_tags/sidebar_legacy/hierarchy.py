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

from aqt.browser import SidebarItem  # type: ignore
from ..config import get_config

SEPARATOR = get_config().get("Separator", "::")


def user_tag_tree(self, root, _old):
    tags = sorted(self.col.tags.all())
    tags_tree = {}

    for t in tags:
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
                item.onClick = lambda i=item, t=partial_tag: self.onTagClick(i, t)  # type: ignore

                tags_tree[partial_tag] = item

                parent.addChild(item)


def on_tag_click(self, item, tag):
    if item.children:  # has children
        self.setFilter(f'("tag:{tag}" or "tag:{tag}{SEPARATOR}*")')
    else:
        self.setFilter("tag", tag)
