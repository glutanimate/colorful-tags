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


from aqt.browser import SidebarItemType  # type: ignore
from aqt.qt import QColor, QFont, QModelIndex, Qt, QVariant
from aqt.theme import theme_manager

from .item import PatchedSideBarItem


def model_data(
    self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole
) -> QVariant:
    if not index.isValid():
        return QVariant()

    if role not in (
        Qt.ItemDataRole.DisplayRole,
        Qt.ItemDataRole.DecorationRole,
        Qt.ItemDataRole.ToolTipRole,
        Qt.ItemDataRole.EditRole,
        Qt.ItemDataRole.FontRole,
        Qt.ItemDataRole.ForegroundRole,
    ):
        return QVariant()

    item: PatchedSideBarItem = index.internalPointer()

    if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
        return QVariant(item.name)
    elif role == Qt.ItemDataRole.ToolTipRole:
        return QVariant(item.tooltip)
    elif role == Qt.ItemDataRole.DecorationRole:
        return QVariant(theme_manager.icon_from_resources(item.icon))

    # add-on roles
    elif role == Qt.ItemDataRole.FontRole:
        if item.item_type == SidebarItemType.TAG and item.is_pinned:
            font = QFont()
            font.setBold(True)
            maybe_deinstrument_object(font)
            return QVariant(font)
    elif role == Qt.ItemDataRole.ForegroundRole:
        if item.item_type == SidebarItemType.TAG and item.color:
            color = QColor(item.color)
            maybe_deinstrument_object(color)
            return QVariant(color)

    return QVariant()


def maybe_deinstrument_object(obj):
    # reverts a QtClassProxy to it's original type
    # needed due to monkey patching done in aqt.qt5_compat.py
    # Qt expects a type e.g. QFont and gets a proxy so it does not work
    if obj.__class__.__name__ == "QtClassProxy":
        setattr(obj, "__class__", obj.__class__.__bases__[0])
