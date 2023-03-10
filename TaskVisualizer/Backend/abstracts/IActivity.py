# Semaphore (in out), Mutex (), Active, Duration, 

from abc import ABC, abstractmethod
from ISemaphore import ISemaphore
from IMutex import IMutex
import numpy as np

class IActivity(ABC):
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
    def incoming_semaphores(self) -> np.array[ISemaphore]:
        pass

    @property
    @abstractmethod
    def outgoing_semaphores(self) -> np.array[ISemaphore]:
        pass

    @property
    @abstractmethod
    def relevant_mutexes(self) -> np.array[IMutex]:
        pass

    @abstractmethod
    def run(self):
        pass
