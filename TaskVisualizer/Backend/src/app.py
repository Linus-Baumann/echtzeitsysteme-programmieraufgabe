import json, os, time
from flask import Flask, jsonify, render_template, request, send_file
from Diagram import Diagram
from FileReader import FileReader

app = Flask(__name__)

file_reader = FileReader()
diagram = Diagram()

startup_executed = False

if not startup_executed:
    # Pfad zur CSV-Datei mit der Konfiguration
    source_filepath = "./static/csv/example-structure.csv"

    rows = file_reader.open(source_filepath)

    diagram.generate(rows)
    startup_executed = True

@app.route('/visualizer-api/reset-diagram', methods=['GET'])
def origin_status():
    diagram.reset()
    diagram.generate(rows)
    diagram.draw_graph()
    time.sleep(2)
    return jsonify("Success")

@app.route('/visualizer-api/diagram', methods=['GET'])
def get_diagram():
    diagram.execute_cycle()
    diagram.draw_graph()
    print(os.getcwd())
    file_path = "./static/images/testGraph.png"
    return send_file(file_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)


