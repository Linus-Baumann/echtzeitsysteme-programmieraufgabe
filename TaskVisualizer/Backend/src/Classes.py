import numpy as np
from typing import List
from Abstracts import ITask,IActivity,IMutex,ISemaphore

class Task(ITask):
    name = ""
    #Liste der dazugehörigen Aktivitäten?
    actList = []   

    def __init__(self, taskName):
        self.name = taskName


class Activity(IActivity):
    name = ""
    duration = 0

    def __init__(self, actName, actDuration) -> None:
        self.name = actName
        self.duration = actDuration
        


class Mutex(IMutex):
# Liste von Aktivitäten?
    actList = []
    initValue = 0

    def __init__(self) -> None:
        super().__init__()


class Semaphore(ISemaphore):
# Veroderung fehlt bei den Semaphoren noch!!
    fromAct = ""
    toAct = ""
    initValue = 0

    def __init__(self, fromAct, toAct, actValue) -> None:
        self.fromAct = fromAct
        self.toAct = toAct
        self.initValue = actValue