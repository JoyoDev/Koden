from datetime import datetime
from uuid import uuid4
from koden.task.task import Task


class TaskEvent:
    """
    Task Event implementation
    Internal process that triggers change of Task's state
    """

    def __init__(self, task: Task):
        self.id = uuid4()
        self.timestamp = datetime.now()
        self.task = task
