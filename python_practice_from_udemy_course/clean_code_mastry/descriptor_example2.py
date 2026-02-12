
class MeasurableAttributes:
    unit_conversions = {
        "temperature": {
            "C": lambda x: x,  # Base unit: Celsius
            "F": lambda x: (x * 9 / 5) + 32,
            "K": lambda x: x + 273.15
        },
        "distance": {
            "m": lambda x: x,  # Base unit: meters
            "km": lambda x: x / 1000,
            "mile": lambda x: x / 1609.34
        },
        "weight": {
            "kg": lambda x: x,  # Base unit: kilograms
            "lb": lambda x: x * 2.20462,
            "g": lambda x: x * 1000
        }
    }

    def __init__(self, category, default_unit):
        self.category = category
        self.default_unit = default_unit

    def __set_name__(self, owner, name):
        """Automatically assigns a unique attribute name per instance."""
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        """Retrieves the instance-specific value."""
        if instance is None:
            return self
        if not hasattr(instance, self.private_name):
            raise TypeError(f"self.private_name[1:] is not set yet.")
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        """Ensure type safety and stores the value in the instance."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.private_name[1:]} must be a number")
        print(f"Setting {self.private_name[1:]} to {value} {self.default_unit}")
        setattr(instance, self.private_name, value)

    def convert(self, instance, to_unit):
        """Converts the stored value to a different units."""
        if to_unit not in self.unit_conversions[self.category]:
            raise ValueError(f"Invalid unit: {to_unit}")
        #Retrive current value correctly
        base_value = self.__get__(instance, type(instance))
        return self.unit_conversions[self.category][to_unit](base_value)

class Temperature:
    value = MeasurableAttributes("temperature", "C")

    def __init__(self, initial_value):
        self.value = initial_value

    def to_fahrenheit(self):
        return Temperature.value.convert(self, "F")

    def to_kelvin(self):
        return Temperature.value.convert(self,"K")

    def describe(self):
        return f"Temperature: {self.value}°C | {self.to_fahrenheit()}°F | {self.to_kelvin()}K"

class Distance:
    value = MeasurableAttributes("distance", "m")

    def __init__(self, initial_value):
        self.value = initial_value

    def to_kilometers(self):
        return Distance.value.convert(self, "km")

    def to_miles(self):
        return Distance.value.convert(self, "mile")

    def describe(self):
        return  f"Distance: {self.value} meters | {self.to_kilometers()} km | {self.to_miles()} miles"

class Weight:
    value = MeasurableAttributes("weight", "kg")

    def __init__(self, initial_value):
        self.value = initial_value

    def to_pounds(self):
        return Weight.value.convert(self, "lb")

    def to_grams(self):
        return Weight.value.convert(self, "g")

    def describe(self):
        return f"Weight: {self.value} kg | {self.to_pounds()} lb | {self.to_grams()} g"

temp = Temperature(25)
print(temp.describe())

dist = Distance(1000)
print(dist.describe())

weight = Weight(70)
print(weight.describe())

print('-' * 30)
temp.value = 30
print(temp.describe())

dist.value = 5000
print(dist.describe())

weight.value = 90
print(weight.describe())


