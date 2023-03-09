from abc import ABC, abstractmethod
from Activity import Activity
from Task import Task
from Semaphore import Semaphore
from Mutex import Mutex
import numpy as np

class Task(ABC):
    @property
    @abstractmethod
    def mutexes(self) -> np.array[Mutex]:
        pass

    @property
    @abstractmethod
    def semaphores(self) -> np.array[Semaphore]:
        pass

    @property
    @abstractmethod
    def activities(self) -> np.array[Activity]:
        pass

    @property
    @abstractmethod
    def tasks(self) -> np.array[Task]:
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def execute_cycle(self):
        pass