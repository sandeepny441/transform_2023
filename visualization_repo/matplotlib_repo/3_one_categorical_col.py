import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with a single categorical column
np.random.seed(0)  # for reproducible result
df = pd.DataFrame(np.random.choice(['Cat', 'Dog', 'Bird', 'Fish'], 1000), columns=['Animal'])


# Bar plo
df['Animal'].value_counts().plot(kind='bar')
plt.title('Bar Plot')
plt.xlabel('Animal')
plt.ylabel('Count')
plt.show()

#pie chart
df['Animal'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()

#Horizontal bar plot 
df['Animal'].value_counts().plot(kind='barh')
plt.title('Horizontal Bar Plot')
plt.xlabel('Count')
plt.ylabel('Animal')
plt.show()

