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

    def run(self):
        #semaphore reduzieren / erhöhen
        #duration anpassen
        
        if self._temp_duration == 1:
            self.finish()
            return
        elif self._temp_duration == self._duration:
            if not self.start():                            # If the start fails, the activity can't be run
                return
        self._temp_duration -= 1
        print(f"Activity {self._name} is running. Duration: {self._temp_duration} (of {self._duration})")

    def start(self) -> bool:
        reserved_semaphores = []
        # Are all incoming semaphores available?
        for semaphore in self._incoming_semaphores:
            if not semaphore.get_state() > 0:
                return False
        
        # Reserve all incoming semaphores
        for semaphore in self._incoming_semaphores: 
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
        self._active = True
        return True

    def finish(self):
        for semaphore in self._outgoing_semaphores: 
                semaphore.release()

        self._active = False
        self._temp_duration = self._duration