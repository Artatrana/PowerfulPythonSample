import snowflake.connector

def connect_to_snowflake(user, password, account, warehouse, database, schema):
    """Establish a connection to Snowflake."""
    return snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

def create_table(cursor):
    """Create a sample table in Snowflake."""
    cursor.execute("""
        CREATE OR REPLACE TABLE sample_table (
            id INT,
            name STRING,
            age INT
        )
    """)
    print("Table created successfully.")

def insert_data(cursor):
    """Insert sample data into the table."""
    cursor.execute("""
        INSERT INTO sample_table (id, name, age) VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    """)
    print("Data inserted successfully.")

def query_data(cursor):
    """Query and print all data from the table."""
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    print("Query results:")
    for row in rows:
        print(row)

def update_data(cursor):
    """Update data in the table."""
    cursor.execute("""
        UPDATE sample_table
        SET age = 28
        WHERE name = 'Bob'
    """)
    print("Data updated successfully.")

def main():
    # Connection parameters
    conn_params = {
        'user': 'your_username',
        'password': 'your_password',
        'account': 'your_account',
        'warehouse': 'your_warehouse',
        'database': 'your_database',
        'schema': 'your_schema'
    }

    # Connect to Snowflake
    conn = connect_to_snowflake(**conn_params)
    cursor = conn.cursor()

    try:
        create_table(cursor)
        insert_data(cursor)
        print("Before update:")
        query_data(cursor)
        update_data(cursor)
        print("After update:")
        query_data(cursor)
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
