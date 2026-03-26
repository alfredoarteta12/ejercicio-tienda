def register_sale(sales):
    operaciones = int(input("cuantos productos deseas registrar: "))
    for i in range(operaciones):
        product = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        sale = {
            "product": product,
            "price": price,
            "quantity": quantity
        }

        sales.append(sale)

        sale_value = price * quantity
        print(f"The value of the sale is: {sale_value}")
    

  