from Model.status import Status


class Task:
    def __init__(self, task_id, name, status=Status.to_do):
        self.id = task_id
        self.name = name
        self.status = status
