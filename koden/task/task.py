from typing import Dict
from datetime import datetime
from uuid import uuid4
from koden.task.state import State
from koden.connection.nat import PortSet


class Task:
    """
    Task implementation
    Unit of work that executes specified image.
    """

    def __init__(self, name: str, image: str, memory: int, disk: int, restart_policy: str):
        self.id = uuid4()
        self.name = name
        self.state = State.PENDING
        self.image = image
        self.memory = memory
        self.disk = disk
        self.exposed_ports: PortSet = PortSet()
        self.port_bindings: Dict[str, str] = dict()
        self.restart_policy = restart_policy
        self.start_time = datetime.now()
        self.finish_time = None
