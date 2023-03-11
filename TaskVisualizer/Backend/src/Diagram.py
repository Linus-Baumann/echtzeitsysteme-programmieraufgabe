import csv
import numpy as np
from typing import List
from Abstracts import IDiagram

class Diagram(IDiagram):

    def __init__(self):
        self._tasks = np.array
        self._activities = np.array
        self._semaphores = np.array
        self._mutexes = np.array

# rows from FileReader
    def parse(self, rows):
        for object in rows:
            if object[0] == "Task":
                print("lol")
            elif object[0] == "Activity":
                pass
            elif object[0] == "Semaphore":
                pass
            elif object[0] == "Mutex":
                pass
    
    # Simon getter und setter für die arrays und möglicherweise blaupause für generate und execute_cycle functionen