from koden.task.task import Task


class Config:
    """
    Configuration for Tasks's containers
    """

    def __init__(self, task: Task, attach_stdin=True, attach_stdout=True, attach_stderr=True, cmd=[], env=[]):
        self.name = task.name
        self.image = task.image
        self.attach_stdin = attach_stdin
        self.attach_stdout = attach_stdout
        self.attach_stderr = attach_stderr
        self.exposed_ports = task.exposed_ports
        self.cmd = cmd
        self.cpu = task.cpu
        self.memory = task.memory
        self.disk = task.disk
        self.env = env
        self.restart_policy = task.restart_policy
