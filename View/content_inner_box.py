from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from scroll_view_parent_grid import ScrollViewParentGrid
from task_input_box import TaskInputBox

Builder.load_file('kv/content_inner_box.kv')


class ContentInnerBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.to_do_bucket = ScrollViewParentGrid()
        self.in_progress_bucket = ScrollViewParentGrid()
        self.completed_bucket = ScrollViewParentGrid()

        self.add_widget(self.to_do_bucket)
        self.add_widget(self.in_progress_bucket)
        self.add_widget(self.completed_bucket)

    def input_a_task(self):
        self.to_do_bucket.children[0].children[0].add_widget(
            TaskInputBox(),
            index=len(self.to_do_bucket.children[0].children[0].children)
        )

    def create_task(self, task_text):
        self.to_do_bucket.children[0].children[0].add_widget(Label(text=task_text))
        print(self.to_do_bucket.children[0].children[0].children)
