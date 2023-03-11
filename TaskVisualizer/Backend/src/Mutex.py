import numpy as np
from typing import List
from Abstracts import IMutex

class Mutex(IMutex):
# Liste von Aktivitäten?
    _activity_list = np.array
    _reserved = False

    def __init__(self, activity_list: np.array):
        self._activity_list = activity_list

    #Simon getter und setter für reserved und get_state und actuaters und die functions reserve und release
