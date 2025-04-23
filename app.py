from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

DATA_FILE = "reuniones.json"

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    if not os.path.exists(DATA_FILE):
        return jsonify({})
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/api/datos', methods=['POST'])
def guardar_datos():
    datos = request.get_json()
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    return jsonify({"mensaje": "Datos guardados correctamente"})

@app.route('/')
def index():
    return send_from_directory('.', 'reuniones.html')

if __name__ == '__main__':
    app.run(debug=True)
