import pandas as pd
import numpy as np

# 1. Create DataFrames
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df1 = pd.DataFrame(data1)

data2 = {'A': [3, 4, 5], 'D': [10, 11, 12]}
df2 = pd.DataFrame(data2)

print("Original DataFrame:")
print(df1)

# 2. Indexing and Selection
print("\nSelect a column:")
print(df1['A'])

print("\nSelect multiple columns:")
print(df1[['A', 'C']])

print("\nRow selection using loc:")
print(df1.loc[1])  # By label

print("\nRow selection using iloc:")
print(df1.iloc[1])  # By index

# 3. Filtering
print("\nFilter rows where A > 1:")
filtered_df = df1[df1['A'] > 1]
print(filtered_df)

# 4. Adding and Modifying Columns
df1['E'] = df1['A'] + df1['B']
print("\nDataFrame after adding a new column:")
print(df1)

# 5. Aggregations
print("\nColumn-wise sum:")
print(df1.sum())

print("\nGroup by and aggregation:")
grouped = df1.groupby('A').sum()
print(grouped)

# 6. Merge, Join, and Concatenation
merged_df = pd.merge(df1, df2, on='A', how='inner')
print("\nMerged DataFrame:")
print(merged_df)

concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated_df)

# 7. Reshaping
pivoted = df1.pivot_table(values='B', index='A', aggfunc=np.sum)
print("\nPivot Table:")
print(pivoted)

melted = pd.melt(df1, id_vars=['A'], value_vars=['B', 'C'])
print("\nMelted DataFrame:")
print(melted)

# 8. Handling Missing Data
df_with_nan = df1.copy()
df_with_nan.loc[1, 'B'] = np.nan
print("\nDataFrame with NaN:")
print(df_with_nan)

print("\nFill NaN with a value:")
print(df_with_nan.fillna(0))

print("\nDrop rows with NaN:")
print(df_with_nan.dropna())

# 9. File I/O
df1.to_csv('dataframe.csv', index=False)
print("\nDataFrame saved to 'dataframe.csv'")

df_from_csv = pd.read_csv('dataframe.csv')
print("\nLoaded DataFrame from CSV:")
print(df_from_csv)

# Read JSON file into a DataFrame
df = pd.read_json('file_path.json')

# Display the DataFrame
print(df)