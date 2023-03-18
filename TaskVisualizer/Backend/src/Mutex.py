import numpy as np
from typing import List
from Abstracts import IMutex, IActivity

class Mutex(IMutex):

    def __init__(self, name):
        self._name = name
        self._activity_list = []
        self._reserved = False

    def get_name(self) -> str:
        return self._name

    def get_state(self) -> bool:
        return self._reserved

    # Which tasks have access to this mutex
    def get_activity_list(self):
        return self._activity_list
    
    def add_to_activity_list(self, activity: IActivity):
        self._activity_list.append(activity)

    def reserve(self) -> bool:
        if self._reserved:
            return False
        else:
            self._reserved = True
            return True

    def release(self) -> bool:
        if not self._reserved:
            return False
        else:
            self._reserved = False
            return True