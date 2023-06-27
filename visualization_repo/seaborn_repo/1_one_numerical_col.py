import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Generate random numerical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({'Value': np.random.randn(1000)})

# Histogram
sns.histplot(df['Value'])
plt.title('Histogram')
plt.show()


# KDE 
sns.kdeplot(df['Value'])
plt.title('Kernel Density Estimate Plot')
plt.show()

# Box plot
sns.boxplot(x=df['Value'])
plt.title('Box Plot')
plt.show()

# Violin plot
sns.violinplot(x=df['Value'])
plt.title('Violin Plot')
plt.show()

# Dist plot 
sns.displot(df['Value'], kde=True)
plt.title('Dist Plot')
plt.show()


