# -*- coding: utf-8 -*-

"""
This file is part of the Hierarchical Tags 2 add-on for Anki

Modifications to the card browser

Copyright: (c) Patrice Neff 2014 <http://patrice.ch/>
           (c) Glutanimate 2018 <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""


from aqt.qt import *

from .config import local_conf


SEPARATOR = local_conf["Separator"]


def userTagTree(self, root, _old):
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
                item.setIcon(0, QIcon(":/icons/anki-tag.png"))

                tags_tree[partial_tag] = item


def onTagClick(self, item, tag):
    if item.childCount():  # has children
        self.setFilter('("tag:{0}" or "tag:{0}::*")'.format(tag))
    else:
        self.setFilter("tag", tag)
