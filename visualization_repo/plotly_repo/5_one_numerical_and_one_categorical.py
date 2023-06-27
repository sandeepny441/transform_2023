import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Value': np.random.randn(1000),
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 1000)
})

# Box plot 
import plotly.express as px

fig = px.box(df, x='Category', y='Value')
fig.update_layout(title='Box Plot', xaxis_title='Category', yaxis_title='Value')
fig.show()

# violin plot 
fig = px.violin(df, x='Category', y='Value')
fig.update_layout(title='Violin Plot', xaxis_title='Category', yaxis_title='Value')
fig.show()

# Bar plot 
grouped_mean = df.groupby('Category')['Value'].mean()

fig = px.bar(x=grouped_mean.index, y=grouped_mean.values)
fig.update_layout(title='Bar Plot', xaxis_title='Category', yaxis_title='Mean Value')
fig.show()


# strip plot 
fig = px.strip(df, x='Category', y='Value')
fig.update_layout(title='Strip Plot', xaxis_title='Category', yaxis_title='Value')
fig.show()


