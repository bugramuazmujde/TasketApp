from kivy.uix.textinput import TextInput


class TaskInputBox(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (60, 60)
        self.size_hint = (1, None)
        self.text = ""
        self.multiline = False
        self.bind(on_text_validate=self.on_enter)

    def on_enter(self, value):
        print("yeraba")