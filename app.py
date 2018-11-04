from flask import Flask, json
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M")

    return """
    <h1>Hola!! Prueba para IV 2018</h1>
    <p>Hora actual: {time}.</p>
    """.format(time=the_time)

@app.route("/status")
def status():
    with open('status.json') as f:
        data = json.load(f)
        response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
