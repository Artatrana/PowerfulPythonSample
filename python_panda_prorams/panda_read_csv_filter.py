# Program 1: Read CSV & Basic Filtering
import pandas as pd

# load data
df_data = pd.read_csv('patients.csv')
older_patients = df_data[df_data["Age"] > 40]

print("Patients older than 40:")
print(older_patients)

avg_cost_city = df_data.groupby("City")["Cost"].mean().round(2).reset_index()
print(type(avg_cost_city))

print("Average treatment cost per city:")
print(avg_cost_city)

# Add a new column "CostCategory"
df_data["CostCategory"] = df_data["Cost"].apply(lambda x: "High" if x > 12000 else "Low")

print("Data with Cost Category:")
print(df_data)

df_sorted_data = df_data.sort_values(by="Cost", ascending=False).head(3)
print("Top 3 most expensive treatments:")
print(df_sorted_data)

# Save patient information for New York City only

df_data_ny = df_data[df_data["City"]=="New York"]
df_data_ny.to_csv("new_york_patients.csv", index=False)
