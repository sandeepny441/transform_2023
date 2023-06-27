import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


# Generate random categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000),
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], 1000)
})
 

# count plot 
sns.countplot(x='Animal', hue='Location', data=df)
plt.title('Countplot')
plt.show()

# corss tabulation with a heatmap 
cross_tab = pd.crosstab(df['Animal'], df['Location'])
sns.heatmap(cross_tab, annot=True, fmt='d')
plt.title('Heatmap of Cross-Tabulation')
plt.show()

# Bar plot 
sns.barplot(x='Animal', hue='Location', y=df.groupby(['Animal', 'Location']).size(), data=df)
plt.title('Bar Plot')
plt.show()

# Clustered Bar chart
cross_tab.plot(kind='bar', stacked=False)
plt.title('Clustered Bar Chart')
plt.show()


