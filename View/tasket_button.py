from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('kv/tasket_button.kv')


class TasketButton(Button):
    def __init__(self, button_name, **kwargs):
        super().__init__(**kwargs)
        self.ids.image_icon.source = '../img/'+button_name+'-icon.png'
