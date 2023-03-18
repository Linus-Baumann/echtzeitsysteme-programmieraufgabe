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
    def run(self):
        # If the activity is is on it's last cycle, finish it        
        if self._temp_duration == 1:
            self.finish()
            return
        # If the activity is not active, start it
        elif self._temp_duration == self._duration:
            if not self.start():                            # If the start fails, the activity can't be run
                return
        # Decrease the activity's duration
        self._temp_duration -= 1
        print(f"Activity {self._name} is running. Duration: {self._temp_duration} (of {self._duration})")

    # Returns True if the activity could be started, False if not
    def start(self) -> bool:
        self._active = True
        return self.reserve_semaphores() and self.reserve_mutexes()
    
    def reserve_semaphores(self) -> bool:
        reserved_semaphores = []
        
        for semaphore in self._incoming_semaphores:
            # Are all incoming semaphores available?
            if not semaphore.get_state() > 0:
                return False
            # Reserve all incoming semaphores
            if not semaphore.reserve():
                print(f"ERROR: Semaphore {semaphore.get_name()} could not be reserved. Activity {self._name} can't be run!")
                print(f"Releasing all reserved semaphores for activity {self._name}...")
                for reserved_semaphore in reserved_semaphores:
                    reserved_semaphore.release()
                print("Successfully released all reserved semaphores for activity {self._name}.")
                return False
            else:
                reserved_semaphores.append(semaphore)
                print(f"Successfully reserved semaphore {semaphore.get_name()} for activity {self._name}.")
        return True
    
    def reserve_mutexes(self) -> bool:
        reserved_mutexes = []
        for mutex in self._relevant_mutexes:
            if mutex.get_state():
                print(f"ERROR: Mutex {mutex.get_name()} is already reserved. Activity {self._name} can't be run!")
                return False
            if not mutex.reserve():
                print(f"ERROR: Mutex {mutex.get_name()} could not be reserved. Activity {self._name} can't be run!")
                print(f"Releasing all reserved mutexes for activity {self._name}...")
                for reserved_mutex in reserved_mutexes:
                    reserved_mutex.release()
                print("Successfully released all reserved mutexes for activity {self._name}.")
                return False
            else:
                reserved_mutexes.append(mutex)
                print(f"Successfully reserved mutexes {mutex.get_name()} for activity {self._name}.")
        return True

    def finish(self):
        # Release all outgoing semaphores
        for semaphore in self._outgoing_semaphores: 
                semaphore.release()
        self._active = False
        self._temp_duration = self._duration