from koden.task.task import Task
from koden.task.config import Config
from koden.task.state import State
import unittest


class TestTask(unittest.TestCase):

    def test_create_task(self):
        task = Task(name="tomcat-task-1", image="tomcat")

        assert task.state == State.PENDING
        assert task.finish_time is None

    def test_config_from_task(self):
        task = Task(name="nginx-task-1", image="nginx")
        config = Config(task=task)

        assert config.name == "nginx-task-1"
        assert config.restart_policy == "always"
