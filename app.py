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
        print("TEXT:", response.text[:500])  # Muestra los primeros 500 caracteres de la respuesta
        response.raise_for_status()
        return jsonify(response.json())  # Intenta parsear JSON y devolverlo
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
