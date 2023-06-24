import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan],
    'B': [5, 6, np.nan, 8],
})

print(df['A'].isnull().sum())  # prints: 2
print(df['A'].isnull().sum().sum())  # also prints: 2, because it's a single column

print(df.isnull().sum())  # prints the sum of null values in each column
print(df.isnull().sum().sum())  # prints the total number of null values in the DataFrame
