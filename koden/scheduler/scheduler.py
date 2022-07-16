from abc import ABC, abstractmethod


class Scheduler(ABC):
    """
    Scheduler abstract class
    Tracks state of each worker, and picks the most suitable one for task scheduling.
    """

    @abstractmethod
    def select_candidate_nodes(self):
        pass

    @abstractmethod
    def score(self):
        pass

    @abstractmethod
    def pick(self):
        pass
