import snowflake.connector

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

# Create a cursor object
cursor = conn.cursor()

try:
    # Create a table
    cursor.execute("""
        CREATE OR REPLACE TABLE sample_table (
            id INT,
            name STRING,
            age INT
        )
    """)
    print("Table created successfully.")

    # Insert data
    cursor.execute("""
        INSERT INTO sample_table (id, name, age) VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    """)
    print("Data inserted successfully.")

    # Query data
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    print("Query results:")
    for row in rows:
        print(row)

    # Update data
    cursor.execute("""
        UPDATE sample_table
        SET age = 28
        WHERE name = 'Bob'
    """)
    print("Data updated successfully.")

    # Query again to check update
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    print("Updated results:")
    for row in rows:
        print(row)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
    print("Connection closed.")