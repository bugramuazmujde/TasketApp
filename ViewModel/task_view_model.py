from Model.status import Status
from Model.task import Task
from Service.task_service import TaskService
from Service.utid_service import UTIDService


class TaskViewModel:
    def __init__(self):
        self.__tasks = []
        self.feed_tasks()

    def create_task(self, task_name):
        task = Task(UTIDService().utid, task_name)
        self.__tasks.append(task)
        TaskService(task.id, task.name, task.status)

    def get_tasks(self):
        return self.__tasks

    def feed_tasks(self):
        for task in TaskService.read_tasks_from_csv():
            self.__tasks.append(Task(task['id'], task['name'], Status(value=task['status'])))


