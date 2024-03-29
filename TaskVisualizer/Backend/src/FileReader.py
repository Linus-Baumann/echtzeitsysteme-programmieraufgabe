import csv
import numpy as np
from typing import List
from Abstracts import IFileReader


class FileReader(IFileReader):
    def __init__(self):
        pass

    def open(self, csv_filename) -> List[List[str]]:
        rows = []
        try:
            with open(csv_filename, "r") as f:
                reader = csv.reader(f)
                rows = [row for row in reader if row != []]
        except Exception as exception:
            print(f"The program failed to open the file. It is very sorry... ()\nThis might help you:\t{exception}")
        return rows