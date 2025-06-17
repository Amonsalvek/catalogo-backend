from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/api/catalogo")
def catalogo():
    sheet = request.args.get("sheet", "accesos")  # accesos o catalogo
    url = f"https://script.google.com/macros/s/AKfycbzpaW4vFJ-vv_k3BfiSriZssmrwsmNmti747rKv5LXbz24c2sV7XRs6SC6fk9sTzle23g/exec?sheet={sheet}"
    response = requests.get(url)
    return jsonify(response.json())
