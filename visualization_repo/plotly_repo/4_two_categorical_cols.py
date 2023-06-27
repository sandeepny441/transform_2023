import pandas as pd
import numpy as np

import plotly.graph_objects as go

# Generate random categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Category1': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'Category2': np.random.choice(['X', 'Y', 'Z'], 1000)
})


# Grouped Bar Plot: 
grouped_counts = df.groupby('Category1')['Category2'].value_counts().unstack()

fig = go.Figure(data=[
    go.Bar(name=col, x=grouped_counts.index, y=grouped_counts[col]) for col in grouped_counts.columns
])
fig.update_layout(title='Grouped Bar Plot', xaxis_title='Category1', yaxis_title='Count', barmode='group')
fig.show()

# Stacked Bar Plot
fig = go.Figure(data=[
    go.Bar(name=col, x=grouped_counts.index, y=grouped_counts[col]) for col in grouped_counts.columns
])
fig.update_layout(title='Stacked Bar Plot', xaxis_title='Category1', yaxis_title='Count', barmode='stack')
fig.show()


# Heatmap
fig = go.Figure(data=[
    go.Bar(name=col, x=grouped_counts.index, y=grouped_counts[col]) for col in grouped_counts.columns
])
fig.update_layout(title='Stacked Bar Plot', xaxis_title='Category1', yaxis_title='Count', barmode='stack')
fig.show()

# Parallel Categories Diagram (Parallel Sets): 
import plotly.express as px

fig = px.parallel_categories(df, dimensions=['Category1', 'Category2'])
fig.update_layout(title='Parallel Categories Diagram')
fig.show()



