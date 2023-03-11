import csv
import numpy as np
from typing import List
from Abstracts import IDiagram

class Diagram(IDiagram):
    _tasks = np.array
    _activities = np.array
    _semaphores = np.array
    _mutexes = np.array

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
    
    # möglicherweise blaupause für generate und execute_cycle functionen
    # Getter verstehe ich die Setter nicht

    def generate(self):
        #Diagramm erstellen, sollte Anfangszustand herstellen, nur einmal ausführen
        pass

    def execute_cycle(self):
        #Schleife über alle Aktivitäten, diese rufen runn auf
        pass

    def get_tasks(self):
        return self._tasks

    def get_activities(self):
        return self._activities

    def get_semaphores(self):
        return self._activities

    def get_mutexes(self):
        return self._mutexes