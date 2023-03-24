import csv
import os
from typing import List
from Abstracts import IDiagram, ITask, IActivity, ISemaphore, IMutex
from Semaphore import Semaphore
from Mutex import Mutex
from Task import Task
from Activity import Activity
import graphviz as gv

class Diagram(IDiagram):
    def __init__(self):
        self._rows = []
        self._tasks = []
        self._activities = []
        self._semaphores = []
        self._mutexes = []

    def check_file_structure(self, rows: List[List[str]]) -> bool:
        print("Checking structure...")
        structure_is_good = True
        allowed_items = ["Semaphore", "Mutex", "Activity", "Task"]
        scanned_items = []
        current_index = 0
        for row in rows:
            try:
                if row[0] != allowed_items[current_index]:
                    current_index += 1
                if row[0] not in scanned_items:
                    scanned_items.append(row[0])
                if current_index > 3:
                    print("ERROR: Wrong file structure. Check if the file lists the Semaphores, Activities, Mutexes and Tasks in the correct order. Other items are not allowed.")
                    structure_is_good = False
            except IndexError:
                rows.remove(row)
                print("Empty Line (IndexError) resolved by deletion: " + str(row))
            
            if row[0] == "Semaphore" and len(row) != 3:
                print("ERROR: Wrong Semaphore structure. Check if the Semaphores have the correct amount of columns. 'Semaphore', 'Name', 'Activated'")
                structure_is_good = False
            if row[0] == "Mutex" and len(row) != 2:
                print("ERROR: Wrong Mutex structure. Check if the Mutexes have the correct amount of columns. 'Mutex', 'Name'")
                structure_is_good = False
            if row[0] == "Activity" and (len(row) != 5 and len(row) != 6):
                print("ERROR: Wrong Activity structure. Check if the Activities have the correct amount of columns. 'Activity', 'Duration', 'Name', 'Ingoing Semaphores', 'Outgoing Semaphores', 'Mutexes'")
                structure_is_good = False
            if row[0] == "Task" and len(row) !=3:
                print("ERROR: Wrong Task structure. Check if the Tasks have the correct amount of columns. 'Task', 'Name', 'Activities'")
                structure_is_good = False
        if scanned_items != allowed_items:
            print("ERROR: Wrong file structure. Check if the file lists the Semaphores, Activities, Mutexes and Tasks in the correct order. Other items are not allowed.")
            structure_is_good = False
        if structure_is_good:
            print("Structure is correct.")
        else:
            print("Structure is not correct.")
        return structure_is_good

    def parse(self, rows):
        self.data_restructuring(rows)
        if not self.check_file_structure(rows):
            return False
        for object in rows:
            if object[0] == "Task":  
                included_activities = self.find_activities(object[2])
                self._tasks.append(Task(object[1], included_activities))
                print(f"Task created: {object[1]}")
            elif object[0] == "Activity":
                incoming_semaphores = self.find_semaphores(object[3])
                outgoing_semaphores = self.find_semaphores(object[4])
                relevant_mutexes = self.find_mutexes(object[5])
                self._activities.append(Activity(object[1], object[2], incoming_semaphores, outgoing_semaphores, relevant_mutexes))
                print(f"Activity created: {object[1]}")
            elif object[0] == "Semaphore":
                self._semaphores.append(Semaphore(object[1].strip(), object[2].strip()))
                print(f"Semaphore created: {object[1]}")
            elif object[0] == "Mutex":
                self._mutexes.append(Mutex(object[1]))
                print(f"Mutex created: {object[1]}")
        return True
    
    def fill_objects(self, objects: List):
        for object in objects:
            if isinstance(object, ITask):
                child_activities = object.get_activities()
                for activity in child_activities:
                    activity.set_task(object)
            for activity in self._activities:
                if isinstance(object, IMutex):
                    # Check if the activity has the mutex in its relevant mutexes and check if the mutex is not empty
                    relevant_mutexes = [mutex for mutex in activity.get_relevant_mutexes() if mutex]
                    if not relevant_mutexes:
                        continue
                    activity_list = [mutex for mutex in relevant_mutexes if mutex.get_name() == object.get_name()]
                    if activity_list:
                        object.add_to_activity_list(activity)
                if isinstance(object, ISemaphore):
                    incoming_semaphores = [semaphore for semaphore in activity.get_incoming_semaphores() if semaphore]
                    outgoing_semaphores = [semaphore for semaphore in activity.get_outgoing_semaphores() if semaphore]
                    if incoming_semaphores:
                        waiting_activites_list = [semaphore for semaphore in incoming_semaphores if semaphore.get_name() == object.get_name()]
                    if outgoing_semaphores:
                        actuator_list = [semaphore for semaphore in outgoing_semaphores if semaphore.get_name() == object.get_name()]
                    if actuator_list:
                        object.add_to_actuators(activity)
                    if waiting_activites_list:
                        object.add_to_waiting_activities(activity)

    def find_semaphores(self, semaphores) -> List[ISemaphore]:
        found_semaphores = []
        for semaphore in semaphores.split(";"):
            if semaphore.count(":") > 0:
                found_semaphore_relation = []
                # Do something if argument is a list
                for related_semaphore in semaphore.split(":"):
                    self.find_in_array(self._semaphores, related_semaphore)[0].set_combined(map(lambda x: self.find_in_array(self._semaphores, x)[0], semaphore.split(':')))
                    found_semaphore_relation.extend(self.find_in_array(self._semaphores, related_semaphore.strip()))
                found_semaphores.extend(found_semaphore_relation)
            else:
                # Do something if argument is a string
                found_semaphores.extend(self.find_in_array(self._semaphores, semaphore))
        return found_semaphores
    
    def find_mutexes(self, mutexes) -> List[IMutex]:
        found_mutexes = []
        for mutex in mutexes.split(";"):
            if mutex != "x":
                found_mutexes.extend(self.find_in_array(self._mutexes, mutex))
        return found_mutexes
    
    def find_activities(self, activities) -> List[IActivity]:
        found_activities = []
        for activty in activities.split(";"):
            found_activities.extend(self.find_in_array(self._activities, activty))
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

    def generate(self, rows: List[List[str]]):
        self._rows = rows

        #Diagramm erstellen, sollte Anfangszustand herstellen, nur einmal ausführen
        self.parse(self._rows)
        self.fill_objects(self._mutexes)
        self.fill_objects(self._semaphores)
        self.fill_objects(self._tasks)
        pass

    def draw_activitys(self, dot):
        for activity in self._activities:
            task = activity.get_task()
            task_name = task.get_name()
            act_name = activity.get_name()

            if activity.get_active():
                dot.node(name=act_name,shape='record', style='filled', fillcolor='green', label='{'+f"T: {task_name}|A {act_name}: {activity.get_duration()}"+'}')
            else:    
                dot.node(name=act_name,shape='record', style='filled', fillcolor='white', label='{'+f"T: {task_name}|A {act_name}: {activity.get_duration()}"+'}')
        pass

    def draw_semaphores(self, dot):
        bufsemaphores = self._semaphores.copy()
        while len(bufsemaphores) != 0:
            semaphore = bufsemaphores.pop(0)
            actuators = semaphore.get_actuators()
            waiting_activities = semaphore.get_waiting_activities()    
        
            if len(semaphore.get_combined()) == 0:
                if semaphore.get_state() == 0:
                    if actuators[0].get_task() == waiting_activities[0].get_task():
                        dot.edge(f'{actuators[0].get_name()}', f'{waiting_activities[0].get_name()}', label= semaphore.get_name()+ ': ' + str(semaphore.get_state()), arrowhead='onormal', color='black')
                    else:
                        dot.edge(f'{actuators[0].get_name()}', f'{waiting_activities[0].get_name()}', label= semaphore.get_name()+ ': ' +str(semaphore.get_state()), arrowhead='', color='black')    
                else:
                    if actuators[0].get_task() == waiting_activities[0].get_task():
                        dot.edge(f'{actuators[0].get_name()}', f'{waiting_activities[0].get_name()}', label= semaphore.get_name()+ ': ' +str(semaphore.get_state()), arrowhead='onormal', color='green')
                    else:
                        dot.edge(f'{actuators[0].get_name()}', f'{waiting_activities[0].get_name()}', label= semaphore.get_name()+ ': ' +str(semaphore.get_state()), arrowhead='', color='green')
            else:
                combi = semaphore.get_combined()
                name =  ''
                for obj in combi:
                    name += obj.get_name()
                dot.node(name=name, shape='point', width='0.01', height='0.01')

                active_temp = False
                for obj in combi:
                    if obj.get_state() == 0:
                        dot.edge(f'{obj.get_actuators()[0].get_name()}', f'{name}', label= semaphore.get_name()+ ': ' +str(obj.get_state()), arrowhead='none', color='black')
                    else: 
                        dot.edge(f'{obj.get_actuators()[0].get_name()}', f'{name}', label= semaphore.get_name()+ ': ' +str(obj.get_state()), arrowhead='none', color='green')
                        active_temp = True
                    if obj in bufsemaphores:
                        bufsemaphores.remove(obj)
                if active_temp:        
                    dot.edge(f'{name}', f'{waiting_activities[0].get_name()}', arrowhead='', color='green')
                    active_temp = False
                else:
                    dot.edge(f'{name}', f'{waiting_activities[0].get_name()}', arrowhead='', color='black')
        pass

    def draw_mutexes(self, dot):
        for mutex in self._mutexes:
            if mutex.get_state():
                dot.node(name=mutex.get_name(), shape='polygon', sides='5', style='filled', fillcolor='green', label="M: " + mutex.get_name())
            else:
                dot.node(name=mutex.get_name(), shape='polygon', sides='5', style='filled', fillcolor='white', label="M: " + mutex.get_name())    
            for activity in mutex.get_activity_list():
                #Weis nicht ob das geht, weil dan die Activity zuerst activ werden muss???
                if activity.get_active():
                    dot.edge(mutex.get_name(), activity.get_name(), style='dashed', arrowhead='none', color='green')
                else:
                    dot.edge(mutex.get_name(), activity.get_name(), style='dashed', arrowhead='none', color='black')
        pass

    #Zeichnen des Diagramms
    def draw_graph(self):
        dot = gv.Digraph(comment='Graph')
        #Activitys zeichnen
        self.draw_activitys(dot)
        #Semaphores zeichnen
        self.draw_semaphores(dot)
        #Mutexe zeichnen
        self.draw_mutexes(dot)
        dot.render('./static/images/testGraph', view=False, format='png')

    def execute_cycle(self):
        for activity in self._activities:
            activity.run()
        for activity in self._activities:
            activity.run(False)

    def reset(self):
        self._tasks = []
        self._activities = []
        self._semaphores = []
        self._mutexes = []
        pass

    def get_tasks(self) -> List[ITask]:
        return self._tasks

    def get_activities(self) -> List[IActivity]:
        return self._activities

    def get_semaphores(self) -> List[ISemaphore]:
        return self._activities

    def get_mutexes(self) -> List[IMutex]:
        return self._mutexes