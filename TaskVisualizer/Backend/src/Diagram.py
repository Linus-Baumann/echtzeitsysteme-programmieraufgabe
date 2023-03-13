import csv
from typing import List
from Abstracts import IDiagram, ITask, IActivity, ISemaphore, IMutex
from Semaphore import Semaphore
from Mutex import Mutex
from Task import Task
from Activity import Activity

class Diagram(IDiagram):
    def __init__(self):
        self._tasks = []
        self._activities = []
        self._semaphores = []
        self._mutexes = []

    def check_file_structure(self, rows):
        return

# rows from FileReader
    def parse(self, rows):
        self.check_file_structure(rows)
        for object in rows:
            if object[0] == "Task":  
                connected_semaphores = self.find_semaphores(object[2])
                self._tasks.append(Task(object[1], connected_semaphores))
                print("Task created")
            elif object[0] == "Activity":
                incoming_semaphores = self.find_semaphores(object[3])
                outgoing_semaphores = self.find_semaphores(object[4])
                self._activities.append(Activity(object[1], object[2], incoming_semaphores, outgoing_semaphores))
            elif object[0] == "Semaphore":
                self._semaphores.append(Semaphore(object[1].strip(), object[2].strip()))
            elif object[0] == "Mutex":
                #needs correction
                #Hier muss mutex hin und es muss beliebig viele Eingaben annehmen können -> vll array
                connected_semaphores = self.find_semaphores(object[1])
                self._mutexes.append(Mutex(connected_semaphores))

    def find_semaphores(self, semaphores) -> List[ISemaphore]:
        found_semaphores = []
        for semaphore in semaphores.split(";"):
            if semaphore.count(":") > 0:
                found_semaphore_relation = []
                # Do something if argument is a numpy array
                for related_semaphore in semaphore.split(":"):
                    found_semaphore_relation.append(self.find_in_array(self._semaphores, related_semaphore.strip()))
                found_semaphores.append(found_semaphore_relation)
            else:
                # Do something if argument is a string
                found_semaphores.append(self.find_in_array(self._semaphores, semaphore))
        return found_semaphores

    def find_in_array(self, array, name):
        return [element for element in array if element._name == name.strip()]


    def generate(self):
        #Diagramm erstellen, sollte Anfangszustand herstellen, nur einmal ausführen
        pass

    def execute_cycle(self):
        #Schleife über alle Aktivitäten, diese rufen runn auf
        pass

    def get_tasks(self) -> List[ITask]:
        return self._tasks

    def get_activities(self) -> List[IActivity]:
        return self._activities

    def get_semaphores(self) -> List[ISemaphore]:
        return self._activities

    def get_mutexes(self) -> List[IMutex]:
        return self._mutexes