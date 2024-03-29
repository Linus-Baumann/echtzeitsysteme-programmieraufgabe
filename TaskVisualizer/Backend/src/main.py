from Diagram import Diagram
from FileReader import FileReader
import os

file_reader = FileReader()
diagram = Diagram()

#rows = file_reader.open("./TaskVisualizer/Backend/src/static/csv/alternative-structure.csv")
#rows = file_reader.open("./TaskVisualizer/Backend/src/static/csv/test_or.csv")
rows = file_reader.open("./TaskVisualizer/Backend/src/static/csv/example-structure.csv")

#diagram.draw_graph()

diagram.generate(rows)
diagram.draw_graph()
while (True):
    #os.system("cls")
    print("###############################################")
    diagram.execute_cycle()
    diagram.draw_graph()
    input("Press Enter to continue...")
print("Done")