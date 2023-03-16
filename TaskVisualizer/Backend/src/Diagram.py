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

    def check_file_structure(self, rows: List[List[str]]) -> bool:
        print("Checking structure...")
        allowed_items = ["Semaphore", "Mutex", "Activity", "Task"]
        scanned_items = []
        current_index = 0
        for row in rows:
            try:
                row[0].strip()
                if row[0] != allowed_items[current_index]:
                    current_index += 1
                if row[0] not in scanned_items:
                    scanned_items.append(row[0])
                if current_index > 3:
                    print("ERROR: Wrong file structure. Check if the file lists the Semaphores, Activities, Mutexes and Tasks in the correct order. Other items are not allowed.")
                    return False
            except IndexError:
                rows.remove(row)
                print("Empty Line (IndexError) resolved by deletion: " + str(row))
        if scanned_items != allowed_items:
            print("ERROR: Wrong file structure. Check if the file lists the Semaphores, Activities, Mutexes and Tasks in the correct order. Other items are not allowed.")
            return False
        print("Structure is correct.")
        return True

# rows from FileReader
    def parse(self, rows):
        self.data_restructuring(rows)
        if not self.check_file_structure(rows):
            return False
        for object in rows:
            if object[0] == "Task":  
                included_activities = self.find_activities(object[2])
                self._tasks.append(Task(object[1], included_activities))
                print("Task created")
            elif object[0] == "Activity":
                incoming_semaphores = self.find_semaphores(object[3])
                outgoing_semaphores = self.find_semaphores(object[4])
                relevant_mutexes = self.find_mutexes(object[5])
                self._activities.append(Activity(object[1], object[2], incoming_semaphores, outgoing_semaphores, relevant_mutexes))
                print("Activity created")
            elif object[0] == "Semaphore":
                self._semaphores.append(Semaphore(object[1].strip(), object[2].strip()))
                print("Semaphore created")
            elif object[0] == "Mutex":
                self._mutexes.append(Mutex(object[1]))
                print("Mutex created")
        self.fill_objects(self._mutexes)
        self.fill_objects(self._semaphores)
        return True
    
    def fill_objects(self, objects: List):
        for object in objects:
            for activity in self._activities:
                if isinstance(object, IMutex):
                    # Check if the activity has the mutex in its relevant mutexes and check if the mutex is not empty
                    relevant_mutexes = [mutex for mutex in activity.get_relevant_mutexes() if mutex]
                    if not relevant_mutexes:
                        continue

                    activity_list = [mutex[0] for mutex in relevant_mutexes if mutex[0].get_name() == object.get_name()]
                    if activity_list:
                        object.add_to_activity_list(activity_list)
                if isinstance(object, ISemaphore):
                    return
#                    incoming_semaphores = [mutex for mutex in activity.get_incoming_semaphores() if mutex]
#                    outgoing_semaphores = [mutex for mutex in activity.get_relevant_mutexes() if mutex]
#                    if not (incoming_semaphores or outgoing_semaphores):
#                        continue
#                    actuator_list = [semaphore[0] for semaphore in outgoing_semaphores if semaphore[0].get_name() == object.get_name()]
#                    waiting_list = [semaphore[0] for semaphore in incoming_semaphores if semaphore[0].get_name() == object.get_name()]
#                    if actuator_list:
#                        object.add_to_actuator_list(actuator_list)
#                    if waiting_list:
#                        object.add_to_waiting_list(waiting_list)


    def find_semaphores(self, semaphores) -> List[ISemaphore]:
        found_semaphores = []
        for semaphore in semaphores.split(";"):
            if semaphore.count(":") > 0:
                found_semaphore_relation = []
                # Do something if argument is a list
                for related_semaphore in semaphore.split(":"):
                    found_semaphore_relation.append(self.find_in_array(self._semaphores, related_semaphore.strip()))
                found_semaphores.append(found_semaphore_relation)
            else:
                # Do something if argument is a string
                found_semaphores.append(self.find_in_array(self._semaphores, semaphore))
        return found_semaphores
    
    def find_mutexes(self, mutexes) -> List[IMutex]:
        found_mutexes = []
        for mutex in mutexes.split(";"):
            if mutex != "x":
                found_mutexes.append(self.find_in_array(self._mutexes, mutex))
        return found_mutexes
    
    def find_activities(self, activities) -> List[IActivity]:
        found_activities = []
        for activty in activities.split(";"):
            found_activities.append(self.find_in_array(self._activities, activty))
        return found_activities

    def find_in_array(self, array, name):
        found_elements = [element for element in array if element._name == name.strip()]
        if len(found_elements) > 0:
            return found_elements
        else:
            print(f"ERROR: No {array[0].__class__.__name__} with name {name} found. Check if the name is correct or the object is missing.")
            return []
    
    def data_restructuring(self, rows: List[List[str]]):
        for row in rows:
            for counter in range(len(row)):
                row[counter] = row[counter].strip()

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