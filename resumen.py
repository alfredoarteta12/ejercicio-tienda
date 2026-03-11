def resumen_ventas(ventas):
    print("Resumen de ventas:")
    total = 0
    for venta in ventas:
        print("producto:", venta["producto"])
        print("cantidad:", venta["cantidad"])


    

    for venta in ventas:
        total += venta["precio"] * venta["cantidad"]
    print("Total vendido:", total)