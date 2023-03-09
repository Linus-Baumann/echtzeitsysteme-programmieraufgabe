# Verbundene Activitäten, Festgelegter zustand False, 
# init mit Actuators
# -- wenn activity gestartet
# ++ wenn activity fertig
from abc import ABC, abstractmethod
import numpy as np

class Mutex(ABC):
    # The state in which this mutex is eg. True
    @property
    @abstractmethod
    def reserved(self) -> bool:
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