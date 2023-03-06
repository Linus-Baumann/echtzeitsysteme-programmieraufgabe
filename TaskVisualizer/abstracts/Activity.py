# Semaphore (in out), Mutex (), Active, Duration, 

from abc import ABC, abstractmethod
import numpy as np

class Activity(ABC):
    @property
    @abstractmethod
    def active(self):
        pass

    @property
    @abstractmethod
    def duration(self):
        pass

