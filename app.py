from flask import Flask, jsonify, request
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/api/catalogo', methods=['GET'])
def get_catalogo():
    sheet = request.args.get("sheet", "accesos")
    url = f"https://script.google.com/macros/s/AKfycbzpaW4vFJ-vv_k3BfiSriZssmrwsmNmti747rKv5LXbz24c2sV7XRs6SC6fk9sTzle23g/exec?sheet={sheet}"

    try:
        response = requests.get(url)
        print("STATUS:", response.status_code)
        print("RAW TEXT:", repr(response.text[:300]))  # Imprime texto bruto para detectar errores invisibles

        if not response.text.strip():
            return jsonify({"error": "Respuesta vacía desde Google Apps Script"}), 502

        return jsonify(response.json())
    except Exception as e:
        print("EXCEPTION:", str(e))  # 🔍 IMPORTANTE
        return jsonify({"error": str(e)}), 500

@app.route("/api/debug", methods=["GET"])
def debug_sheet():
    url = "https://script.google.com/macros/s/AKfycbzpaW4vFJ-vv_k3BfiSriZssmrwsmNmti747rKv5LXbz24c2sV7XRs6SC6fk9sTzle23g/exec?sheet=accesos"
    r = requests.get(url)
    print("STATUS:", r.status_code)
    print("TEXT:", r.text[:500])
    return r.text  # Devuelve texto plano para verificar qué llega


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
