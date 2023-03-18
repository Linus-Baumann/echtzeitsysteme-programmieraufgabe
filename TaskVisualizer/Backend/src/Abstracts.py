from abc import ABC, abstractmethod
import numpy as np
from typing import List

class ITask(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_activities(self) -> 'List[IActivity]':
        pass

class IActivity(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_task(self):
        pass

    @abstractmethod
    def get_active(self) -> bool:
        pass

    @abstractmethod
    def get_duration(self):
        pass
    
    @abstractmethod
    def get_incoming_semaphores(self) -> 'List[ISemaphore]':
        pass
    
    @abstractmethod
    def get_outgoing_semaphores(self) -> 'List[ISemaphore]':
        pass

    @abstractmethod
    def get_relevant_mutexes(self) -> 'List[IMutex]':
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def finish(self):
        pass

class ISemaphore(ABC):
    # The name of this semaphore eg. "1"
    @abstractmethod
    def get_name(self) -> str:
        pass

    # The state in which this semaphore is eg. 2
    @abstractmethod
    def get_state(self):
        pass

    # The state in which this semaphore is eg. 2
    @abstractmethod
    def set_state(self):
        pass

    # Which tasks have access to this semaphore
    @abstractmethod
    def get_actuators(self):
        pass

    @abstractmethod
    def add_to_actuators(self, activity: IActivity):
        pass

    # Which tasks are waiting for the semaphore to be released
    @abstractmethod
    def get_waiting_activities(self):
        pass

    @abstractmethod
    def add_to_waiting_activities(self, activity: IActivity):
        pass

    @abstractmethod
    def reserve(self) -> bool:
        pass

    @abstractmethod
    def release(self):
        pass

class IMutex(ABC):
    # The name of this mutex
    @abstractmethod
    def get_name(self) -> str:
        pass

    # The state in which this mutex is (eg. True)
    @abstractmethod
    def get_state(self) -> bool:
        pass

    # Which tasks have access to this mutex
    @abstractmethod
    def get_activity_list(self):
        pass

    @abstractmethod
    def add_to_activity_list(self, activity: IActivity):
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