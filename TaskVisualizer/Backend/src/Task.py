import numpy as np
from typing import List
from Abstracts import ITask

class Task(ITask):
    _name = ""
    _activities = np.array   

    def __init__(self, task_name):
        self._name = task_name

    @property
    def get_activities(self):
        return self._activities