"""Envio de notificaciones detras de una abstraccion (DIP e ISP)."""
from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def enviar(self, destino, mensaje):
        """Envia un mensaje al destino indicado."""


class NotificadorConsola(Notificador):
    def enviar(self, destino, mensaje):
        print(f"[CORREO simulado a {destino}] {mensaje}")


class NotificadorMemoria(Notificador):
    """Util para pruebas: guarda los mensajes en una lista."""

    def __init__(self):
        self.mensajes = []

    def enviar(self, destino, mensaje):
        self.mensajes.append((destino, mensaje))
