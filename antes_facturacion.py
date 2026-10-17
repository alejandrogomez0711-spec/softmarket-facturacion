# CODIGO LEGADO (el "caos"): todo mezclado en una sola clase.
class Facturacion:
    def crear_factura(self, cliente, tipo_cliente, items, correo):
        # 1. calcula el total
        total = 0
        for item in items:
            total = total + item["precio"] * item["cantidad"]

        # 2. calcula descuentos (hay que modificar este if cada vez que hay un tipo nuevo)
        if tipo_cliente == "normal":
            descuento = 0
        elif tipo_cliente == "frecuente":
            descuento = total * 0.10
        elif tipo_cliente == "mayorista":
            descuento = total * 0.20
        else:
            descuento = 0
        total_final = total - descuento

        # 3. imprime la factura
        print("FACTURA para", cliente)
        print("Total a pagar:", total_final)

        # 4. guarda en un archivo (acoplado a archivos de texto)
        archivo = open("facturas.txt", "a")
        archivo.write(cliente + ";" + str(total_final) + "\n")
        archivo.close()

        # 5. envia correo (acoplado a un unico canal)
        print("Enviando correo a", correo)
        return total_final


if __name__ == "__main__":
    f = Facturacion()
    f.crear_factura("Tienda La Esquina", "frecuente",
                    [{"precio": 100000, "cantidad": 2}, {"precio": 50000, "cantidad": 1}],
                    "tienda@correo.com")
