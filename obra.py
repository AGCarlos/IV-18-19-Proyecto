# -*- coding: utf-8 -*-
#
# Clase Obra
# Se define una obra con su id, nombre, precio, descripción, si está activa, tipo de pago,
# materiales usados y horas de mano de obra.
# Autor: Francisco Miguel Toledo Aguilera
# 

class Obra:                
    def Nueva(self, i, n, p, d, a, tp, m, hmo):
        self.id = i
        self.nombre = n
        self.precio = p
        self.descripcion = d
        self.activa = a
        self.tipo_pago = tp
        self.materiales = m
        self.horas_mano_obra = hmo

    def __init__(self):
        self.id = -1
        self.nombre = " "
        self.precio = -1
        self.descripcion = " "
        self.activa = False
        self.tipo_pago = " "
        self.materiales = " "
        self.horas_mano_obra = -1
     
    def print_nombre(self):
        print (self.nombre)
         
    def print_precio(self):
        print (self.precio)

    def print_descripcion(self):
        print (self.descripcion)

    def print_activa(self):
        print (self.activa)

    def print_tipo_pago(self):
        print (self.tipo_pago)

    def print_materiales(self):
        print (self.materiales)

    def print_horas_mano_obra(self):
        print (self.horas_mano_obra)

    def precio_con_iva(self, t):
        iva = (self.precio*t) + self.precio
        return iva

#
# Clase ObraManager
# Sistema gestor de Obras (clase anterior)
# Se define una lista de obras
# Permite hacer: altas, bajas y borrado
# 

class ObraManager:
    def __init__(self):
        self.lista_obras = []

    def add_obra(self, obra):
        self.lista_obras.append(obra)

    def buscar_obra(self, obra_id):
        for ob in self.lista_obras:
            if ob.id == obra_id:
                return ob
            else:
                print("No se ha encontrado la obra")

    def delete_obra(self, obra_id):
        index = self.buscar_obra(obra_id)
        if index != None:
            self.lista_obras.remove(index)
            print("Obra borrada con exito")
        else:
            print("No se ha encontrado la obra a borrar")

    def num_obras(self):
        count = 0
        for ob in self.lista_obras:
            count +=1

        return count

    def gasto_total_obras_sinIVA(self):
        count = 0
        for ob in self.lista_obras:
            count += ob.precio

        return count

    def gasto_total_obras_conIVA(self):
        count = 0
        for ob in self.lista_obras:
            count += ob.precio_con_iva(0.21)

        return count
        
    def horas_manoObra_totales(self):
        count = 0
        for ob in self.lista_obras:
            count += ob.horas_mano_obra

        return count
