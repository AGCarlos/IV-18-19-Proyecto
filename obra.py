
class Obra:

    def __init__(self, n, p, d, a):
        self.nombre = n
        self.precio = p
        self.descripcion = d
        self.activa = a
     
    def print_nombre(self):
        print (self.nombre)
         
    def print_precio(self):
        print (self.precio)

    def print_descripcion(self):
        print (self.descripcion)

    def print_activa(self):
        print (self.activa)

    def precio_con_iva(self, t):
        iva = (self.precio*t) + self.precio
        return iva