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
