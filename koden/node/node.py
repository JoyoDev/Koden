class Node:
    """
    Represents physical machine where worker runs
    """
    def __init__(self, name: str, ip: str, cores: int, memory: int, disk: int):
        self.name = name
        self.ip = ip
        self.cores = cores
        self.memory = memory
        self.memory_allocated = 0
        self.disk = disk
        self.disk_allocated = 0
        self.task_count = 0
