from Diagram import Diagram
from FileReader import FileReader
import os

file_reader = FileReader()
diagram = Diagram()

rows = file_reader.open("example-structure.csv")

diagram.generate(rows)
print("Done")