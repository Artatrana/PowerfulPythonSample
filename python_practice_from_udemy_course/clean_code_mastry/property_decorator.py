# Getter and setter method
# Only Getter method
# Calculated attributes
# Deleter method

# class Car:
#     def __init__(self, speed ):
#         self._speed = speed
#
#     def get_speed(self):
#         return self._speed
#
#     def set_speed(self, value):
#         if value <= 0:
#             raise ValueError("Speed cann't be negative")
#         self._speed = value

# car = Car(50)
# print(car.get_speed())
# print(car._speed)
# car._speed = 60
# print(car.get_speed())
#
# car.set_speed(70)
# print(car.get_speed())

class Car:
    def __init__(self, speed ):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        if value <= 0:
            raise ValueError("Speed cann't be negative")
        self.__speed = value

car = Car(50)
print(car.speed)
#print(car.__speed)
car.__speed = 60
print(car.speed)
# print(car.speed)
car.speed = 70
print(car.speed)

#
# car.set_speed(70)
# print(car.get_speed())



# class Base:
#     def __init__(self, value):
#         self._value = value
#
#     @property
#     def value(self):
#         """Getter for value"""
#         print("Base class getter called")
#         return self._value
#
# class Derived(Base):
#
#     @Base.value.getter
#     def value(self):
#         """Enhhanced getter in subclass"""
#         print("Derived clsass getter called")
#         return super().value * 2
#
# obj = Derived(10)
# print( obj.value)

# import time
# class CurrencyCoverter:
#
#     def __init__(self):
#         self._exchange_rate = None
#         self._last_updated = None
#         self._chche_timeout = 5
#
#     @property
#     def exchange_rate(self):
#         """Getter that fetches the latest exchange rate if outdated"""
#         if self._exchange_rate is None:
#             print("Fetching initial exchange rate...")
#             self._exchange_rate = self._fetch_exchange_rate()
#             self._last_updated = time.time()
#         elif time.time() - self._last_updated > self._chche_timeout:
#             print("Exchange rate is outdate")
#             self._exchange_rate = self._fetch_exchange_rate()
#             self._last_updated = time.time()
#         return self._exchange_rate
#     @staticmethod
#     def _fetch_exchange_rate():
#         """Simulate API call to fetch exchange rate (e.g. USD to EUR)"""
#         print("Calling external API for exchange rate")
#         time.sleep(1)
#         return 0.85
#
# converter = CurrencyCoverter()
#
# print(converter.exchange_rate) # Fetch rate and caches it
# print(converter.exchange_rate) # Uses cache rate
# time.sleep(10)
#
# print(converter.exchange_rate) # Fetches new rate due to timeout
# print()


