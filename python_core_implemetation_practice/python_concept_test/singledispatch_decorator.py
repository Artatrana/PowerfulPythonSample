# This program to see the functionalty of a singledipathch decorator
# Imagine you’re building:
# An API
# A logging system
# A data pipeline
# You want one function that can convert any data type into a string format, depending on its type.

from functools import singledispatch
import json
from datetime import datetime

@singledispatch
def serialize(data):
    """Default serializer (fallback)"""
    return TypeError(f"Unsupported type:{type(data)}")

@serialize.register
def _(data:int):
    return f"Integer value: {data}"

@serialize.register
def _(data: list):
    return ",".join(map(str, data))

@serialize.register
def _(data: dict):
    return json.dumps(data)

@serialize.register
def _(data: datetime):
    return data.isoformat()

# Use the same function for all tyeps
print(serialize(10))
print(serialize([1, 2, 3]))
print(serialize({"name": "Ramesh", "role": "Engineer"}))
print(serialize(datetime.now()))
print(serialize("test"))


