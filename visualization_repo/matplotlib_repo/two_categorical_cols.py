import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn simplifies creating complex plots

# Generate random categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000),
    'Color': np.random.choice(['Red', 'Blue', 'Green', 'Yellow'], 1000),
})


# Grouped Bar Chart
grouped = df.groupby(['Animal', 'Color']).size().unstack()

grouped.plot(kind='bar', stacked=False)
plt.title('Grouped Bar Plot')
plt.xlabel('Animal')
plt.ylabel('Count')
plt.show()

# Stacked Bar plot 
grouped.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Plot')
plt.xlabel('Animal')
plt.ylabel('Count')
plt.show()


# Heatmap
sns.heatmap(grouped, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap')
plt.show()

