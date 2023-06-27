import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with two columns
np.random.seed(0)  # for reproducible result
df = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B'])


# scatter plot 

plt.scatter(df['A'], df['B'])
plt.title('Scatter Plot')
plt.xlabel('A')
plt.ylabel('B')
plt.show()


# line plot 

plt.plot(df['A'], df['B'])
plt.title('Line Plot')
plt.xlabel('A')
plt.ylabel('B')
plt.show()


# Hexbin plot 

plt.hexbin(df['A'], df['B'], gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
plt.title('Hexbin Plot')
plt.xlabel('A')
plt.ylabel('B')
plt.show()
