import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Generate random numerical and categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Weight': np.random.normal(60, 10, 1000),  # Weight of an animal
    'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000)  # Type of animal
})

# Box plot 
sns.boxplot(x='Animal', y='Weight', data=df)
plt.title('Boxplot')
plt.show()

# Violin plot 
sns.violinplot(x='Animal', y='Weight', data=df)
plt.title('Violinplot')
plt.show()

#Bar plot 
sns.barplot(x='Animal', y='Weight', data=df)
plt.title('Barplot')
plt.show()

#point plot 
sns.pointplot(x='Animal', y='Weight', data=df)
plt.title('Pointplot')
plt.show()

#strip plot 
sns.stripplot(x='Animal', y='Weight', data=df)
plt.title('Stripplot')
plt.show()

