# Dazugehörige Aktivitäten, 

from abc import ABC, abstractmethod
from IActivity import IActivity
import numpy as np

class ITask(ABC):
    @property
    @abstractmethod
    def activities(self) -> np.array[IActivity]:
        pass

