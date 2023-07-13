import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'A': [1, -1, -1, -999, 4, -999, -999, -999, 6, -1, -1],
  'B': ['a', 'b', 'b', 'c', 'd', 'MISSING', 'MISSING', 'MISSING', 'f', 'g', 'g']
})

print("Original DataFrame:")
print(df)

# Use replace
df['A'].replace(-999, None, inplace=True)
df['B'].replace('MISSING', None, inplace=True)

print("\nDataFrame after replacing values:")
print(df)
