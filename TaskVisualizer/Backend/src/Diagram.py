import csv
import numpy as np
from typing import List
from Abstracts import IDiagram

class Diagram(IDiagram):
# Müssen wir hier nicht die Variablen (Arrays) erstellen, nicht im Constructor da wir sie 
# dort doch noch gar nicht kennen???
    
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