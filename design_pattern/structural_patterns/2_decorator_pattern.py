# 2. Decorator Pattern
# Intent: Add new behavior to an object dynamically without changing its original class
# Real‑World Analogy
# Ordering coffee and adding milk, sugar, or cream — each adds functionality without changing the coffee itself.
# Real Applications
# - Java I/O streams (BufferedInputStream, DataInputStream)
# - Django / Spring middleware
# When to Use
# - Avoid subclass explosion
# - Add optional features dynamically
# - Follow the Open‑Closed Principle

# Python Example of a Decorator Pattern
# Intent: Added a new behavior to an object dynamically without changing its original class

# 1> Base Component: ( Coffee): This is the code object that will be decorated
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Plain Coffee"

# 2️⃣ Base Decorator (Optional but clean design): This ensures all decorators follow the same interface.
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

# 3️⃣ Concrete Decorators
# Each decorator:
    # Wraps a Coffee
    # Adds behavior
    # Does not modify Coffee

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description()+ ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.5

    def description(self):
        return self.coffee.description() + ", Sugar"

class CreamDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 1.5

    def description(self):
        return self.coffee.description() + ", Cream"

# 4️⃣ Client Code (Dynamic Composition)
coffee = Coffee()
print(coffee.description(), "-> $", coffee.cost())

coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)
coffee = CreamDecorator(coffee)

print(coffee.description(), "-> $", coffee.cost())