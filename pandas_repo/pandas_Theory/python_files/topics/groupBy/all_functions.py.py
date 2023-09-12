import pandas as pd
import numpy as np

import pandas as pd

data = {'Store': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Product': ['Apple', 'Orange', 'Apple', 'Banana', 'Orange', 'Banana'], 
        'Revenue': [1200, 500, 700, 400, 800, 900]}

df = pd.DataFrame(data)

df.groupby('Store')['Revenue'].sum()
df.groupby(['Store', 'Product'])['Revenue'].sum()
df.groupby('Store')['Revenue'].agg(['sum', 'mean', 'max', 'min', 'count'])
df.groupby('Store').agg({'Revenue': ['sum', 'mean'], 'Product': 'count'})
df.groupby('Store')['Revenue'].apply(lambda x: (x - x.mean()) / x.std())
df.groupby('Store').filter(lambda x: x['Revenue'].sum() > 1000)
df.groupby('Store')['Revenue'].transform(lambda x: (x - x.mean()) / x.std())
df.pivot_table(values='Revenue', index='Store', columns='Product', aggfunc='sum')
for name, group in df.groupby('Store'):
    print(name)
    print(group)

