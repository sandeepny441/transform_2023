import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'A': ['one', 'one', 'two', 'three'] * 3,
  'B': ['A', 'B', 'C'] * 4,
  'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
  'D': np.random.randn(12),
  'E': np.random.randn(12)
})

pd.crosstab(df.A, df.B)
