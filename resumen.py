def sales_summary(sales):

    total = 0

    print("\nSales Summary")
    print("------------------")

    for sale in sales:
        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]
        subtotal = price * quantity

        print(f"Product: {product} , Quantity: {quantity}")

        total += subtotal

    print("------------------")
    print(f"Total sold: {total}")
    print("Thank you for using our program :>:")