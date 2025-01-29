import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data
data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 15, 25]}
df = pd.DataFrame(data)

# Seaborn bar plot
sns.barplot(x='Category', y='Values', data=df, palette='viridis')
plt.title("Bar Plot Example")
plt.show()
