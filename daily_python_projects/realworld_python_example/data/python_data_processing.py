# This code will demo the different python processing code of single piece of data
# We are going to write a simple decorator function to note timing of each function

import time
from functools import wraps

def time_it(label=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            name = label or func.__name__
            print(f"{name} took {end - start:.4f} seconds")
            return result
        return wrapper
    return decorator

# 2️⃣ Plain Python (csv → list of dicts)
import csv

@time_it("CSV -> List[Dict]")
def read_csv_dict(path):
    customers = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(row)
    return customers

data = read_csv_dict("data/customers-10000.csv")
# print(len(data))

# 3️⃣ Generator-Based Streaming
@time_it("CSV → Generator")
def process_with_generator(path):
    country_counts = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            c = row["Country"]
            country_counts[c] = country_counts.get(c, 0) + 1
    return country_counts

data_country_count = process_with_generator("data/customers-10000.csv")
#print(data_country_count)

# 4️⃣ Pandas (In-Memory)
import pandas as pd

@time_it("Pandas Full Read")
def panda_full(path):
    df= pd.read_csv(path)
    return df["Country"].value_counts()

# print(panda_full("data/customers-10000.csv"))

# 5️⃣ Pandas with Chunks
@time_it("Pandas with chunked")
def pandas_chunked(path, chunksize=1000):
    counts = {}
    for chunk in pd.read_csv(path,chunksize=chunksize):
        vc = chunk["Country"].value_counts()
        for key, value in vc.items():
            counts[key] = counts.get(key,0) + value

    return counts

# print(pandas_chunked("data/customers-10000.csv"))

# 6️⃣ Multiprocessing
from multiprocessing import Pool
from collections import Counter

def extract_country(row):
    return row["Country"]

@time_it("Multiprocessing")
def multiprocessing_count(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    with Pool(4) as p:
        countries = p.map(extract_country, rows)

    return Counter(countries)

# print(multiprocessing_count("data/customers-10000.csv"))

# import this
# print(this)

# 7️⃣ PySpark
from pyspark.sql  import SparkSession
@time_it("PySpark")
def spark_count(path):
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("test")
        .getOrCreate()
    )

    df = spark.read.option("header", True).csv(path)
    count_var = df.count()
    return count_var


#print(spark_count("data/customers-10000.csv"))

# 8️⃣ DuckDB (SQL on CSV)
import duckdb

@time_it("DuckDB SQL")
def duckdb_count(path):
    con = duckdb.connect()
    return con.execute( """select Country, COUNT(*)
            FROM read_csv_auto(?)
        GROUP BY Country
    """, [path]).fetchall()

print(duckdb_count("data/customers-10000.csv"))








