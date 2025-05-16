
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data
data1 = {'Category': ['A', 'B', 'C'], 'Values': [10, 20, 15]}
data2 = {'Category': ['X', 'Y', 'Z'], 'Values': [5, 25, 10]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Create first plot
fig1, ax1 = plt.subplots()
sns.barplot(x='Category', y='Values', data=df1, palette='Blues', ax=ax1)
ax1.set_title("First Plot")
ax1.set_xlabel("First Plot X-axis")
ax1.set_ylabel("First Plot Y-axis")

# Create second plot
fig2, ax2 = plt.subplots()
sns.barplot(x='Category', y='Values', data=df2, palette='Greens', ax=ax2)
ax2.set_title("Second Plot")
ax2.set_xlabel("Second Plot X-axis")
ax2.set_ylabel("Second Plot Y-axis")

plt.show()
