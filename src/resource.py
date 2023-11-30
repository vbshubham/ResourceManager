import threading

from src.task import Task


class Resource:
    def __init__(self, resource_id, resource_type, cpu_config, price):
        self.task_history = []
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.cpu_config = cpu_config
        self.price = price
        self.is_allocated = False

    def __str__(self):
        return f'Resource {self.resource_id}'

    def allocate(self, task: Task):
        self.is_allocated = True
        self.task_history.append(task)
        print(f'{task} is allocated on {self}')

    def deallocate(self):
        self.is_allocated = False

    def execute_task(self):
        if self.task_history:
            task = self.task_history[0]

            # Using threading to run the task in a separate thread
            thread = threading.Thread(target=self._execute_task_thread, args=(task,))
            thread.start()

    def _execute_task_thread(self, task):
        try:
            task.run()
        except Exception as e:
            print(f"Task execution failed: {e}")
            task.set_failed()

        # Free up the resource after task completion
        self.deallocate()
