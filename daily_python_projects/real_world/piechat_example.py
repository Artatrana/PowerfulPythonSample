import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
import textwrap

# Use a clean font family globally
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})

india = {
    "Cluster / System Configuration": ["Resource  Allocation","Dynamic allocation","Shuffle Service","GC Tuning","Serialization","Speculative Execution","Data Locality","Parallelism","Network and I/O"],
    "Application-Level": ["Predicate Pushdown","Column Pruning","Filter Early","Avoid UDFs","Avoid Collect","Avoid Shuffles","Avoid Wide Transformations","Broadcast Join","Repartition Wisely","Caching/Persisting","Window Functions Optimization","Skew Handling"],
    "Data Storage & Format": ["File Formats", "Compression", "Partitioning", "Bucketing", "File Size", "Schema Evolution & Merging" ],
    "Query execution technique":["Adaptive Query Execution (AQE)","Join Reordering","Dynamic Partition Pruning"]
}

categories = list(india.keys())
category_sizes = [len(items) for items in india.values()]

inner_labels = []
inner_sizes = []
inner_colors = []

# Choose a strong, colorblind-friendly palette with high contrast
base_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red

def lighten_color(color, amount=0.6):
    c = mcolors.to_rgb(color)
    return tuple(1 - (1 - x) * amount for x in c)

for i, (category, items) in enumerate(india.items()):
    inner_labels.extend(items)
    inner_sizes.extend([1] * len(items))
    inner_colors.extend([lighten_color(base_colors[i], 0.7)] * len(items))

fig, ax = plt.subplots(figsize=(6,6), dpi=150)  # high DPI for crispness

wedges_outer, _ = ax.pie(category_sizes, radius=1.3, colors=base_colors,
                         wedgeprops=dict(width=0.3, edgecolor='white'))

for wedge, label in zip(wedges_outer, categories):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 1.15
    y = np.sin(np.deg2rad(angle)) * 1.15

    rotation = angle
    if rotation > 90 and rotation < 270:
        rotation += 180

    ax.text(x, y, textwrap.fill(label, 15),
            rotation=rotation,
            rotation_mode='anchor',
            ha='center', va='center',
            fontsize=7, weight='bold',
            color='black')  # dark text for contrast

wedges_inner, _ = ax.pie(inner_sizes, radius=1.0, colors=inner_colors,
                         wedgeprops=dict(width=0.3, edgecolor='white'))

for wedge, label in zip(wedges_inner, inner_labels):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = np.cos(np.deg2rad(angle)) * 0.85
    y = np.sin(np.deg2rad(angle)) * 0.85

    rotation = angle
    if rotation > 90 and rotation < 270:
        rotation += 180

    wrapped_label = textwrap.fill(label, width=12)

    ax.text(x, y, wrapped_label,
            rotation=rotation,
            rotation_mode='anchor',
            ha='center', va='center',
            fontsize=6,
            color='black')  # dark text for clarity

# Add header text in the center
ax.text(0, 0, "Spark Optimization\nwith\nCADQ\nFramework",
        ha='center', va='center',
        fontsize=10, weight='bold', color='black')

plt.title("Spark Optimization", fontsize=12, weight='bold', pad=20, color='black')

plt.tight_layout()
plt.show()
