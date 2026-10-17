"""Modelos de datos. Responsabilidad unica: representar la informacion."""
from dataclasses import dataclass, field


@dataclass
class ItemFactura:
    nombre: str
    precio: float
    cantidad: int

    def __post_init__(self):
        if self.precio < 0 or self.cantidad <= 0:
            raise ValueError("El precio no puede ser negativo y la cantidad debe ser mayor que 0")

    def subtotal(self):
        return self.precio * self.cantidad


@dataclass
class Cliente:
    nombre: str
    correo: str
    tipo: str = "normal"


@dataclass
class Factura:
    cliente: Cliente
    items: list = field(default_factory=list)
    descuento: float = 0.0

    def subtotal(self):
        return sum(item.subtotal() for item in self.items)

    def total(self):
        return self.subtotal() - self.descuento
