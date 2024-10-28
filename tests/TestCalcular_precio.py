import unittest
from src.logica.Calcular_precio import Producto

class TestCalcularPrecio(unittest.TestCase):
    def test_precio_final(self):
        producto = Producto(precio=100, cantidad=2)  # Precio de 100 por unidad y cantidad 2
        descuento = 0.1  # 10% de descuento
        impuesto = 0.15  # 15% de impuesto
        precio_esperado = 207.0  # Calculado manualmente: 200 - 20 (10% descuento) + 30 (15% impuesto)
        precio_final = producto.calcular_precio(descuento, impuesto)
        self.assertEqual(precio_esperado,precio_final)

