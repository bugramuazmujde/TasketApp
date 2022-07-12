from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_file('kv/tasket_label.kv')


class TasketLabel(Label):
    def __init__(self, label_text, **kwargs):
        super().__init__(**kwargs)
        self.text = label_text
