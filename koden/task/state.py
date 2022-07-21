from enum import Enum
from typing import Dict, List


class State(Enum):
    """
    List of possible states for a Task
    """
    PENDING = 0
    SCHEDULED = 1
    COMPLETED = 2
    RUNNING = 3
    FAILED = 4


# all possible transitions from one state to others
state_transition_map: Dict[State, List[State]] = {
    State.PENDING: [State.SCHEDULED],
    State.SCHEDULED: [State.SCHEDULED, State.RUNNING, State.FAILED],
    State.RUNNING: [State.RUNNING, State.COMPLETED, State.FAILED],
    State.COMPLETED: [],
    State.FAILED: []
}
