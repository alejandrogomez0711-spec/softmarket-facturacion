from softmarket.modelos import Cliente, ItemFactura
from softmarket.notificador import NotificadorConsola
from softmarket.repositorio import RepositorioArchivo
from softmarket.servicio import ServicioFacturacion


def main():
    servicio = ServicioFacturacion(RepositorioArchivo("facturas.txt"), NotificadorConsola())
    cliente = Cliente("Tienda La Esquina", "tienda@correo.com", "frecuente")
    items = [ItemFactura("Licencia", 100000, 2), ItemFactura("Soporte", 50000, 1)]
    factura = servicio.crear_factura(cliente, items)
    print(f"Subtotal: ${factura.subtotal():,.2f}")
    print(f"Descuento: ${factura.descuento:,.2f}")
    print(f"Total: ${factura.total():,.2f}")


if __name__ == "__main__":
    main()
