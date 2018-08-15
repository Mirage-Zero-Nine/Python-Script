#!python3

'''
This widget script shows a grid of shortcut buttons that launch URLs when tapped.

The shortcut titles/URLs and the grid layout can be configured with the SHORTCUTS, COLS, ROWS variables.
'''

import appex, ui
import os
from math import ceil, floor

# NOTE: The ROWS variable determines the number of rows in "compact" mode. In expanded mode, the widget shows all shortcuts.
COLS = 4
ROWS = 2

'''
This widget script shows a grid of shortcut buttons that launch URLs when tapped.
The shortcut titles/URLs and the grid layout can be configured with the SHORTCUTS, COLS, ROWS variables.
Each shortcut should be a dict with at least a 'title' and 'url' key. 'color' and 'icon' are optional. 
If set, 'icon' should be the name of a built-in image.
The URL can be iOS url-scheme or internet URL.
'''
SHORTCUTS = [

# Add your own buttom here
{'title': 'Calander', 'url': 'calshow://', 'color': '#d29898', 'icon': 'iow:calendar_24'},
]

class LauncherView (ui.View):
	def __init__(self, shortcuts, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for s in shortcuts:
			btn = ui.Button(title=' ' + s['title'], image=ui.Image(s.get('icon', 'iow:compass_24')), name=s['url'], action=self.button_action, bg_color=s.get('color', '#55bcff'), tint_color='#fff', corner_radius=9)
			self.add_subview(btn)
			self.buttons.append(btn)
	
	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw + 1, i//COLS * bh, bw - 1, bh - 1).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		import webbrowser
		webbrowser.open(sender.name)

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	if v is None or v.name != widget_name:
		v = LauncherView(SHORTCUTS)
		v.name = widget_name
		appex.set_widget_view(v)

if __name__ == '__main__':
	main()
