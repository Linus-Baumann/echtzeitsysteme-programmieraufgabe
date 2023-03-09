# Semaphore (in out), Mutex (), Active, Duration, 

from abc import ABC, abstractmethod
import numpy as np

class Activity(ABC):
    @property
    @abstractmethod
    def active(self) -> bool:
        pass

    @property
    @abstractmethod
    def duration(self):
        pass

    @property
    @abstractmethod
    def incoming_semaphores(self) -> np.array:
        pass

    @property
    @abstractmethod
    def outgoing_semaphores(self) -> np.array:
        pass

    @property
    @abstractmethod
    def relevant_mutexes(self) -> np.array:
        pass

