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
    def name(self) -> str:
        return self._name
    
    @property
    def state(self) -> int:
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value

    @property
    def actuators(self) -> List[IActivity]:
        return self._actuators
    
    @actuators.setter
    def actuators(self, value) :
        self._actuators = value
    
    @property
    def waiting_activities(self) -> List[IActivity]:
        return self._waiting_activities
    
    @waiting_activities.setter
    def waiting_activities(self, value):
        self._waiting_activities = value

    def reserve(self) -> bool:
        if self._state > 0:
            self._state -= 1
            return True
        else:
            return False

    def release(self):
        self._state += 1