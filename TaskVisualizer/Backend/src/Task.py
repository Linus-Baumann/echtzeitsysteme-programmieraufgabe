import numpy as np
from typing import List
from Abstracts import ITask, IActivity

class Task(ITask):
    def __init__(self, name, activity_list: List[IActivity]):
        self._name = name
        self._activities = activity_list #Kein plan ob das geht wegen List -> Array

    @property
    def get_activities(self):
        return self._activities