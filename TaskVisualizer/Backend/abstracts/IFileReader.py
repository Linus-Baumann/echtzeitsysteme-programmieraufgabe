# Excel Datei einlesen

import numpy as np
from typing import List
from abc import ABC, abstractmethod

class ICSVOperator(ABC):
    @abstractmethod
    def open(self, csv_filename):
        pass

    @abstractmethod
    def parse(self, rows):
        pass
