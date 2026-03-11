from registrar import registrar_venta
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

