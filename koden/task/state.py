from enum import Enum


class State(Enum):
    """
    List of possible states for a Task
    """
    PENDING = 0
    SCHEDULED = 1
    COMPLETED = 2
    RUNNING = 3
    FAILED = 4
