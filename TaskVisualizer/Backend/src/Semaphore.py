import numpy as np
from typing import List
from Abstracts import ITask,IActivity,IMutex,ISemaphore



class Semaphore(ISemaphore):
# Veroderung fehlt bei den Semaphoren noch!!

    def __init__(self, name, state=0) -> None:
        self._name = name
        self._state = state

        self._actuators = []
        self._waiting_activities = []

    @property
    def get_name(self) -> str:
        return self._name
    

    # Which tasks have access to this mutex
    def get_actuators(self):
        return self._activity_list
    
    def set_actuators(self, activity_list: List[IActivity]):
        self._activity_list = activity_list
    
    # Which tasks have access to this mutex
    def get_waiting_activities(self):
        return self._waiting_activities
    
    def set_waiting_activities(self, waiting_activities: List[IActivity]):
        self._waiting_activities = waiting_activities

    def get_state(self) -> int:
        return self._state
    
    def set_state(self, value) -> int:
        self._state = value
        
    def reserve(self) -> bool:
        if self._state > 0:
            self._state -= 1
            return True
        else:
            return False

    def release(self):
        self._state += 1