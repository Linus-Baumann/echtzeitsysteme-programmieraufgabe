# Dazugehörige Aktivitäten, 

from abc import ABC, abstractmethod
import numpy as np

class Task(ABC):
    @abstractmethod
    def run(self):
        pass