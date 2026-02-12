import pandas as pd
from markdown_it.rules_core import inline


# df.shape
# df.columns
# df.index
# df.dtypes
# df.size
# df.ndim
# df.values
# df.axes

def avg_notnull(series: pd.Series, trim: float = 0.1) -> float:
    """
    Returns the mean of a pandas Series after trimming
    the lowest `trim` fraction and the highest `trim` fraction.
    """
    s_sorted = series.dropna().sort_values()
    size = len(s_sorted)

    # number of elements to trim from each side
    cut = int(size * trim)
    if cut == 0:
        return s_sorted.mean()

    trimmed = s_sorted.iloc[cut : size - cut]
    return trimmed.mean()

# Read CSV
employee_data = pd.read_csv("employee.csv")

# Calculate trimmed mean
trimmed_mean = round(avg_notnull(employee_data['salary'], 0.1), 2)
print(f"Trimmed mean of salary: {trimmed_mean}")

# Show rows with missing salary
print("Rows with missing salary:")
print(employee_data[employee_data['salary'].isnull()])

# Fill missing salary with trimmed mean
employee_data['salary'].fillna(trimmed_mean, inplace=True)

# Verify
print("Data after filling missing salary:")
print(employee_data)

