import json, os, time
from flask import Flask, jsonify, render_template, request, send_file
from Diagram import Diagram
from FileReader import FileReader


app = Flask(__name__)

file_reader = FileReader()
diagram = Diagram()

startup_executed = False
first_pic = True

if not startup_executed:
    # Pfad zur CSV-Datei mit der Konfiguration
    source_filepath = "./static/csv/example-structure.csv"

    rows = file_reader.open(source_filepath)

    diagram.generate(rows)
    startup_executed = True

@app.route('/visualizer-api/reset-diagram', methods=['GET'])
def origin_status():
    global first_pic
    diagram.reset(False)
    first_pic = True
    diagram.generate(rows)
    diagram.draw_graph()
    time.sleep(2)
    return jsonify("Success")

# to read a new csv File
@app.route('/visualizer-api/update-config', methods=['GET'])
def update_config():
    global rows
    global source_filepath
    global startup_executed
    source_filepath = "./static/csv/" + request.args.get('config-name')
    diagram.reset(True)

    rows = file_reader.open(source_filepath)
    diagram.generate(rows)
    startup_executed = True
    return jsonify("Success")

@app.route('/visualizer-api/diagram', methods=['GET'])
def get_diagram():
    global first_pic
    if first_pic:
        first_pic = False
    else:
        diagram.execute_cycle()
    diagram.draw_graph()
    print(os.getcwd())
    file_path = "./static/images/testGraph.png"
    return send_file(file_path, mimetype='image/png')

@app.route('/visualizer-api/config-list', methods=['GET'])
def get_config_list():
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk("./static/csv"):
        file_list.extend(filenames)
        break
    return jsonify(file_list)
if __name__ == '__main__':
    app.run(debug=True)


