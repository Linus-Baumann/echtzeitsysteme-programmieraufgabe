import numpy as np
from typing import List
from Abstracts import ITask, IActivity

class Task(ITask):
    def __init__(self, name, activity_list: List[IActivity]):
        self._name = name
        self._activities = activity_list

    def get_name(self) -> str:
        return self._name
    
    def get_activities(self) -> List[IActivity]:
        return self._activities