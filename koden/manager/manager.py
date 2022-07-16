from typing import Dict, List
from uuid import UUID
from koden.task.task import Task
from koden.task.task_event import TaskEvent
from koden.worker.worker import Worker
import queue


class Manager:
    """
    Control Plane implementation
    Manages cluster state - accepts requests, schedules tasks and keeps track of the entire workload.
    """

    def __init__(self):
        self.pending: queue.Queue = queue.Queue()
        self.task_db: Dict[str, Task] = dict()
        self.task_event_db: Dict[str, TaskEvent] = dict()
        workers: List[Worker] = []
        worker_task_map: Dict[str, List[UUID]] = dict()
        task_worker_map: Dict[UUID, str] = dict()

    def select_worker(self):
        pass

    def update_tasks(self):
        pass

    def send_work(self):
        pass
