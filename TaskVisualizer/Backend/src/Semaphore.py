import numpy as np
from typing import List
from Abstracts import ITask,IActivity,IMutex,ISemaphore



class Semaphore(ISemaphore):
# Veroderung fehlt bei den Semaphoren noch!!

    def __init__(self, name, state=0) -> None:
        self._name = name
        self._state = int(state)

        self._combined = []
        self._actuators = []
        self._waiting_activities = []

    def get_name(self) -> str:
        return self._name
    

    # Which tasks have access to this mutex
    def get_actuators(self):
        return self._actuators
    
    def add_to_actuators(self, activity: IActivity):
        self._actuators.append(activity)
    
    # Which tasks have access to this mutex
    def get_waiting_activities(self):
        return self._waiting_activities
    
    def add_to_waiting_activities(self, activity: IActivity):
        self._waiting_activities.append(activity)

    def get_state(self) -> int:
        return int(self._state)
    
    def set_state(self, value) -> int:
        self._state = int(value)

    def set_combined(self, value):
        self._combined = []
        self._combined.extend(value)

    def get_combined(self):
        return self._combined    
        
    def reserve(self) -> bool:
        if self._state > 0:
            self._state -= 1
            return True
        else:
            return False

    def release(self):
        self._state += 1