import unittest

from softmarket.descuentos import Descuento
from softmarket.modelos import Cliente, ItemFactura
from softmarket.notificador import NotificadorMemoria
from softmarket.repositorio import RepositorioMemoria
from softmarket.servicio import ServicioFacturacion


class TestServicioFacturacion(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorioMemoria()
        self.notificador = NotificadorMemoria()
        self.servicio = ServicioFacturacion(self.repo, self.notificador)
        # Subtotal = 100000*2 + 50000*1 = 250000
        self.items = [ItemFactura("Licencia", 100000, 2), ItemFactura("Soporte", 50000, 1)]

    def _facturar(self, tipo):
        return self.servicio.crear_factura(Cliente("Ana", "ana@correo.com", tipo), self.items)

    def test_cliente_normal_sin_descuento(self):
        self.assertAlmostEqual(self._facturar("normal").total(), 250000)

    def test_cliente_frecuente_10_por_ciento(self):
        self.assertAlmostEqual(self._facturar("frecuente").total(), 225000)

    def test_cliente_mayorista_20_por_ciento(self):
        self.assertAlmostEqual(self._facturar("mayorista").total(), 200000)

    def test_tipo_desconocido_no_tiene_descuento(self):
        self.assertAlmostEqual(self._facturar("otro").total(), 250000)

    def test_la_factura_se_guarda(self):
        self._facturar("normal")
        self.assertEqual(len(self.repo.facturas), 1)

    def test_se_notifica_al_cliente(self):
        self._facturar("normal")
        self.assertEqual(self.notificador.mensajes[0][0], "ana@correo.com")

    def test_nuevo_descuento_sin_modificar_el_servicio(self):
        class DescuentoVIP(Descuento):
            def calcular(self, subtotal):
                return subtotal * 0.30

        servicio = ServicioFacturacion(self.repo, self.notificador, {"vip": DescuentoVIP()})
        factura = servicio.crear_factura(Cliente("Luis", "luis@correo.com", "vip"), self.items)
        self.assertAlmostEqual(factura.total(), 175000)


if __name__ == "__main__":
    unittest.main()
