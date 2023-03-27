from typing import List
from Abstracts import IActivity, ISemaphore, IMutex
from Semaphore import Semaphore
import numpy as np

class Activity(IActivity):
    def __init__(self, name, actvity_duration, incoming_semaphores, outgoing_semaphores, relevant_mutexes, active=False) -> None:
        self._name = name
        self._duration = int(actvity_duration)
        self._temp_duration = int(actvity_duration)
        self._incoming_semaphores = incoming_semaphores
        self._outgoing_semaphores = outgoing_semaphores
        self._relevant_mutexes = relevant_mutexes
        self._active = active
        self._task = None
        self._reserved_semaphores = []
        self._reserved_mutexes = []

    def get_name(self) -> str:
        return self._name

    def set_task(self, task):
        if self._task is not None:
            print("ERROR: Activity already has a task assigned to it")
            return
        self._task = task

    def get_task(self):
        return self._task

    def get_duration(self) -> str:
        return self._duration
    
    def get_active(self) -> bool:
        return self._active

    def get_incoming_semaphores(self) -> List[ISemaphore]:
        return self._incoming_semaphores

    def get_outgoing_semaphores(self) -> List[ISemaphore]:
        return self._outgoing_semaphores

    def get_relevant_mutexes(self) -> List[IMutex]:
        return self._relevant_mutexes

    # Executes the activity for one cycle
    def run(self, work_on_activity: bool = True):
        # If the activity is is on it's last cycle, finish it        
        if self._temp_duration == 1 and work_on_activity:
            self.finish()
        # If the activity is not active, start it
        elif not self._active:
            self.start()                            # If the start fails, the activity can't be run
            return
        if work_on_activity:
            # Decrease the activity's duration
            self._temp_duration -= 1
            print(f"Activity {self._name} is running. Duration: {self._temp_duration} (of {self._duration})")

    # Returns True if the activity could be started, False if not
    def start(self) -> bool:
        if self.reserve_semaphores() and self.reserve_mutexes():
            self._active = True
            print(f"------------- Activity {self._name} started --------------")
            return True
        else:
            self.release_dependencies()
            return False
    
    def release_dependencies(self):
        # print(f"Releasing all reserved mutexes for activity {self._name}...")
        for reserved_mutex in self._reserved_mutexes:
            reserved_mutex.release()
            self._reserved_mutexes.remove(reserved_mutex)
        # print(f"Releasing all reserved semaphores for activity {self._name}...")
        for reserved_semaphore in self._reserved_semaphores:
            reserved_semaphore.release()
            self._reserved_semaphores.remove(reserved_semaphore)
        # print("Successfully released all reserved semaphores and mutexes for activity {self._name}.")
    
    def reserve_semaphores(self) -> bool:
        for semaphore in self._incoming_semaphores:
            if not semaphore.get_combined():
                # Reserve all incoming semaphores
                if semaphore.reserve():
                    self._reserved_semaphores.append(semaphore)
                    print(f"Successfully reserved semaphore {semaphore.get_name()} for activity {self._name}.")
                    
            else:
                combined_semaphore = semaphore.get_combined()
                for inner_semaphore in combined_semaphore:
                    if inner_semaphore not in self._reserved_semaphores:
                        combination_satisfied = True

                if not combination_satisfied: 
                    if inner_semaphore.reserve():
                        self._reserved_semaphores.append(semaphore)
                        print(f"Successfully reserved semaphore {semaphore.get_name()} for activity {self._name}.")
                      
                    else:
                        return False
        return True

    def reserve_mutexes(self) -> bool:
        for mutex in self._relevant_mutexes:
            # Reserve the mutex
            if mutex.reserve():
                self._reserved_mutexes.append(mutex)
                print(f"Successfully reserved mutexes {mutex.get_name()} for activity {self._name}.")
            else:
                print(f"ERROR: Mutex {mutex.get_name()} could not be reserved. Activity {self._name} can't be run!")
                return False
        return True

    def finish(self):
        # Release all outgoing semaphores
        for semaphore in self._outgoing_semaphores: 
            semaphore.release()
            print(f"Successfully released semaphore {semaphore.get_name()} by activity {self._name}.")
        self._reserved_semaphores = []
        self._reserved_mutexes = []
        # Release all relevant mutexes
        for mutex in self._relevant_mutexes:
            if mutex.release():
                print(f"Successfully released mutex {mutex.get_name()} by activity {self._name}.")
        self._active = False
        self._temp_duration = self._duration
        print(f"------------- Activity {self._name} finished -------------")