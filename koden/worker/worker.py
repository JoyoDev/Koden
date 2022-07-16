from typing import Dict
from koden.task.task import Task
from uuid import UUID
from queue import Queue


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

    def run_task(self):
        pass

    def start_task(self):
        pass

    def stop_task(self):
        pass
