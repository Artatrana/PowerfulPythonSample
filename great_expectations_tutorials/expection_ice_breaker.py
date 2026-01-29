from tokenize import Number

import great_expectations as gx
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "user_id": [1, 2, 3, None],
    "age": [25, 30, -5, 40]
})

# 1. Create a Great Expectations context (in-memory)
context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="age", min_value=0, max_value=120
)

expectation2 = gx.expectations.ExpectColumnValuesToBeBetween(
    column="test",
    min_value=0,
    max_value=100
)

# 6. Validate the data
#Run and get the results!
validation_result = batch.validate(expectation)
print(validation_result)


