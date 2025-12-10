class InventoryItems:
    """ A class to demonstrate operator overloading for inventory managements"""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItems(name={self.name}, quantity={self.quantity}) "

    # Arithmatic Operator
    def __add__(self, other):
        if isinstance(other, InventoryItems) and self.name== other.name:
            return InventoryItems(self.name, self.quantity + other.quantity)
        raise Exception("Cann't add item of different type.")

item1 = InventoryItems("Apple", 50)
item2 = InventoryItems("Apple", 30)
item3 = InventoryItems("Orange", 20)

result_add = item1 + item3
print(result_add)





