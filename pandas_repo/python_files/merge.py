import pandas as pd
import numpy as np 

# Define two DataFrames
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': np.random.randn(4)
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'D', 'E'],
    'value': np.random.randn(4)
})

# Inner merge (default)
inner_merged = df1.merge(df2, on='key', suffixes=('_df1', '_df2'), how='inner')

# Outer merge
outer_merged = df1.merge(df2, on='key', suffixes=('_df1', '_df2'), how='outer')

# Left merge
left_merged = df1.merge(df2, on='key', suffixes=('_df1', '_df2'), how='left')

# Right merge
right_merged = df1.merge(df2, on='key', suffixes=('_df1', '_df2'), how='right')

print("Inner Merge:\n", inner_merged, "\n")
print("Outer Merge:\n", outer_merged, "\n")
print("Left Merge:\n", left_merged, "\n")
print("Right Merge:\n", right_merged, "\n")
