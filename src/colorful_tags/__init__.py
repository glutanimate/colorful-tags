from aqt.gui_hooks import browser_sidebar_will_show_context_menu
from aqt.browser import SidebarItem, SidebarModel

from .sidebar import maybe_add_context_actions, model_data, add_sidebar_item_child


browser_sidebar_will_show_context_menu.append(maybe_add_context_actions)
SidebarItem.add_child = add_sidebar_item_child
SidebarModel.data = model_data
