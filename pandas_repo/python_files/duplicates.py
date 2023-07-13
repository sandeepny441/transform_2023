import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7],
  'B': ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'g']
})

print("Original DataFrame:")
print(df)

# Use duplicated
print("\nDuplicated rows:")
print(df[df.duplicated()])

# Use drop_duplicates
print("\nDataFrame after dropping duplicates:")
print(df.drop_duplicates())
