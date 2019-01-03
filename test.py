# -*- coding: utf-8 -*-
from obra import Obras, Obra

misObras = Obras()

# Test para añadir una obra individual
def test_add():
    prueba = Obra("prueba", 1234, "obra de prueba", False, "Transferencia", "Nada", 120)
    resultado = misObras.add(prueba)
    assert resultado == True
    misObras.delete_all()

# Test para buscar una obra determinada
def test_buscar_obra():
    misObras.inicializar()
    for o in misObras.buscar_obra("Ikea"):
        assert o['nombre'] == "Ikea"
    
    assert misObras.buscar_obra("No Existe") == None
    misObras.delete_all()

# Test para eliminar todos los datos
def test_delete_all():
    misObras.inicializar()
    assert misObras.delete_all() == None

# Test para el contador de obras en la BD
def test_size():
    misObras.inicializar()
    assert misObras.size_obras() == 4
    misObras.delete_all()

# Test para el gasto total de obras sin IVA
def test_gasto_total_obras_sinIVA():
    misObras.inicializar()
    assert misObras.gasto_total_obras_sinIVA() == 109723211
    misObras.delete_all()


# Test para el gasto total de obras con IVA
def test_gasto_total_obras_conIVA():
    misObras.inicializar()
    assert misObras.gasto_total_obras_conIVA() == 132765085.30999999
    misObras.delete_all()


# Test para el numero de horas de mano de obra totales
# de todas las obras gestionadas
def test_horas_manoObra_totales():
    misObras.inicializar()
    assert misObras.horas_manoObra_totales() == 3800
    misObras.delete_all()

# Test para inicializar datos de prueba
def test_inicializar():
    assert misObras.inicializar() == True
    assert misObras.inicializar() == False
    misObras.delete_all()
    
