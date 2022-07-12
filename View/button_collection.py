from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.tasket_button import TasketButton

Builder.load_file('kv/button_collection.kv')


class ButtonCollection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_button = TasketButton("add")
        self.add_button.bind(on_press=self.add_text_input_to_status_to_do)

        self.add_widget(self.add_button)
        self.add_widget(TasketButton("edit"))
        self.add_widget(TasketButton("minus"))

    def add_text_input_to_status_to_do(self, value):
        self.parent.parent.children[0].children[0].create_task()
