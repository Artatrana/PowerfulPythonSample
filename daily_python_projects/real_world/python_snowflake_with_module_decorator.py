import snowflake.connector
import time
from functools import wraps

def execution_timer(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

def ensure_connection(func):
    """Decorator to ensure the Snowflake connection is active."""
    @wraps(func)
    def wrapper(conn, *args, **kwargs):
        if conn.is_closed():
            raise ConnectionError("Snowflake connection is not active.")
        return func(conn, *args, **kwargs)
    return wrapper

@execution_timer
@ensure_connection
def create_table(conn):
    """Create a sample table in Snowflake."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE OR REPLACE TABLE sample_table (
            id INT,
            name STRING,
            age INT
        )
    """)
    cursor.close()
    print("Table created successfully.")

@execution_timer
@ensure_connection
def insert_data(conn):
    """Insert sample data into the table."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sample_table (id, name, age) VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    """)
    cursor.close()
    print("Data inserted successfully.")

@execution_timer
@ensure_connection
def query_data(conn):
    """Query and print all data from the table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sample_table")
    rows = cursor.fetchall()
    cursor.close()
    print("Query results:")
    for row in rows:
        print(row)

@execution_timer
@ensure_connection
def update_data(conn):
    """Update data in the table."""
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE sample_table
        SET age = 28
        WHERE name = 'Bob'
    """)
    cursor.close()
    print("Data updated successfully.")

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

    try:
        create_table(conn)
        insert_data(conn)
        print("Before update:")
        query_data(conn)
        update_data(conn)
        print("After update:")
        query_data(conn)
    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
