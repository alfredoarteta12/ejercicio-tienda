ventas = []

def registrar_venta():
    ventas = []
    producto = input("ingrese nombre del producto: ")
    precio = int(input("ingrese precio del producto: "))
    cantidad = int(input("ingrese cantidad del producto: "))

    venta = {"producto": producto, "precio": precio, "cantidad": cantidad}
    ventas.append(venta)

    valor_venta = precio * cantidad
    print(f"el valor de la venta es : {valor_venta}")

registrar_venta()

registrar_nueva_venta = input("desea registar nueva venta si/no:")

while registrar_nueva_venta.lower() == "si":
    registrar_venta()
    registrar_nueva_venta = input("desea registar nueva venta si/no:")

total = 0
def resumen_ventas(ventas):
    print("Resumen de ventas:")

    for venta in ventas:
        print("producto:", venta["producto"])
        print("cantidad:", venta["cantidad"])


    

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]

print("Total vendido:", total)
print("Gracias por usar el programa de ventas.")