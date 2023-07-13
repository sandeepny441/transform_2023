df.loc[0]

df.loc[1:5]

df.loc[:, 'column']

df.loc[:, ['col1', 'col2']]

df.loc[df['column'] > 0]

mask = df['column'] > 0
df.loc[mask]

df.loc[1, 'column'] = 120

df.loc[0:2, 'column'] = 5