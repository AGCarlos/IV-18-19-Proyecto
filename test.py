
from obra import Obra

nevada = Obra("Centro Comercial Nevada", 20, "Obra realizada en Granada", True)

def test_iva():
    assert nevada.precio_con_iva(0.21) == 24.2
