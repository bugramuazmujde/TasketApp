from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from content_inner_box import ContentInnerBox
from status_bar import StatusBar

Builder.load_file('kv/content_box.kv')


class ContentBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StatusBar())
        self.add_widget(ContentInnerBox())
