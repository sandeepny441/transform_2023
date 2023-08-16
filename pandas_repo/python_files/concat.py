import pandas as pd

# Define two DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7']
})

print('df1', df1)

print("=================================")

print('df2', df2)
# Concatenate the dataframes along rows
result_row = pd.concat([df1, df2])
print("Row-wise concatenation:\n", result_row)

# Concatenate the dataframes along columns
result_column = pd.concat([df1, df2], axis=1)
print("\nColumn-wise concatenation:\n", result_column)

# Concatenate with keys
result_keys = pd.concat([df1, df2], keys=['x', 'y'])
print("\nConcatenation with keys:\n", result_keys)

print("Hello world")