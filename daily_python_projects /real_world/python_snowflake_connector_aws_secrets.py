#Below is a Python script demonstrating how to connect to Snowflake by securely retrieving credentials from AWS Secrets Manager:

import boto3
import snowflake.connector
import json

'''
we are going to get below environment variable to authenticate AWS secret service
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=your_region
'''

# Function to retrieve secret from AWS Secrets Manager
def get_secret(secret_name, region_name ):
    """
    Fetches the secret from AWS Secrets Manager.

    :param secret_name: The name of the secret in AWS Secrets Manager
    :param region_name: The AWS region where the secret is stored
    :return: The secret's content as a dictionary
    """
    # Create a Secrets Manager client
    clint = boto3.client('secretsmanager', region_name=region_name)
    try:
        # Get the Secret value
        response = clint.get_secret_value(SecretId=secret_name)
        # Parse the secret
        if 'SecretString' in response:
            return json.loads(response['SecretString'])
        else:
            return json.loads(response['SecretBinary'].decode('utf-8'))

    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise

# Retrieve Snowflake credentials from AWS Secrets Manager
def connect_to_snowflake():
    """
    Connects to Snowflake using credentials from AWS Secrets Manager.
    """
    secret_name = "your-snowflake-secret-name"  # Replace with your secret name
    region_name = "your-region-name"  # Replace with your AWS region

    # Fetch secret
    secret = get_secret(secret_name, region_name)

    # Extract Snowflake credentials
    account = secret.get('account')
    user = secret.get('user')
    password = secret.get('password')
    database = secret.get('database')
    schema = secret.get('schema')
    warehouse = secret.get('warehouse')
    role = secret.get('role')
    # Connect to Snowflake
    try:
        connection = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            database=database,
            schema=schema,
            warehouse=warehouse,
            role=role
        )
        print("Successfully connected to Snowflake!")
        return connection
    except Exception as e:
        print(f"Failed to connect to Snowflake: {e}")
        raise


# Example usage
if __name__ == "__main__":
    conn = connect_to_snowflake()
    # Perform queries or operations here, e.g., conn.cursor().execute("SELECT 1")
    conn.close()

