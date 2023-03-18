from Diagram import Diagram
from FileReader import FileReader
import os

file_reader = FileReader()
diagram = Diagram()

rows = file_reader.open("example-structure.csv")

diagram.draw_graph()

diagram.generate(rows)
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
diagram.execute_cycle()
print("Done")