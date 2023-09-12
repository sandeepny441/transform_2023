import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  'B': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
})

print("Original DataFrame:")
print(df)

# Min-Max normalization
df['A'] = (df['A'] - df['A'].min()) / (df['A'].max() - df['A'].min())
df['B'] = (df['B'] - df['B'].min()) / (df['B'].max() - df['B'].min())

print("\nDataFrame after normalization:")
print(df)
