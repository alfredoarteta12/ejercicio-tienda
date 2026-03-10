ventas = []



producto = input("ingrese nombre del producto: ")
precio = int(input("ingrese precio del producto: "))
cantidad = int(input("ingrese cantidad del producto: "))

def registrar_venta():
    venta = {"producto": producto, "precio": precio, "cantidad": cantidad}
    ventas.append(venta)

valor_venta = precio * cantidad
print(f"el valor de la venta es : {valor_venta}")

registrar_nueva_venta = input("desea registar nueva venta si/no:")
while registrar_nueva_venta.lower() == "si":
    producto = input("ingrese nombre del producto: ")
    precio = int(input("ingrese precio del producto: "))
    cantidad = int(input("ingrese cantidad del producto: "))
    registrar_venta()

    valor_venta = precio * cantidad
    print(f"el valor de la venta es : {valor_venta}")
    registrar_nueva_venta = input("desea registar nueva venta si/no:")


