from flask import Flask, json
from datetime import datetime
app = Flask(__name__)

@app.route("/status")
def status():
    with open('data/status.json') as f:
        data = json.load(f)
        response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/datosObras")
def datos():
    datos = {
        "app": "ObrasMTA",
        "datos": "/datosObras/obraX",
        "x": "Entero 1 o 2"
    }

    with open(datos) as f:
        data = json.load(f)
        response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/datosObras/<file>")
def datosObras(file):
    with open("data/"+str(file)+".json") as f:
        data = json.load(f)
        response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port="80")
