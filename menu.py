from registrar import register_sale
from resumen import sales_summary


def menu(sales):
     continuar = True
     while continuar:

          print(" 1: Agregar producto: ")
          print(" 2: Consultar productos: ")
          print("3 salir del programa")
     
          
          opcion = input("ingrese la opcion que desea realizar (1/3): ")

          if opcion == "1":
                    register_sale(sales)
                    
          elif opcion == "2":
                    sales_summary(sales)
          elif opcion == "3":
                    print("saliendo del programa")
                    continuar = False
               
          else:
                    print("opcion invalida")      

     

           







