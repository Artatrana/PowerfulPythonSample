class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Plain Coffee"


class MilkDecorator(Coffee):
    def cost(self):
        return self.cost() + 1

    def description(self):
        return self.description()+ ", Milk"

coffee = Coffee()
print(coffee.description(), "-> $", coffee.cost())

coffee = MilkDecorator()
print(coffee.description(), "-> $", coffee.cost())