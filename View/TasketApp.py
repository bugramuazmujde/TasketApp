from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from View.tasket_inner_box import TasketInnerBox

Builder.load_file('kv/tasket.kv')

TITLE = 'Tasket'
Config.set('graphics', 'resizable', '0')
Window.size = (1000, 800)
Window.minimum_width, Window.minimum_height = Window.size


class Tasket(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TasketInnerBox())


class TasketApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Tasket()


if __name__ == "__main__":
    TasketApp().run()
