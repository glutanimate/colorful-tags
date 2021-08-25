from aqt.qt import *
from aqt.theme import theme_manager
from aqt.browser import SidebarItemType, SidebarItem


def model_data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> QVariant:
    if not index.isValid():
        return QVariant()

    if role not in (
        Qt.DisplayRole,
        Qt.DecorationRole,
        Qt.ToolTipRole,
        Qt.EditRole,
        Qt.FontRole,
        Qt.ForegroundRole,
    ):
        return QVariant()

    item: SidebarItem = index.internalPointer()

    if role in (Qt.DisplayRole, Qt.EditRole):
        return QVariant(item.name)
    elif role == Qt.ToolTipRole:
        return QVariant(item.tooltip)
    elif role == Qt.DecorationRole:
        return QVariant(theme_manager.icon_from_resources(item.icon))

    # add-on roles
    elif role == Qt.FontRole:
        if item.item_type == SidebarItemType.TAG and item.is_pinned:
            font = QFont()
            font.setWeight(QFont.Bold)
            return QVariant(font)
    elif role == Qt.ForegroundRole:
        if item.item_type == SidebarItemType.TAG and item.color:
            return QVariant(QColor(item.color))

    return QVariant()
