import csv
import numpy as np
from typing import List
from abstracts.IDiagram import IDiagram

class Diagram(IDiagram):
    def __init__(self):
        self._tasks = np.array
        self._activities = np.array
        self._semaphores = np.array
        self._mutexes = np.array

    def parse(seld, rows):
        for object in rows:
            if object[0] == "Task":
                print("lol")
            elif object[0] == "Activity":
                pass
            elif object[0] == "Semaphore":
                pass
            elif object[0] == "Mutex":
                pass