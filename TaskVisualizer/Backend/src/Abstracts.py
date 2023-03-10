from abc import ABC, abstractmethod
import numpy as np

class ITask(ABC):
    @property
    @abstractmethod
    def activities(self) -> 'np.array[IActivity]':
        pass

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
    def incoming_semaphores(self) -> 'np.array[ISemaphore]':
        pass

    @property
    @abstractmethod
    def outgoing_semaphores(self) -> 'np.array[ISemaphore]':
        pass

    @property
    @abstractmethod
    def relevant_mutexes(self) -> 'np.array[IMutex]':
        pass

    @abstractmethod
    def run(self):
        pass

class ISemaphore(ABC):
    # The state in which this semaphore is eg. 2
    @property
    @abstractmethod
    def state(self):
        pass

    # Which tasks have access to this semaphore
    @property
    @abstractmethod
    def actuators(self) -> np.array[IActivity]:
        pass

    @abstractmethod
    def reserve(self):
        pass

    @abstractmethod
    def release(self):
        pass

class IMutex(ABC):
    # The state in which this mutex is eg. True
    @property
    @abstractmethod
    def state(self) -> bool:
        pass

    @property
    @abstractmethod
    def get_state(self) -> bool:
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

class ICSVOperator(ABC):
    @abstractmethod
    def open(self, csv_filename):
        pass

    @abstractmethod
    def parse(self, rows):
        pass

class IDiagram(ABC):
    @property
    @abstractmethod
    def mutexes(self) -> np.array[IMutex]:
        pass

    @property
    @abstractmethod
    def semaphores(self) -> np.array[ISemaphore]:
        pass

    @property
    @abstractmethod
    def activities(self) -> np.array[IActivity]:
        pass

    @property
    @abstractmethod
    def tasks(self) -> np.array[ITask]:
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def execute_cycle(self):
        pass