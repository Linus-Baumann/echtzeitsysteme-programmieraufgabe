# init mit Zahl und Actuators
# -- wenn activity gestartet
# ++ wenn activity fertig
from abc import ABC, abstractmethod
import numpy as np

class Activity(ABC):
    # The state in which this semaphore is eg. 2
    @property
    @abstractmethod
    def state(self):
        pass

    # Which tasks have access to this semaphore
    @property
    @abstractmethod
    def actuators(self):
        pass

    @abstractmethod
    def reserve(self):
        pass

    @abstractmethod
    def release(self):
        pass