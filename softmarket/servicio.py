"""Caso de uso: crear una factura. Solo coordina; no sabe CÓMO se guarda ni se envia."""
from softmarket.descuentos import DESCUENTOS_POR_TIPO, SinDescuento
from softmarket.modelos import Factura


class ServicioFacturacion:
    def __init__(self, repositorio, notificador, descuentos=None):
        # Dependencias inyectadas (DIP)
        self.repositorio = repositorio
        self.notificador = notificador
        self.descuentos = descuentos if descuentos is not None else DESCUENTOS_POR_TIPO

    def crear_factura(self, cliente, items):
        factura = Factura(cliente, items)
        descuento = self.descuentos.get(cliente.tipo, SinDescuento())
        factura.descuento = descuento.calcular(factura.subtotal())
        self.repositorio.guardar(factura)
        self.notificador.enviar(cliente.correo, f"Su factura es por ${factura.total():,.2f}")
        return factura
