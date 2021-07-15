from aqt.qt import *
from aqt.browser import SidebarItemType

from ..data import tag_data, save


def maybe_add_context_actions(sidebar, menu, item, index):
    if item.item_type == SidebarItemType.TAG:
        menu.addSeparator()
        pin_action = "Unpin" if item.is_pinned else "Pin"
        menu.addAction(pin_action, lambda: _toggle_pin(sidebar, item))
        menu.addAction("Assign Color", lambda: _assign_color(sidebar, item))
        if item.color:
            menu.addAction("Remove Color", lambda: _remove_color(sidebar, item))


def _toggle_pin(sidebar, item):
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


def _assign_color(sidebar, item):
    color = QColor(item.color or "#000000")
    dialog = QColorDialog(color, parent=sidebar)
    color = dialog.getColor(color)
    if color.isValid():
        if not (tag := tag_data().get(item.full_name, None)):
            tag = tag_data()[item.full_name] = {}
        tag["color"] = color.name()
        save()
        sidebar.refresh()


def _remove_color(sidebar, item):
    if tag := tag_data().get(item.full_name, None):
        if "color" in tag:
            del tag["color"]
            if not len(tag):
                del tag_data()[item.full_name]
            save()
            sidebar.refresh()
