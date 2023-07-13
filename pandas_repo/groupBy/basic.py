import pandas as pd
import numpy as np

data = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
}

df = pd.DataFrame(data)


print(df.groupby('A').mean())

print(df.groupby(['A', 'B']).sum())

for name, group in df.groupby('A'):
    print(name)
    print(group)

grouped = df.groupby('A')

print(grouped.get_group('bar'))

print(df.groupby('A').agg(['mean', 'median', 'std']))

print(df.groupby('A').agg({'C': 'sum', 'D': 'mean'}))

print(df.groupby('A').filter(lambda x: x['C'].mean() > 0))

print(df.groupby('B').transform(lambda x: x - x.mean()))

print(df.groupby('A').apply(lambda x: x / x.sum()))

