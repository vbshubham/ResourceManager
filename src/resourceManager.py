import time
from typing import Optional

from src.resource import Resource


class ResourceManager:
    def __init__(self):
        self.is_running = False
        self.resources = []
        self.task_queue = []

    def add_resource(self, res):
        self.resources.append(res)

    def delete_resource(self, resource_id):
        self.resources = [res for res in self.resources if res.resource_id != resource_id]

    def get_available_resources(self, resource_type, min_cpu_config):
        return [res for res in self.resources if res.resource_type == resource_type
                and res.cpu_config >= min_cpu_config and not res.is_allocated]

    def get_allocated_resources(self, resource_type):
        return [res for res in self.resources if res.resource_type == resource_type and res.is_allocated]

    def allocate_resource(self, task, allocation_criteria):
        print(f'Trying to allocate {task} using {allocation_criteria}')
        resource: Optional[Resource] = None
        available_resources = self.get_available_resources(task.cpu_requirement[0], task.cpu_requirement[1])

        if not available_resources:
            print(f"No resource available. {task} is waiting for resources.")
            self.task_queue.append((task, allocation_criteria))
            return

        if allocation_criteria == "price":
            resource = min(available_resources, key=lambda x: x.price)
        elif allocation_criteria == "execution_time":
            resource = min(available_resources, key=lambda x: x.cpu_config)

        resource.allocate(task)
        resource.execute_task()

    def check_task_status(self, task_id: int) -> str:
        for resource in self.resources:
            for task in resource.task_history:
                if task.task_id == task_id:
                    return task.get_task_details()

        for queued_task, allocation_criteria in self.task_queue:
            if queued_task.task_id == task_id:
                return f"Task {task_id} is waiting for resources with allocation criteria {allocation_criteria}."

        return f"Task {task_id} not found."

    def process_waiting_tasks(self):
        while self.task_queue:
            task, allocation_criteria = self.task_queue.pop(0)
            self.allocate_resource(task, allocation_criteria)

    def start_manager(self, interval=1):
        self.is_running = True
        while self.is_running:
            self.process_waiting_tasks()
            time.sleep(interval)

    def stop_manager(self):
        self.is_running = False
