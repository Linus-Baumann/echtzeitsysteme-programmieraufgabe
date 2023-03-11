from Abstracts import IActivity

class Activity(IActivity):
    _name = ""
    _duration = 0
    _active = False

    def __init__(self, activity_name, actvity_duration, incoming_semaphores, outgoing_semaphores, relevant_mutexes, active=False) -> None:
        self._name = activity_name
        self._duration = actvity_duration
        self._incoming_semaphores = incoming_semaphores
        self._outgoing_semaphores = outgoing_semaphores
        self._relevant_mutexes = relevant_mutexes
        self._active = active

    #Simon getter und setter für die properties und blaupause für run
    @property
    def active(self) -> bool:
        return self._active