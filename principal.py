# -*- coding: utf-8 -*-
from obra import Obra, ObraManager

def print_info_completa(self):
    print("ID:" , str(self.id), "Nombre: ", self.nombre, "\nDescripción: ", self.descripcion, "\nPrecio(+IVA): ", str(self.precio), "\n¿Activa?: ", self.activa, "Tipo de pago: ", self.tipo_pago, "Materiales: ", self.materiales, "Horas de mano de obra: ", str(self.horas_mano_obra))

ikea = Obra()
ikea.Nueva(1, "Ikea", 200500, "Obra realizada en Málaga", True, "Transferencia", "2000m2 de cubierta sandwich", 200)
leroy = Obra()
leroy.Nueva(2, "Leroy", 589663, "Obra realizada en Sevilla", False, "Tarjeta de crédito", "5 Fachada sandwich y 10 cubiertas deck", 600)
nevada = Obra()
nevada.Nueva(3, "Centro comercial Nevada", 8966524, "Obra realizada en Granada", True, "PayPal", "Suelo laminado y cubierta deck", 1200)
plazaMayor = Obra()
plazaMayor.Nueva(3, "Complejo Plaza Mayor", 99966524, "Obra realizada en Málaga", True, "Transferencia", "199925 m2 de azulejos laminados y 859658m2 cubiertas con lucesnarios", 1200)

gestionObras = ObraManager()
gestionObras.add_obra(ikea)
gestionObras.add_obra(leroy)
gestionObras.add_obra(nevada)
gestionObras.add_obra(plazaMayor)

print("El número de obras es:", gestionObras.num_obras())
print("El gasto total obras sin IVA:", gestionObras.gasto_total_obras_sinIVA())
print("El gasto total obras con IVA:", gestionObras.gasto_total_obras_conIVA())
print("Las horas de mano de obra totales:", gestionObras.horas_manoObra_totales())
print("Precion con IVA de IKEA:", ikea.precio_con_iva(0.21))
