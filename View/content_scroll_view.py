from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from View.task_bucket import TaskBucket


class ContentScrollView(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_bucket = TaskBucket()
        self.task_bucket.bind(minimum_height=self.task_bucket.setter('height'))
        self.add_widget(self.task_bucket)

