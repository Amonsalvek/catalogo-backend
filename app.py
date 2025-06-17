from flask import Flask, jsonify, request
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Esto habilita CORS automáticamente

@app.route("/api/catalogo")
def catalogo():
    sheet = request.args.get("sheet", "accesos")
    url = f"https://script.google.com/macros/s/AKfycbzpaW4vFJ-vv_k3BfiSriZssmrwsmNmti747rKv5LXbz24c2sV7XRs6SC6fk9sTzle23g/exec?sheet={sheet}"
    r = requests.get(url)
    return jsonify(r.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render asigna dinámicamente el puerto
    app.run(host='0.0.0.0', port=port)
