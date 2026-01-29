# Builder: Builds a complex object step-by-step, avoiding large constructors and improving readability and flexibility.
# For example, when building a car, instead of creating one big constructor that takes all components at once,
# you assemble the car gradually—engine, wheels, interior—using small steps, and finally produce the complete car.
# from pyspark_sandbox.sql import SparkSession
#
# # Sprak Session builder is a real example
# spark = (
#     SparkSession.builder
#     .appName("TestApp")
#     .config("spark.executor.memory", "4g")
#     .config("spark.sql.shuffle.partitions", "200")
#     .getOrCreate()
# )
# 1. The product
class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.sunroof = None
        self.gps = None

    def __repr__(self):
        return f"Car(engine={self.engine}, color={self.color}, sunroof={self.sunroof}, gps={self.gps})"

# Step 2: The Builder
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine
        return self # Enables chaining

    def set_color(self, color):
        self.car.color = color
        return self

    def add_sunroof(self):
        self.car.sunroof = True
        return self

    def add_gps(self):
        self.car.gps = True
        return self

    def build(self):
        return self.car

# Step 3: Use the Builder
# car = (
#     CarBuilder()
#     .set_engine("V8")
#     .set_color("White")
#     .add_sunroof()
#     .add_gps()
#     .build()
# )
car = CarBuilder().add_gps().set_color("red").build()
print(car)
