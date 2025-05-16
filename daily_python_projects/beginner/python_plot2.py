import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data
data1 = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 15]}
data2 = {'Category': ['X', 'Y', 'Z'], 'Values': [5, 25, 10]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Create first Seaborn bar plot
sns.barplot(x='Category', y='Values', data=df1, palette='Blues')
#sns.barplot(x='Category', y='Values', data=df2, palette='Greens')
plt.title("First Plot")  # This applies to the first plot
plt.xlabel("First Plot X-axis")
plt.ylabel("First Plot Y-axis")

# Create second Seaborn bar plot
sns.barplot(x='Category', y='Values', data=df2, palette='Greens')
plt.title("Second Plot")  # This applies to the second plot
plt.xlabel("Second Plot X-axis")
plt.ylabel("Second Plot Y-axis")

# Display plots
plt.show()
