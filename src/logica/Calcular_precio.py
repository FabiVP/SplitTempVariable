class Producto:
    def __init__(self, precio, cantidad):
        self.precio = precio
        self.cantidad = cantidad

    def calcular_precio(self, descuento, impuesto):
        # Cálculo del subtotal
        subtotal = self.precio * self.cantidad
        # Cálculo del descuento total
        total_descuento = subtotal * descuento
        # Cálculo del impuesto total
        total_impuesto = subtotal * impuesto
        # Cálculo del precio final
        total = subtotal - total_descuento + total_impuesto

        return total


