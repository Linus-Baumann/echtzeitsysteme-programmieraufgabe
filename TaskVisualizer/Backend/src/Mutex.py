import numpy as np
from typing import List
from Abstracts import IMutex, IActivity

class Mutex(IMutex):

    def __init__(self, name, activity_list: List[IActivity]):
        self._name = name
        self._activity_list = activity_list
        self._reserved = False

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_state(self) -> bool:
        return self._reserved

    # Which tasks have access to this semaphore
    @property
    def get_actuators(self):
        return self._activity_list

    def reserve(self):
        self._reserved = True

    def release(self):
        self._reserved = False