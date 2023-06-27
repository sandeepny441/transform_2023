import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Generate random categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000)})

# count plot 
sns.countplot(x='Animal', data=df)
plt.title('Countplot')
plt.show()

# Bar plot 
sns.barplot(x='Animal', y=df.groupby('Animal').size(), data=df)
plt.title('Bar Plot')
plt.show()


# Pie chart 
df['Animal'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

# Histogram
df['Animal'].value_counts().plot(kind='bar')
plt.title('Histogram')
plt.show()

