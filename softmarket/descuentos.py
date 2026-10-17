"""Estrategias de descuento. Abierto a extension, cerrado a modificacion (OCP)."""
from abc import ABC, abstractmethod


class Descuento(ABC):
    @abstractmethod
    def calcular(self, subtotal):
        """Devuelve el valor (en dinero) a descontar."""


class SinDescuento(Descuento):
    def calcular(self, subtotal):
        return 0


class DescuentoFrecuente(Descuento):
    def calcular(self, subtotal):
        return subtotal * 0.10


class DescuentoMayorista(Descuento):
    def calcular(self, subtotal):
        return subtotal * 0.20


# Para un tipo nuevo: crear una clase nueva y agregar UNA linea aqui.
DESCUENTOS_POR_TIPO = {
    "normal": SinDescuento(),
    "frecuente": DescuentoFrecuente(),
    "mayorista": DescuentoMayorista(),
}
