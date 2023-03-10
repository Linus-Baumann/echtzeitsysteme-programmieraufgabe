import csv
import numpy as np
from typing import List
from abstracts.IFileReader import abs_CSVOperator

class CSVOperator(abs_CSVOperator):
    def __init__(self):
        pass

    def open(self, csv_filename) -> np.array:
        rows = []
        try:
            with open(csv_filename, "r") as f:
                reader = csv.reader(f)
                rows = [row for row in reader]
        except Exception as exception:
            print(f"The program failed to open the file. It is very sorry... ({self.id})\nThis might help you:\t{exception}")
        return np.array(rows[0])