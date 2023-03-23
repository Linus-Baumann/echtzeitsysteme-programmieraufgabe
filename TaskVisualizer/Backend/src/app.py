import json
from flask import Flask, render_template, request, send_file
from Diagram import Diagram
from FileReader import FileReader
import os

app = Flask(__name__)

file_reader = FileReader()
diagram = Diagram()

# Pfad zur CSV-Datei mit der Konfiguration
filepath = "./TaskVisualizer/Backend/src/static/csv/example-structure.csv"

rows = file_reader.open(filepath)

diagram.generate(rows)

@app.route('/visualizer-api/diagram', methods=['GET'])
def get_diagram():
    diagram.execute_cycle()
    diagram.draw_graph()
    print(os.getcwd())
    file_path = "./TaskVisualizer/Backend/src/static/images/testGraph.png"
    return send_file(file_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
