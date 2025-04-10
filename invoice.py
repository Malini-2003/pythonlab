def generate_invoice(customer_name, product_name, price, quantity):
    total_amount = price * quantity  # Calculate total price

    print("******************** INVOICE ********************")
    print(f"Customer Name: {customer_name}")
    print(f"Product: {product_name}")
    print(f"Price per unit: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print("---------------------------------------------------")
    print(f"Total Amount: ${total_amount:.2f}")
    print("***************************************************")

customer_name = input("Enter the customer's name: ")
product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product: $"))
quantity = int(input("Enter the quantity of the product: "))

generate_invoice(customer_name, product_name, price, quantity)
