from obra import Obra

def print_info_completa(self):
    print ("Nombre: ", self.nombre, "\nDescripción: ", self.descripcion, "\nPrecio(+IVA): ", self.precio_con_iva(0.21), "\n¿Activa?: ", self.activa)

ikea = Obra("Ikea", 200500, "Obra realizada en Málaga", True)
print_info_completa(ikea)
print("\n")
leroy = Obra("Leroy", 589663, "Obra realizada en Sevilla", False)
print_info_completa(leroy)