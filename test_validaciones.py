import unittest

from softmarket.modelos import ItemFactura


class TestValidaciones(unittest.TestCase):
    def test_cantidad_negativa_lanza_error(self):
        with self.assertRaises(ValueError):
            ItemFactura("Licencia", 100000, -1)

    def test_precio_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            ItemFactura("Licencia", -5, 1)


if __name__ == "__main__":
    unittest.main()
