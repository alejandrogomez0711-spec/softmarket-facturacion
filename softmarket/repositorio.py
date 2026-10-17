"""Almacenamiento de facturas detras de una abstraccion (DIP e ISP)."""
from abc import ABC, abstractmethod


class RepositorioFacturas(ABC):
    @abstractmethod
    def guardar(self, factura):
        """Guarda una factura."""


class RepositorioArchivo(RepositorioFacturas):
    def __init__(self, ruta="facturas.txt"):
        self.ruta = ruta

    def guardar(self, factura):
        with open(self.ruta, "a", encoding="utf-8") as archivo:
            archivo.write(f"{factura.cliente.nombre};{factura.total():.2f}\n")


class RepositorioMemoria(RepositorioFacturas):
    """Util para pruebas: no escribe nada en el disco."""

    def __init__(self):
        self.facturas = []

    def guardar(self, factura):
        self.facturas.append(factura)
