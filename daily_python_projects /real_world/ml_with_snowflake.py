import snowflake.connector
import  pandas as pd
from sklearn.preprocessing import StandardScaler

# Connect to Snowflake
def data_connector():
    conn = snowflake.connector.connect(
        user='your_username',
        password='your_password',
        account='your_account',
        warehouse='your_warehouse',
        database='your_database',
        schema='your_schema'
    )

    # Query data
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, conn)

    # Close connection
    conn.close()

# Data Preprocessing: Clean and prepare the data for the ML model. This includes handling missing values,
# encoding categorical variables, normalizing numerical features, and feature engineering.
# Handle missing values
def data_processing(df: pd.DataFrame ):
    df.fillna(method='ffill',inplace=True)

    # One-hot encode categorical variable
    df = pd.get_dummies(df, columns=['categorical_column'])

    # Normalize numerical columns
    scaler = StandardScaler()
    df[['num_col1', 'num_col2']] = scaler.fit_transform(df[['num_col1', 'num_col2']])



