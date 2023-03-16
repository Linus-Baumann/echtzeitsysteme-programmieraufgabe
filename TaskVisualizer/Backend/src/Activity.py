from typing import List
from Abstracts import IActivity, ISemaphore, IMutex
from Semaphore import Semaphore
import numpy as np

class Activity(IActivity):
    def __init__(self, name, actvity_duration, incoming_semaphores, outgoing_semaphores, relevant_mutexes, active=False) -> None:
        self._name = name
        self._duration = actvity_duration
        self._temp_duration = actvity_duration
        self._incoming_semaphores = incoming_semaphores
        self._outgoing_semaphores = outgoing_semaphores
        self._relevant_mutexes = relevant_mutexes
        self._active = active

    @property
    def get_name(self) -> str:
        return self._name
    
    @property
    def get_duration(self) -> str:
        return self._duration
    
    @property
    def active(self) -> bool:
        return self._active
    
    @property
    def incoming_semaphores(self) -> List[ISemaphore]:
        return self._incoming_semaphores

    @property
    def outgoing_semaphores(self) -> List[ISemaphore]:
        return self._outgoing_semaphores

    @property
    def relevant_mutexes(self) -> List[ISemaphore]:
        return self._relevant_mutexes

    def run(self):
        #semaphore reduzieren / erhöhen
        #duration anpassen
        if self._temp_duration == 0:
            for semaphore in self._outgoing_semaphores: 
                semaphore.release()                           # Funktion zum erhöhen der Semaphore fehlt

            self._active = False
            self._temp_duration = self._duration

        elif self._temp_duration <= self._duration:
            self._temp_duration -= 1

        elif self._temp_duration == self._duration:
            for semaphore in self._incoming_semaphores:
                if not semaphore.state() > 0:
                    return
            for semaphore in self._incoming_semaphores: 
                semaphore.reserve()                           # Funktion zum verringern der Semaphore fehlt
            self._active = True
            self._temp_duration -= 1