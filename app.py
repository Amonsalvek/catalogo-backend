from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import csv
import io

app = Flask(__name__)
CORS(app)

SHEET_URLS = {
    "accesos": "https://docs.google.com/spreadsheets/d/1-r__LMsLbiVj3dXxv8lbY6eGgwSj_gVxOjO1WgRx9K0/export?format=csv&gid=259253579",
    "catalogo": "https://docs.google.com/spreadsheets/d/1-r__LMsLbiVj3dXxv8lbY6eGgwSj_gVxOjO1WgRx9K0/export?format=csv&gid=0"
}

@app.route('/api/catalogo', methods=['GET'])
def get_catalogo():
    sheet = request.args.get("sheet", "accesos")
    url = SHEET_URLS.get(sheet)

    if not url:
        return jsonify({"error": "Hoja no encontrada"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Leer CSV
        f = io.StringIO(response.text)
        reader = csv.DictReader(f)
        data = list(reader)

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
