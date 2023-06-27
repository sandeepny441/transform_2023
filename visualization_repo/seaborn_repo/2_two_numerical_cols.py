import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Generate random numerical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({'A': np.random.randn(1000), 'B': np.random.randn(1000)})
 

# Scatter plot 
sns.scatterplot(data=df, x='A', y='B')
plt.title('Scatterplot')
plt.show()


# Line Plot 
sns.lineplot(data=df, x='A', y='B')
plt.title('Lineplot')
plt.show()


# Jointplot
sns.jointplot(data=df, x='A', y='B')
plt.show()


# Hexbin plot 
sns.jointplot(data=df, x='A', y='B', kind='hex')
plt.show()


# Pair plot 
sns.pairplot(df)
plt.show()
