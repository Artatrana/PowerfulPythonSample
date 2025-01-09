# Inventory Management System with Python

def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("1. Add new item")
    print("2. Update stock")
    print("3. View inventory")
    print("4. Search for an item")
    print("5. Exit")

def add_item(inventory):
    name = input("Enter item name: ").strip()

    if name in inventory:
        print("Item already exists. Use 'Update stock' to change the quantity.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"quantity": quantity, "price":price}
        print("Item added successfully!")
    except ValueError:
        print("Invalid input. Quantity and price must be numbers.")

def update_stock(inventory):
    name = input("Enter item name to update: ").strip()
    if name not in inventory:
        print("Item not found in inventory.")
        return
    try:
        quantity = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = quantity
        print("Stock updated successfully!")
    except ValueError:
        print("Invalid input. Quantity must be a number.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nInventory:")
    for i, (name, details) in enumerate(inventory.items(),1):
        print(f"{i}.{name} - Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def search_item(inventory):
    name = input("Enter item name to search: ").strip()
    if name in inventory:
        details = inventory[name]
        print(f"Found: {name} - Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

    else:
        print("Item not found.")

def main_exe():
    inventory = {}
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_stock(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_exe()








