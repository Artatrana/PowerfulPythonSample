# Import polars library
import polars as pl

# Print header
print("Customer Data Filter & Exporter (Polars)")
print("=========================================\n")

# Read the CSV file
# (use pl.read_csv() to load 'customers.csv')
df = pl.read_csv('customers.csv')

# Display total customers loaded
print(f"Loading customer data from 'customers.csv'...")
print(f"Total customers loaded: {len(df)}\n")

# Print filter criteria message
print("Applying filters:")
print("- Purchase amount > $1000")
print("- Country: USA\n")

# Apply filters
# (filter for Purchase_Amount > 1000 AND Country == 'USA')
# (use .filter() method with pl.col() and & operator)
filtered_df = df.filter((pl.col('Purchase_Amount') > 1000) & (pl.col('Country') == 'USA'))

# Display filtered results
# (print the filtered DataFrame)
print("Filtered Results:")
print("-----------------")
print(filtered_df)
print()

# Calculate and display summary statistics
# (count of filtered customers)
print("Summary Statistics:")
print("-------------------")
print(f"Total customers found: {len(filtered_df)}")

# (average purchase amount of filtered customers)
average_purchase = filtered_df['Purchase_Amount'].mean()
print(f"Average purchase amount: ${average_purchase:.2f}\n")

# Export filtered data to new CSV file
# (use .write_csv() method)
filtered_df.write_csv('filtered_customers_polars.csv')

# Print completion message
print("Exporting to 'filtered_customers_polars.csv'...")
print("Export complete!")