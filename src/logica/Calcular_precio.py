class Producto:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def calcular_precio(self, descuento, impuesto):
        # Cálculo del subtotal
        total = self.precio * self.cantidad
        # Aplicar el descuento
        total = total - (total * descuento)
        # Aplicar el impuesto
        total = total + (total * impuesto)

        return total

