# -*- encoding: utf-8 -*-
"""Creates a setting "show_minimap" in the root settings that removes
the minimap that's typically on the right side of the screen when set to
false.
"""

# Stolen from https://stackoverflow.com/a/46959583/2252772

import sublime
import sublime_plugin


class MinimapSetting(sublime_plugin.EventListener):
    def on_activated(self, view):
        show_minimap = view.settings().get("show_minimap")
        if show_minimap is False:
            view.window().set_minimap_visible(False)
