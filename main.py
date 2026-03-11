ventas = []

def registrar_venta(ventas):
    
    producto = input("ingrese nombre del producto: ")
    precio = int(input("ingrese precio del producto: "))
    cantidad = int(input("ingrese cantidad del producto: "))

    venta = {"producto": producto, "precio": precio, "cantidad": cantidad}
    ventas.append(venta)

    valor_venta = precio * cantidad
    print(f"el valor de la venta es : {valor_venta}")
    return ventas

ventas = registrar_venta(ventas)

def continuar_venta(ventas):
    registrar_nueva_venta = input("desea registar nueva venta si/no:")
    
    while registrar_nueva_venta.lower() == "si":
        registrar_venta(ventas)
        registrar_nueva_venta = input("desea registar nueva venta si/no:")
        
        

continuar_venta(ventas)

def resumen_ventas(ventas):
    print("Resumen de ventas:")
    for venta in ventas:
        print(f"Producto: {venta['producto']}, , Cantidad: {venta['cantidad']}")
    total = 0
    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]
    print("Total vendido:", total)


resumen_ventas(ventas)
