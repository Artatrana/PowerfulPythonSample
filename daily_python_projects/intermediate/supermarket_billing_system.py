# Project Description
# Create a command line program that simulates a basic billing system for a supermarket.
# The user can input items purchased (e.g., butter, eggs, etc), their prices, and quantities.
# The app will calculate the total bill, apply any applicable discounts, and display an itemized bill summary.
# This project focuses on loops, dictionaries, and arithmetic calculations.

def calculate_bill(items, tax_rate = 0.5, discount_threshold=100, discount_rate=0.10):
    discount_rate = 0.10
    subtotal = 0
    bill_details = []

    for item in items:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]
        total_price = price * quantity
        subtotal += total_price

        bill_details.append({"name": name, "price": price, "quantity": quantity, "total_price": total_price} )

    discount = subtotal * discount_rate if subtotal > discount_threshold else 0
    tax = (subtotal - discount) * tax_rate
    total = subtotal - discount + tax
    return subtotal, discount, tax, total, bill_details

def display_bill(subtotal, discount, tax, total, bill_details):
    print("\n--- Bill Summary ---")
    for item in bill_details:
        print(f"{item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['total_price']:.2f}")
        print(f"Subtotoal: ${subtotal:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Sales Tax (5%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print("\nThank you for shopping with us!")

print("Welcome to the Supermarket Billing Systems!")
items = []

try:
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        name = input("Name: ")
        price = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))
        items.append({"name":name, "price": price, "quantity": quantity})
        subtotal, discount, tax, total, bill_details = calculate_bill(items)
        display_bill(subtotal, discount, tax, total, bill_details)

except ValueError:
    print("Invalid input. Please enter numbers for price and quantity.")


