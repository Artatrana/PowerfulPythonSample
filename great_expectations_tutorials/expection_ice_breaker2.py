import great_expectations as gx
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "user_id": [1, 2, 3, None],
    "age": [25, 30, -5, 40]
})

# 1. Create a Great Expectations context (in-memory)
context = gx.get_context()

# 2. Create an in-memory datasource
context.add_datasource(
    name="my_pandas_datasource",
    class_name="Datasource",
    execution_engine={
        "class_name": "PandasExecutionEngine"
    },
    data_connectors={
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"]
        }
    }
)

# 3. Create a batch from the DataFrame
batch_request = gx.core.batch.BatchRequest(
    datasource_name="my_pandas_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="my_dataframe",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "batch1"},
)

# 4. Get a validator
validator = context.get_validator(batch_request=batch_request)

# 5. Add expectations
validator.expect_column_values_to_not_be_null("user_id")
validator.expect_column_values_to_be_between("age", min_value=0, max_value=120)

# 6. Validate the data
results = validator.validate()
print(results)


