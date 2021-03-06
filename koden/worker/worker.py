from typing import Dict
from koden.task.state import State, state_transition_map
from koden.task.task import Task
from koden.task.config import Config
from koden.task.docker_client import DockerResult, DockerClient
from uuid import UUID
from queue import Queue
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class Worker:
    """
    Worker implementation
    Represents service running on top of the node in the cluster.
    """

    def __init__(self):
        self.queue = Queue()
        self.db: Dict[UUID, Task] = dict()
        self.task_count = 0

    def collect_stats(self):
        pass

    def add_task(self, task: Task):
        self.queue.put(task)

    def run_task(self) -> DockerResult:
        task = self.queue.get()
        if task is None:
            logger.error("No tasks in the queue")
            return DockerResult()

        if task.id in self.db.keys():
            task_persisted = self.db[task.id]
        else:
            task_persisted = None

        if task_persisted is None:
            task_persisted = task
            self.db[task.id] = task

        result = DockerResult()
        if task.state in state_transition_map[task_persisted.state]:  # validate transition
            if task.state == State.SCHEDULED:
                result = self.start_task(task)
            elif task.state == State.COMPLETED:
                result = self.stop_task(task)
            else:
                result.error = f"Undefined state for task {task.id}"
        else:
            result.error = f"Invalid transition from {task_persisted.state} to {task.state}"

        return result

    def start_task(self, task: Task) -> DockerResult:
        config = Config(task=task)
        d = DockerClient(task_config=config)

        result = d.run()
        if result.error is not None:
            logger.error(f"Error starting task {task.id} with error {result.error}")
            task.state = State.FAILED
            self.db[task.id] = task
            return result

        task.container_id = result.container_id
        task.state = State.RUNNING
        self.db[task.id] = task

        return result

    def stop_task(self, task: Task) -> DockerResult:
        config = Config(task=task)
        d = DockerClient(task_config=config)

        result = d.stop(task.container_id)
        if result.error is not None:
            logger.error(f"Error stopping container {task.container_id} with error {result.error}")
            task.state = State.FAILED
            self.db[task.id] = task
            return result

        task.finish_time = datetime.now()
        task.state = State.COMPLETED
        self.db[task.id] = task
        logger.info(f"Stopped and removed container {task.container_id} for task {task.id}")

        return result