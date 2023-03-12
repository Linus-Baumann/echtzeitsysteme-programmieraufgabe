import numpy as np
from typing import List
from Abstracts import IMutex

class Mutex(IMutex):
    _activity_list = np.array
    _reserved = False

    def __init__(self, activity_list: np.array):
        self._activity_list = activity_list


    def get_state(self) -> bool:
        return self._reserved

    # Which tasks have access to this semaphore
    def get_actuators(self):
        return self._activity_list

    def reserve(self):
        _reserved = True

    def release(self):
        _reserved = False