import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'date': ['2023-07-01', '2023-07-02', '2023-07-01', '2023-07-02'],
  'city': ['New York', 'New York', 'Los Angeles', 'Los Angeles'],
  'temperature': [30, 32, 35, 36],
  'humidity': [80, 82, 78, 85]
})

print("Original DataFrame:")
print(df)

# Stack the DataFrame
df_stack = df.stack()

print("\nStacked DataFrame:")
print(df_stack)

# Unstack the DataFrame
df_unstack = df_stack.unstack()

print("\nUnstacked DataFrame:")
print(df_unstack)
