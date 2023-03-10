# Dazugehörige Aktivitäten, 

from abc import ABC, abstractmethod
from Activity import Activity
import numpy as np

class Task(ABC):
    @property
    @abstractmethod
    def activities(self) -> np.array[Activity]:
        pass

