from flask import Flask, json, jsonify, request
from datetime import datetime
from obra import Obras

app = Flask(__name__)

@app.route("/")
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

@app.route("/AllObras", methods=['GET'])
def AllObras():
    misObras = Obras()

    todas = misObras.all_obras()
    output = []
    for ob in todas:
        output.append({
            'nombre' : ob['nombre'], 
            'precio' : ob['precio'],
            'descripcion' : ob['descripcion'],
            'activa' : ob['activa'],
            'tipo_pago' : ob['tipo_pago'],
            'materiales' : ob['materiales'],
            'horas_mano_obra' : ob['horas_mano_obra']
        })

    response = app.response_class(
        response=json.dumps(output),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/buscarObra/<nombre>", methods=['GET'])
def buscarObra(nombre):
    misObras = Obras()
    respuesta = misObras.buscar_obra(nombre)
    output = []

    if(respuesta != None):
        for ob in respuesta:
            output.append({
                'nombre' : ob['nombre'], 
                'precio' : ob['precio'],
                'descripcion' : ob['descripcion'],
                'activa' : ob['activa'],
                'tipo_pago' : ob['tipo_pago'],
                'materiales' : ob['materiales'],
                'horas_mano_obra' : ob['horas_mano_obra']
            })
    else:
        output = "No se ha encontrado la obra con nomnbre: " + nombre

    response = app.response_class(
        response=json.dumps(output),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/crearObra", methods=['POST'])
def crearObras():
    misObras = Obras()

    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']
    activa = request.json['activa']
    tipo_pago = request.json['tipo_pago']
    materiales = request.json['materiales']
    horas_mano_obra = request.json['horas_mano_obra']

    nueva = Obra(nombre, precio, descripcion, activa, tipo_pago, materiales, horas_mano_obra)
    misObras.add(nueva)

    respuesta = misObras.buscar_obra(nombre)
    output = []

    if(respuesta != None):
        for ob in respuesta:
            output.append({
                'nombre' : ob['nombre'], 
                'precio' : ob['precio'],
                'descripcion' : ob['descripcion'],
                'activa' : ob['activa'],
                'tipo_pago' : ob['tipo_pago'],
                'materiales' : ob['materiales'],
                'horas_mano_obra' : ob['horas_mano_obra']
            })

    response = app.response_class(
        response=json.dumps(output),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()
    #app.run(use_reloader=True, host='0.0.0.0', port="80")
