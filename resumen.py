ventas = []
def resumen_ventas(ventas):
    print("Resumen de ventas:")
    
    for venta in ventas:
      print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}")
          
    total = 0
    for venta in ventas:
      total += venta["precio"] * venta["cantidad"]

    print("Total vendido:", total)




