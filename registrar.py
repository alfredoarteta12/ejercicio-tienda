def registrar_venta(ventas):
    
    producto = input("Ingrese nombre del producto: ")
    precio = int(input("Ingrese precio del producto: "))
    cantidad = int(input("Ingrese cantidad del producto: "))

    venta = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    }

    ventas.append(venta)

    valor_venta = precio * cantidad
    print(f"El valor de la venta es: {valor_venta}")

    return ventas


def continuar_venta(ventas):

    registrar_nueva_venta = input("¿Desea registrar nueva venta? si/no: ")

    while registrar_nueva_venta.lower() == "si":
        registrar_venta(ventas)
        registrar_nueva_venta = input("¿Desea registrar nueva venta? si/no: ")

    return ventas