def register_sale(sales):

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

    return sales


def continue_sale(sales):

    register_new_sale = input("Do you want to register a new sale? yes/no: ")

    while register_new_sale.lower() == "yes":
        register_sale(sales)
        register_new_sale = input("Do you want to register a new sale? yes/no: ")

    return sales