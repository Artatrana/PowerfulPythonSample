from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 🔹 Your SQL Self-Join use cases text
text = """
SQL Self-Join Duplicate-Rows Nth-Highest Hierarchical  Comparing-Rows Consecutive-Records Reconciliation  Detecting-Gaps
"""

# 🔹 Generate the word cloud
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='plasma',
    max_words=100
).generate(text)

# 🔹 Display the word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("SQL Self-Join Use Cases Word Cloud")
plt.show()
