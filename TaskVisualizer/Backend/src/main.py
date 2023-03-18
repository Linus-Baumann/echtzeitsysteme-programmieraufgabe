from Diagram import Diagram
from FileReader import FileReader
import os

file_reader = FileReader()
diagram = Diagram()

rows = file_reader.open("example-structure.csv")

diagram.draw_graph()

diagram.generate(rows)
while (True):
    os.system("cls")
    diagram.execute_cycle()
    input("Press Enter to continue...")
print("Done")