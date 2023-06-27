import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# Generate random data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Height': np.random.normal(150, 20, 1000),  # normal distribution
    'Weight': np.random.normal(70, 10, 1000),   # normal distribution
    'Gender': np.random.choice(['Male', 'Female'], 1000),
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], 1000),
})

# Scatter plot with colors and shapes
sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender', style='Location')
plt.title('Scatter Plot')
plt.show()

# Facet Grid 
g = sns.FacetGrid(df, col='Gender', row='Location')
g = g.map(plt.scatter, 'Height', 'Weight')
plt.show()


# Pair Grid
g = sns.PairGrid(df, hue='Gender', corner=True)  # corner=True for a half pairplot
g = g.map_lower(sns.scatterplot)
g = g.map_diag(sns.histplot)
g = g.add_legend()
plt.show()
