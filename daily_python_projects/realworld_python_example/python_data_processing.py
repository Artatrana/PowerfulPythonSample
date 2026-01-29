# This code will demo the different python processing code of single piece of data
# We are going to write a simple decorator function to note timing of each function

import csv

# 1️⃣ Plain Python (csv module) — First Principles

def csv_module_load(path):
    customers = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(row)
    return  customers

# Some simple analysis
countries = {}
customers = csv_module_load("data/customers-10000.csv")
for c in customers:
    country = c["Country"]
    countries[country] = countries.get(country, 0) + 1

# print(countries)

#  2️⃣ Load as List of Tuples (Memory-Efficient, Structured)
def load_list_tuple(path):
    customers = []
    with open(path, newline="", encoding="utf-8" ) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            customers.append(row)
    return  header , customers


header, customers = load_list_tuple("data/customers-10000.csv")
country_idx = header.index("Country")

country_count = {}
for row in customers:
    country = row[country_idx]
    country_count[country] = country_count.get(country, 0) + 1
# print(country_count)

# 3️⃣ Generator-Based Processing (Streaming / Low Memory)
def read_customers(path):
    with open(path,newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield  row

country_counts = {}
for row in read_customers("data/customers-10000.csv"):
    country = row["Country"]
    country_counts[country] = country_count.get(country, 0) + 1
#print(country_counts)

# 4️⃣ Multiprocessing (CPU-bound work)
from multiprocessing import Pool

def process_row(row):
    return row["Country"]

def multiprocessing_data_load(path):
    with open("customers.csv", newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    with Pool(4) as p:
        countries = p.map(process_row, reader)

    from collections import Counter
    #print(Counter(countries))

    return (Counter(countries))

# print(multiprocessing_data_load("data/customers-10000.csv"))

# 5️⃣ Multithreading (I/O-bound)
# This is good for API call, Validation checks, External lookups

from concurrent.futures import ThreadPoolExecutor
def extract_email(row):
    return row["Email"]

def multithreading_load(path):

    with open(path,newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    with ThreadPoolExecutor(max_workers=8) as executor:
        emails = list(executor.map(extract_email, reader, ))
    return emails

email_list = multithreading_load("data/customers-10000.csv")
# print(len(email_list))
# print(email_list[:10])

#c6️⃣ Pandas (Most Common for Analysis)
import pandas as pd

df = pd.read_csv("data/customers-10000.csv")
# print(df.shape)
# print(df["Country"].count())
# print(df["Email"].isna().sum())
# print(df["Subscription Date"].min())
# print(df["Subscription Date"].max())

# 7️⃣ Chunked Pandas (Large Files)

country_counts = {}
for chunk in pd.read_csv("data/customers-10000.csv", chunksize=1000):
    counts = chunk["Country"].value_counts()

    for k, v in counts.items():
        country_counts[k] = country_count.get(k,0) + v
# 8️⃣ PySpark (Distributed Processing)
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.read.option("header", True).csv("data/customers-10000.csv")
print( df.count())
#df.groupBy("Country").count().show()
print(df.filter(df.Email.isNull()).count() )




