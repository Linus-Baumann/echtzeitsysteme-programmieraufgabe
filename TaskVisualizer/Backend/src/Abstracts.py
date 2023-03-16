from abc import ABC, abstractmethod
import numpy as np
from typing import List

class ITask(ABC):
    @property
    @abstractmethod
    def get_activities(self) -> 'List[IActivity]':
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
    def incoming_semaphores(self) -> 'List[ISemaphore]':
        pass

    @property
    @abstractmethod
    def outgoing_semaphores(self) -> 'List[ISemaphore]':
        pass

    @property
    @abstractmethod
    def relevant_mutexes(self) -> 'List[IMutex]':
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
    def actuators(self) -> List[IActivity]:
        pass

    # Which tasks are waiting for the semaphore to be released
    @property
    @abstractmethod
    def waiting_activities(self) -> List[IActivity]:
        pass

    @abstractmethod
    def reserve(self) -> bool:
        pass

    @abstractmethod
    def release(self):
        pass

class IMutex(ABC):
    # The state in which this mutex is (eg. True)
    @property
    @abstractmethod
    def reserved(self) -> bool:
        pass

    @abstractmethod
    def get_state(self) -> bool:
        pass

    # Which tasks have access to this semaphore
    @abstractmethod
    def get_actuators(self):
        pass

    @abstractmethod
    def reserve(self):
        pass

    @abstractmethod
    def release(self):
        pass

class IFileReader(ABC):
    @abstractmethod
    def open(self, csv_filename):
        pass

class IDiagram(ABC):
    @abstractmethod
    def get_mutexes(self) -> List[IMutex]:
        pass

    @abstractmethod
    def get_semaphores(self) -> List[ISemaphore]:
        pass

    @abstractmethod
    def get_activities(self) -> List[IActivity]:
        pass

    @abstractmethod
    def get_tasks(self) -> List[ITask]:
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def execute_cycle(self):
        pass