# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId


def conexion():
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['test']
    return db.obrasmta

#
# Clase Obras
# Sistema CRUD de Obras
# Autor: Francisco Miguel Toledo Aguilera
# 
class Obras():

    def add(self, nombre, precio, descripcion, activa, tipo_pago, materiales, horas_mano_obra):
        obras = conexion()
        suID = "None"
        suID = obras.insert_one({
            "nombre": nombre,
            "precio": precio,
            "descripcion": descripcion,
            "activa": activa,
            "tipo_pago": tipo_pago,
            "materiales": materiales,
            "horas_mano_obra": horas_mano_obra,
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
        respuesta = bd.find({"nombre": { "$regex": name } })
        result = list(respuesta)
        if(len(result) > 0):
            return result
        else:
            return None

    def update(self, id, nombre, precio, descripcion, activa, tipo_pago, materiales, horas_mano_obra):
        bd = conexion()
        resultado = bd.update_one(
            {
            '_id': ObjectId(id)
            }, 
            {
                '$set': {
                    "nombre": nombre,
                    "precio": precio,
                    "descripcion": descripcion,
                    "activa": activa,
                    "tipo_pago": tipo_pago,
                    "materiales": materiales,
                    "horas_mano_obra": horas_mano_obra,
                }
            })
        return resultado.modified_count

    def delete(self, id):
        bd = conexion()
        resultado = bd.delete_one(
            {
            '_id': ObjectId(id)
            })
        return resultado.deleted_count

    def delete_all(self):
        bd = conexion()
        return bd.drop()


    def size_obras(self):
        bd = conexion()
        return bd.count_documents({})

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
        if(bd.count_documents({}) == 0):
            misObras = Obras()
            misObras.add("Ikea", 200500, "Obra realizada en Málaga", True, "Transferencia", "2000m2 de cubierta sandwich", 200)
            misObras.add("Leroy", 589663, "Obra realizada en Sevilla", False, "Tarjeta de crédito", "5 Fachada sandwich y 10 cubiertas deck", 600)
            misObras.add("Centro comercial Nevada", 8966524, "Obra realizada en Granada", True, "PayPal", "Suelo laminado y cubierta deck", 1200)
            misObras.add("Complejo Plaza Mayor", 99966524, "Obra realizada en Málaga", True, "Transferencia", "199925 m2 de azulejos laminados y 859658m2 cubiertas con lucesnarios", 1800)

            return True
        else:
            return False


mis = Obras()

print(str(mis.buscar_obra("i")))