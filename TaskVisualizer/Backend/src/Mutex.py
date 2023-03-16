import numpy as np
from typing import List
from Abstracts import IMutex, IActivity

class Mutex(IMutex):

    def __init__(self, name):
        self._name = name
        self._activity_list: List[IActivity]
        self._reserved = False

    def get_name(self) -> str:
        return self._name

    def get_state(self) -> bool:
        return self._reserved

    # Which tasks have access to this mutex
    def get_actuators(self):
        return self._activity_list
    
    def set_actuators(self, activity_list: List[IActivity]):
        self._activity_list = activity_list

    def reserve(self):
        self._reserved = True

    def release(self):
        self._reserved = False