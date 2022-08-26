from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from content_box import ContentBox
from header_box import HeaderBox

Builder.load_file('kv/tasket_inner_box.kv')


class TasketInnerBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HeaderBox())
        self.add_widget(ContentBox())
