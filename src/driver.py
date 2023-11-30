import random
import time
from threading import Thread

from src.resourceManager import ResourceManager
from src.resource import Resource
from src.task import Task

if __name__ == "__main__":
    resource_manager = ResourceManager()

    # Adding resources
    resource_manager.add_resource(Resource(1, "SERVER_INSTANCE", 8, 100))
    resource_manager.add_resource(Resource(2, "SERVER_INSTANCE", 16, 150))
    resource_manager.add_resource(Resource(3, "SERVER_INSTANCE", 8, 120))
    resource_manager.add_resource(Resource(4, "SERVER_INSTANCE", 8, 120))
    resource_manager.add_resource(Resource(5, "SERVER_INSTANCE", 16, 120))

    # Start the resource manager in a separate thread
    manager_thread = Thread(target=resource_manager.start_manager, args=(5,), daemon=True)
    manager_thread.start()

    # Simulating task generation
    for task_id in range(1, 11):
        cpu_requirement = ("SERVER_INSTANCE", random.choice([8, 16]))
        task = Task(task_id, cpu_requirement)

        # Randomly choosing allocation criteria
        allocation_criteria = random.choice(["price", "execution_time"])

        resource_manager.allocate_resource(task, allocation_criteria)

        # Simulating time between task submissions
        time.sleep(random.uniform(0.1, 1.0))

    # Stop the resource manager after some time
    time.sleep(20)
    resource_manager.stop_manager()
    manager_thread.join()

    # Checking task status
    for task_id in range(1, 11):
        print(resource_manager.check_task_status(task_id))
