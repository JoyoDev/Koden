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

    def __init__(self, name: str, image: str, cpu=0.0, memory=0, disk=0, restart_policy="always"):
        self.id = uuid4()
        self.container_id = ""
        self.name = name
        self.state = State.PENDING
        self.image = image
        self.cpu: float = cpu
        self.memory = memory
        self.disk = disk
        self.exposed_ports: PortSet = dict()
        self.port_bindings: Dict[str, str] = dict()
        self.restart_policy = restart_policy
        self.start_time = datetime.now()
        self.finish_time = None
