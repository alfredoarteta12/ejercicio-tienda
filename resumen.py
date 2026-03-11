def resumen_ventas(ventas):

    total = 0

    print("\nResumen de ventas")
    print("------------------")

    for venta in ventas:
        producto = venta["producto"]
        precio = venta["precio"]
        cantidad = venta["cantidad"]
        subtotal = precio * cantidad

        print(f"Producto: {producto} , Cantidad: {cantidad} ")

        total += subtotal

    print("------------------")
    print(f"Total vendido: {total}")