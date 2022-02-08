from datetime import datetime
from tokenize import Double


class Transaccion:

    VENTA=1
    ABASTECIMINETO=2
    def __init__(self, tipo: int, cantidad: int):
        self._tipo = tipo
        self._cantidad =cantidad
        self._time = datetime.now
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor == 1 or valor == 2:
            self._tipo = valor


class Libro:
    def __init__(self, isbn, titulo, precio_compra, precio_venta, cantidad_actual):
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_actual = cantidad_actual 
        self.transacciones = list()



class Tienda:
    def __init__(self, dinero_en_caja):
        self.dinero_en_caja = 1000000
        self.catalogo = dict()





if __name__ == "__main__":
    trans_1 = Transaccion(Transaccion.VENTA, 5)
    trans_2 = Transaccion(Transaccion.ABASTECIMINETO, 10)

    print(f"Cantidad t1: {trans_1.cantidad}")
    print(f"Cantidad t2: {trans_2.cantidad}")


