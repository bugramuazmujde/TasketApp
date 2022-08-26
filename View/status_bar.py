from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from tasket_label import TasketLabel

Builder.load_file('kv/status_bar.kv')


class StatusBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for label in ["TODO", "IN PROGRESS", "COMPLETED"]:
            self.add_widget(TasketLabel(label))
