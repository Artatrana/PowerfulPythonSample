# 5. Prototype Pattern: Create new objects by copying an existing object ( the prototype) instead building it form scratch
# Clone an object instead of building it
# Use Prototype when
# Object creation is expensive( time and resource)
# You need many similar objects
# You want to avoid repeating initialization logic e.g. setting up a standard email account for employees and cloning it for new hires.
# You want runtime flexibility( clone any object) e.g. spawning multiple enemies in a video game by cloning a base enemy and tweaking attributes.

# Lets implement a python class to understand
# 1 - The product
import copy

class Car:
    def __init__(self, engine, color, sunroof, gps):
        self.engine = engine
        self.color = color
        self.sunroof = sunroof
        self.gps = gps

    def clone(self):
        return copy.deepcopy(self)  # deep copy to clone nested objects

    def __str__(self):
        return f"Car(engine={self.engine}, color={self.color}, sunroof={self.sunroof}, gps={self.gps})"

# Step 2: Use the Prototype
# Base prototype
base_car = Car("V8", "Red", True, True)

# Clone it
car1 = base_car.clone()
car1.color = "Blue"

car2 = base_car.clone()
car2.sunroof = False

print(base_car)
print(car1)
print(car2)

# Data engineering Analogy
base_df = spark.read.parquet("data.parquet")
df1 = base_df.clone().filter("age > 30")
df2 = base_df.clone().filter("salary > 500000")