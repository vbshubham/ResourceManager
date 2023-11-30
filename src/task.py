import random
from datetime import datetime, timedelta
from time import sleep


class Task:
    def __init__(self, task_id, cpu_requirement):
        self.start_time = None
        self.end_time = None
        self.task_id = task_id
        self.cpu_requirement = cpu_requirement
        self.status = 'WAITING'

    def run(self):
        self.start_time = datetime.now()
        task_execution_time = random.uniform(0.1, 1.0)
        self.status = 'RUNNING'
        # sleep(task_execution_time)
        self.end_time = datetime.now() + timedelta(seconds=task_execution_time)
        self.status = 'COMPLETED'

    def set_failed(self):
        self.status = 'FAILED'

    def __str__(self):
        return f'Task :{self.task_id}'

    def get_task_details(self):
        return (f'{str(self)} is {self.status}' +
                f' Start time = {self.start_time} End time = {self.end_time}')

