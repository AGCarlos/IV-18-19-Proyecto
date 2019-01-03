# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

#
# Clase Obra
# Se define una obra con su id, nombre, precio, descripción, si está activa, tipo de pago,
# materiales usados y horas de mano de obra.
# Autor: Francisco Miguel Toledo Aguilera
# 

def conexion():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['test']
    return db.obrasmta

class Obra:
    def __init__(self, nombre, precio, descripcion, activa, tipo_pago, materiales, horas_mano_obra):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.activa = activa
        self.tipo_pago = tipo_pago
        self.materiales = materiales
        self.horas_mano_obra = horas_mano_obra

    def getName(self):
        return self.nombre

#
# Clase Obras
# Sistema CRUD de Obras
# Autor: Francisco Miguel Toledo Aguilera
# 
class Obras:
    def add(self, obra):
        obras = conexion()
        suID = "None"
        suID = obras.insert_one({
            "nombre": obra.nombre,
            "precio": obra.precio,
            "descripcion": obra.descripcion,
            "activa": obra.activa,
            "tipo_pago": obra.tipo_pago,
            "materiales": obra.materiales,
            "horas_mano_obra": obra.horas_mano_obra,
        }).inserted_id

        if(suID != "None"):
            return True
        else:
            return False
     
    def all_obras(self):
        bd = conexion()
        self.inicializar()
        return bd.find()

    def buscar_obra(self, name):
        bd = conexion()
        buscar = {"nombre": { "$regex": name } }
        respuesta = bd.find(buscar)
        if(respuesta.count() > 0):
            return respuesta
        else:
            return None

    def update(self, id, obra):
        bd = conexion()
        resultado = bd.productos.update_one(
            {
            '_id': ObjectId(id)
            }, 
            {
                '$set': {
                    "nombre": obra.nombre,
                    "precio": obra.precio,
                    "descripcion": obra.descripcion,
                    "activa": obra.activa,
                    "tipo_pago": obra.tipo_pago,
                    "materiales": obra.materiales,
                    "horas_mano_obra": obra.horas_mano_obra,
                }
            })
        return resultado.modified_count

    def delete(self, id):
        bd = conexion()
        resultado = bd.productos.delete_one(
            {
            '_id': ObjectId(id)
            })
        return resultado.deleted_count

    def delete_all(self):
        bd = conexion()
        return bd.drop()


    def size_obras(self):
        bd = conexion()
        return bd.count()

    def precio_con_iva(self, precio, t):
        iva = (precio*t) + precio
        return iva

    def gasto_total_obras_sinIVA(self):
        bd = conexion()
        obras = bd.find()
        count = 0
        for ob in obras:
            count += ob['precio']

        return count

    def gasto_total_obras_conIVA(self):
        bd = conexion()
        obras = bd.find()
        count = 0
        for ob in obras:
            count += self.precio_con_iva(ob['precio'], 0.21)

        return count
        
    def horas_manoObra_totales(self):
        bd = conexion()
        obras = bd.find()
        count = 0
        for ob in obras:
            count += ob['horas_mano_obra']

        return count

    def inicializar(self):
        bd = conexion()
        if(bd.find().count() == 0):
            misObras = Obras()
            ikea = Obra("Ikea", 200500, "Obra realizada en Málaga", True, "Transferencia", "2000m2 de cubierta sandwich", 200)
            leroy = Obra("Leroy", 589663, "Obra realizada en Sevilla", False, "Tarjeta de crédito", "5 Fachada sandwich y 10 cubiertas deck", 600)
            nevada = Obra("Centro comercial Nevada", 8966524, "Obra realizada en Granada", True, "PayPal", "Suelo laminado y cubierta deck", 1200)
            plazaMayor = Obra("Complejo Plaza Mayor", 99966524, "Obra realizada en Málaga", True, "Transferencia", "199925 m2 de azulejos laminados y 859658m2 cubiertas con lucesnarios", 1800)

            misObras.add(ikea)
            misObras.add(leroy)
            misObras.add(nevada)
            misObras.add(plazaMayor)
            return True
        else:
            return False
