import random
from datetime import datetime, timedelta
from time import sleep


class Resource:
    def __init__(self, resource_id, resource_type, cpu_config, price):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.cpu_config = cpu_config
        self.price = price
        self.is_allocated = False
        self.task_id = None
        self.start_time = None
        self.end_time = None

    def allocate(self, task_id):
        self.is_allocated = True
        self.task_id = task_id
        self.start_time = datetime.now()

    def deallocate(self):
        self.is_allocated = False
        self.task_id = None
        self.start_time = None
        self.end_time = datetime.now()

    def execute_task(self):
        # Simulating task execution time
        task_execution_time = random.uniform(0.1, 1.0)
        sleep(task_execution_time)
        self.end_time = datetime.now() + timedelta(seconds=task_execution_time)
        print(f"Task {self.task_id} executed on Resource {self.resource_id}")
        # Free up the resource after task completion
        self.deallocate()
