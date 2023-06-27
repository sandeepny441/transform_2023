import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt


# Generate random numerical and categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Weight': np.random.normal(60, 10, 1000),  # Weight of an animal
    'Age': np.random.normal(5, 2, 1000),  # Age of an animal
    'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000),  # Type of animal
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], 1000)  # Location of the animal
})

# Scatter plot 
sns.scatterplot(x='Weight', y='Age', hue='Animal', data=df)
plt.title('Scatterplot')
plt.show()


# Box plot 
sns.boxplot(x='Animal', y='Weight', hue='Location', data=df)
plt.title('Boxplot')
plt.show()


# Violin plot 
sns.violinplot(x='Animal', y='Weight', hue='Location', data=df)
plt.title('Violinplot')
plt.show()


# pair plot 
sns.pairplot(df, hue='Animal')
plt.show()
