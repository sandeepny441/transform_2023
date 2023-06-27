import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(size=1000)

#Histogram
plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Box plot
plt.boxplot(data)
# plt.boxplot(data, vert = False)
plt.title('Box plot')
plt.ylabel('Value')
plt.show()

# Density plot 
df = pd.DataFrame(data, columns=['Value'])
df['Value'].plot(kind='density')
plt.title('Density plot')
plt.xlabel('Value')
plt.show()

# Line plot 
plt.plot(df['value'])
plt.title('Line plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

