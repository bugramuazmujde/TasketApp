import csv
from csv import DictReader
from os.path import exists


class TaskService:
    def __init__(self, task_id, task_name, task_status):
        self.name = task_name
        self.id = task_id
        self.status = task_status
        if not exists("../Service/tasks.csv"):
            self.create_tasks_csv()
            self.append_task_to_csv()
        else:
            self.append_task_to_csv()

    def create_tasks_csv(self):
        header = ["name", "id", "status"]
        self.write_to_csv(header)

    def append_task_to_csv(self):
        data = [self.name, self.id, self.status.value]
        self.write_to_csv(data)

    @staticmethod
    def write_to_csv(data):
        with open('../Service/tasks.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    @staticmethod
    def read_tasks_from_csv():
        if not exists("../Service/tasks.csv"):
            return {}
        else:
            file_handle = open('../Service/tasks.csv', 'r', encoding="utf8")
            return DictReader(file_handle)
