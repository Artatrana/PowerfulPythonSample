
class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value +=  1

    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f"Count={self.value}"

    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception("Invalid Type")


# count1 = Counter()
# count2 = Counter()
#
# count1.count_up()
# count2.count_up()
#
# print(count1)
# print(count1+1)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model} "

    def __repr__(self):
        return f"Car( make={self.make}, model={self.model}, year={self.year})"

my_car = Car("Toyota", "Corolla", 2021)

print(str(my_car))
print(repr(my_car))
