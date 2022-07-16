from typing import List


class Config:
    """
    Configuration for Tasks's containers
    """

    def __init__(self, name: str, image: str, restart_policy: str, attach_stdin: bool = True,
                 attach_stdout: bool = True, attach_stderr: bool = True, cmd: List[str] = [], memory: int = 0,
                 disk: int = 0, env: List[str] = []):
        self.name = name
        self.image = image
        self.restart_policy = restart_policy
        self.attach_stdin = attach_stdin
        self.attach_stdout = attach_stdout
        self.attach_stderr = attach_stderr
        self.cmd = cmd
        self.memory = memory
        self.disk = disk
        self.env = env
