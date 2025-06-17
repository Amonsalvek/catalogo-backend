from flask import Flask, jsonify, request
import requests
import os
from flask_cors import CORS  # 👈 IMPORTANTE

app = Flask(__name__)
CORS(app)  # 👈 ESTO ACTIVA CORS

@app.route("/api/catalogo")
def catalogo():
    sheet = request.args.get("sheet", "accesos")
    url = f"https://script.google.com/macros/s/AKfycbzpaW4vFJ-vv_k3BfiSriZssmrwsmNmti747rKv5LXbz24c2sV7XRs6SC6fk9sTzle23g/exec?sheet={sheet}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
