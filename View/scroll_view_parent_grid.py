from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from View.content_scroll_view import ContentScrollView

Builder.load_file('kv/scroll_view_parent_grid.kv')


class ScrollViewParentGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ContentScrollView())
