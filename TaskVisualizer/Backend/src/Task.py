import numpy as np
from typing import List
from Abstracts import ITask, IActivity

class Task(ITask):
    _name = ""
    _activities = np.array   

    def __init__(self, task_name, activity_list: List[IActivity]):
        self._name = task_name
        self._activities = activity_list #Kein plan ob das geht wegen List -> Array

    @property
    def get_activities(self):
        return self._activities