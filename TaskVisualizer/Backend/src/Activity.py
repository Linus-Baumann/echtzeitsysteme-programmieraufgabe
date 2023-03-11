from Abstracts import IActivity
import numpy as np

class Activity(IActivity):
    _name = ""
    _duration = 0
    _temp_duration = 0 #Für die Run Funktion
    _active = False
    _incoming_semaphores = np.array
    _outgoing_semaphores = np.array
    _relevant_mutexes = np.array

    def __init__(self, activity_name, actvity_duration, incoming_semaphores, outgoing_semaphores, relevant_mutexes, active=False) -> None:
        self._name = activity_name
        self._duration = actvity_duration
        self._temp_duration = actvity_duration #Für die Run Funktion
        self._incoming_semaphores = incoming_semaphores
        self._outgoing_semaphores = outgoing_semaphores
        self._relevant_mutexes = relevant_mutexes
        self._active = active

    @property
    def active(self) -> bool:
        return self._active
    
    @property
    def incoming_semaphores(self) -> np.array:
        return self._incoming_semaphores

    @property
    def outgoing_semaphores(self) -> np.array:
        return self._outgoing_semaphores

    @property
    def relevant_mutexes(self) -> np.array:
        return self._relevant_mutexes

    def run(self):
        #semaphore reduzieren / erhöhen
        #duration anpassen
        if self._temp_duration == 0:
            for object in self._outgoing_semaphores: 
                #object.                           # Funktion zum erhöhen der Semaphore fehlt
            
            for object in self._incoming_semaphores: 
                #object.                           # Funktion zum verringern der Semaphore fehlt

            self._active = False
            self._temp_duration = self._duration

        elif self._temp_duration <= self._duration:
            self._temp_duration -= 1

        elif self._temp_duration == self._duration:
            self._active = True
            self._temp_duration -= 1

        pass