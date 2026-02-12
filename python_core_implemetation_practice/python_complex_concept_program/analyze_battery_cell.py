# Analyze battery cell data with validation, efficient streaming, and advanced processing
# ✅ Object-Oriented Programming (OOP)
# ✅ Decorators
# ✅ Generators
# ✅ Context Managers
# ✅ Functional programming (map, filter, reduce)
# ✅ Type hints with Pydantic validation
# ✅ Exception handling

from typing import Generator, List
from functools import reduce
from pydantic  import BaseModel, ValidationError
from contextlib import contextmanager

from interview_coding_practice.list_based_medium_questions import result


# 1. Define data model with Pydantic
class BatteryCell(BaseModel):
    voltage: float
    current: float
    temperature: float

    def power(self) -> float:
        return self.voltage * self.current

# 2. Context manager to simulate opening a battery data file
@contextmanager
def battery_data_sources():
    print("Opening battery data source...")
    data = [
        {"voltage": 3.7, "current": 1.5, "temperature": 25},
        {"voltage": 3.6, "current": 1.2, "temperature": 27},
        {"voltage": 3.8, "current": 2.0, "temperature": 24},
        {"voltage": 3.5, "current": -1.0, "temperature": 30}  # Discharge current
    ]
    yield data
    print("Closing battery data source...")

# 3. Generator to stream battery cells
def battery_cell_generator(data) -> Generator[BatteryCell, None, None]:
    for record in data:
        try:
            yield BatteryCell(**record)
        except ValidationError as e:
            print("Invalid record: " , e)

# Decorator to log function execution
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result

    return wrapper

# 5. Processing function with functional programming
@log_function
def analyze_battery_cells(cells: List[BatteryCell]):
    # Calculate total power using reduce
    total_power = reduce(
        lambda acc, cell: acc + cell.power(),
        filter(lambda c: c.current > 0 , cells),
        0
    )

    avg_temp = sum(map(lambda c: c.temperature, cells)) / len(cells)
    print(f"Total charging power: {total_power:.2f} W")
    print(f"Average temperature: {avg_temp:.2f} °C")

# 6. Main execution
if __name__ == "__main__":
    with battery_data_sources() as data:
        cells = list(battery_cell_generator(data))
        analyze_battery_cells(cells)



