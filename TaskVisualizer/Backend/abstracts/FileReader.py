# Excel Datei einlesen

import numpy as np
from typing import List
from abc import ABC, abstractmethod

class abs_CSVOperator(ABC):
    @property
    @abstractmethod
    def open(self, csv_filename):
        pass
    
