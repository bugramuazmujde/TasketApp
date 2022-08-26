from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from button_collection import ButtonCollection

Builder.load_file('kv/header_box.kv')


class HeaderBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="", size_hint_x=.6))
        self.add_widget(Label(text="TASKET", color="#000000"))
        self.add_widget(Label(text="", size_hint_x=.2))
        self.add_widget(ButtonCollection())
