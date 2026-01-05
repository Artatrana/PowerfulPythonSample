Pydantic

1. Define a Pydantic Model that represents the ideal schema of the data.
    - This include expected fields, their types, and any validation constraints (eg gt=0 for positive numbers)

2. Instantiate the model with raw input data(usually a dictionary or JSON-like structure).
    - Pydantic will automatically validate the data and coerce it into the correct python types (if possible).
    - if the data doesn't meet the model's requirements, Pydantic raise a ValidationError.

3. Pass the validated model object to functions or use it throughout the code base.
    - This ensure that every part of your program works with clean, type-safe, and logically valid data.

- Data Type check
- Data Validation like
- Data Format check like email
- Metadata with Annotation
- Fild data validation
