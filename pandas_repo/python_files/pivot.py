import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'date': ['2023-07-01', '2023-07-01', '2023-07-02', '2023-07-02'],
  'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
  'temperature': [30, 35, 32, 36],
  'humidity': [80, 78, 82, 85]
})

print("Original DataFrame:")
print(df)

# Pivot the DataFrame
df_pivot = df.pivot(index='date', columns='city')

print("\nPivoted DataFrame:")
print(df_pivot)
