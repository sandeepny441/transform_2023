import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'date': ['2023-07-01', '2023-07-02'],
  'New York_temperature': [30, 32],
  'New York_humidity': [80, 82],
  'Los Angeles_temperature': [35, 36],
  'Los Angeles_humidity': [78, 85]
})

print("Original DataFrame:")
print(df)

# Melt the DataFrame
df_melt = df.melt(id_vars='date')

print("\nMelted DataFrame:")
print(df_melt)
