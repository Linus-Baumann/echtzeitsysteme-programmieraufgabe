import json
from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# Pfad zum Verzeichnis mit den Bildern und CSV-Dateien
image_directory = os.path.join(os.getcwd(), 'static/images')
csv_directory = os.path.join(os.getcwd(), 'static/csv')

# Liste der Bilder im Verzeichnis
image_list = os.listdir(os.path.normpath(image_directory))

@app.route('/', methods=['GET'])
def index():
    # Standardmäßig wird das erste Bild im Verzeichnis angezeigt
    image_path = os.path.join(image_directory, image_list[0])
    return render_template('index.html', image_path=image_path)

@app.route('/next', methods=['POST'])
def next_image():
    # Nächstes Bild in der Liste anzeigen
    current_image = request.form['current_image']
    current_index = image_list.index(current_image)
    next_index = (current_index + 1) % len(image_list)
    next_image = image_list[next_index]
    next_image_path = os.path.join(image_directory, next_image)
    return render_template('index.html', image_path=next_image_path)

@app.route('/previous', methods=['POST'])
def previous_image():
    # Vorheriges Bild in der Liste anzeigen
    current_image = request.form['current_image']
    current_index = image_list.index(current_image)
    previous_index = (current_index - 1) % len(image_list)
    previous_image = image_list[previous_index]
    previous_image_path = os.path.join(image_directory, previous_image)
    return render_template('index.html', image_path=previous_image_path)

@app.route('/save', methods=['POST'])
def save_image():
    # Hier können Sie den Code zum Speichern des Bildes einfügen
    pass

@app.route('/csv', methods=['POST'])
def select_csv():
    # CSV-Datei auswählen
    csv_file = request.files['csv_file']
    csv_path = os.path.join(csv_directory, csv_file.filename)
    csv_file.save(csv_path)
    return render_template('index.html', csv_path=csv_path)

@app.route('/visualizer-api/diagram', methods=['GET'])
def get_diagram():
    # Hier können Sie den Code zum Laden des Diagramms einfügen
    # converts the diagram to a json string and returns it
    file_path = "./static/images/lobster.png"
    return send_file(file_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
