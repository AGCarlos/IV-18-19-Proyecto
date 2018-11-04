# coding=utf-8
# Funciones de testeo para la clase Obra y ObraManager

from obra import Obra, ObraManager

ikea = Obra()
ikea.Nueva(1, "Ikea", 200500, "Obra realizada en Málaga", True, "Transferencia", "2000m2 de cubierta sandwich", 200)
leroy = Obra()
leroy.Nueva(2, "Leroy", 589663, "Obra realizada en Sevilla", False, "Tarjeta de crédito", "5 Fachada sandwich y 10 cubiertas deck", 600)
nevada = Obra()
nevada.Nueva(3, "Centro comercial Nevada", 8966524, "Obra realizada en Granada", True, "PayPal", "Suelo laminado y cubierta deck", 1200)
plazaMayor = Obra()
plazaMayor.Nueva(3, "Complejo Plaza Mayor", 99966524, "Obra realizada en Málaga", True, "Transferencia", "199925 m2 de azulejos laminados y 859658m2 cubiertas con lucesnarios", 1800)

gestionObras = ObraManager()
gestionObras.add_obra(ikea)
gestionObras.add_obra(leroy)
gestionObras.add_obra(nevada)
gestionObras.add_obra(plazaMayor)

# Test de precio con iva para una obra individual
def test_iva():
    assert ikea.precio_con_iva(0.21) == 242605.0

# Test para el nombre de una obra individual
def test_print_nombre():
    assert ikea.nombre == "Ikea"

# Test para el numero de obras gestionadas
def test_num_obras():
    assert gestionObras.num_obras() == 4

# Test para el gasto total de obras sin IVA
def test_gasto_total_obras_sinIVA():
    assert gestionObras.gasto_total_obras_sinIVA() == 109723211

# Test para el gasto total de obras con IVA
def test_gasto_total_obras_conIVA():
    assert gestionObras.gasto_total_obras_conIVA() == 132765085.30999999

# Test para el numero de horas de mano de obra totales
# de todas las obras gestionadas
def test_horas_manoObra_totales():
    assert gestionObras.horas_manoObra_totales() == 3800