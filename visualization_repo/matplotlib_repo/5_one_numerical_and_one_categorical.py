import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Animal': np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000),
    'Weight': np.random.randn(1000)
})

# Box plot 
df.boxplot(by='Animal', column='Weight')
plt.title('Box Plot')
plt.suptitle('')  # Remove automatic title
plt.xlabel('Animal')
plt.ylabel('Weight')
plt.show()

# Violin plot 
sns.violinplot(x='Animal', y='Weight', data=df)
plt.title('Violin Plot')
plt.show()

# Bar plot 
df.groupby('Animal')['Weight'].mean().plot(kind='bar')
plt.title('Bar Plot')
plt.xlabel('Animal')
plt.ylabel('Mean Weight')
plt.show()


#Strip Plot 
sns.stripplot(x='Animal', y='Weight', data=df)
plt.title('Strip Plot')
plt.show()


