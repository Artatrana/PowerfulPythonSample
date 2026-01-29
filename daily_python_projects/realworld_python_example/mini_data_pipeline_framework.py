# Build a mini data pipeline framework

# * Read data from multiple sources
# * Applies transformations (filters, aggregations)
# * Writes results to a target (CSV / JSON)
# * Supoort plugable steps and reuseable pipelines
# * Include logging, error handling, progress reporting
#
# Think of it like a mini Airflow / Pandas pipeline, suitable for a senior Python engineer demo.

import csv
import json
from functools import wraps
from typing import Callable, Iterable, List, Any, Dict
import logging
from contextlib import contextmanager

# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------------------
# Context Manager for Safe File Handling
# -------------------------------
@contextmanager
def open_file(path: str, mode: str):
    try:
        f = open(path, mode, newline='')
        yield f
    finally:
        f.close()

# -------------------------------
# Data Source Classes
# -------------------------------
class DataSource:
    """Abstract Base Class for all data sources"""
    def read(self) -> Iterable[Dict[str, Any]]:
        raise NotImplementedError

class CSVSource(DataSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> Iterable[Dict[str, Any]]:
        logger.info(f"Reading CSV data from {self.filepath}")
        with open_file(self.filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row

class JSONSource(DataSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> Iterable[Dict[str, Any]]:
        logger.info(f"Reading JSON data from {self.filepath}")
        with open_file(self.filepath, 'r') as f:
            data = json.load(f)
            for row in data:
                yield row

# -------------------------------
# Transform Step Decorator
# -------------------------------
def transform_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting transformation: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Completed transformation: {func.__name__}")
        return result
    return wrapper

# -------------------------------
# Sample Transformations
# -------------------------------
@transform_step
def filter_data(data: Iterable[Dict[str, Any]], column: str, value: Any) -> Iterable[Dict[str, Any]]:
    for row in data:
        if row.get(column) == value:
            yield row

@transform_step
def aggregate_sum(data: Iterable[Dict[str, Any]], column: str) -> Dict[Any, float]:
    result = {}
    for row in data:
        key = row.get(column)
        result[key] = result.get(key, 0) + float(row.get('amount', 0))
    return result

# -------------------------------
# Data Sink
# -------------------------------
class DataSink:
    def write(self, data: Any):
        raise NotImplementedError

class CSVSink(DataSink):
    def __init__(self, filepath: str, fieldnames: List[str]):
        self.filepath = filepath
        self.fieldnames = fieldnames

    def write(self, data: Iterable[Dict[str, Any]]):
        logger.info(f"Writing CSV data to {self.filepath}")
        with open_file(self.filepath, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

# -------------------------------
# Pipeline Class
# -------------------------------
class Pipeline:
    def __init__(self, source: DataSource, sink: DataSink):
        self.source = source
        self.sink = sink
        self.transforms: List[Callable[[Iterable[Dict[str, Any]]], Iterable[Dict[str, Any]]]] = []

    def add_transform(self, transform: Callable[[Iterable[Dict[str, Any]]], Iterable[Dict[str, Any]]]):
        self.transforms.append(transform)

    def run(self):
        data = self.source.read()
        for transform in self.transforms:
            data = transform(data)
        self.sink.write(data)

# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    # Source
    csv_source = CSVSource("data/sales.csv")

    # Sink
    csv_sink = CSVSink("data/filtered_sales.csv", fieldnames=["order_id", "customer_id", "region", "amount", "order_date", "customer_name", "quantity", "product"])

    # Pipeline
    pipeline = Pipeline(csv_source, csv_sink)
    pipeline.add_transform(lambda d: filter_data(d, column="region", value="US"))
    pipeline.run()
