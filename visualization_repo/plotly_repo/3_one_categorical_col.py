import pandas as pd
import numpy as np

import plotly.graph_objects as go

# Generate random categorical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 1000)
})

# Bar plot 
counts = df['Category'].value_counts()

fig = go.Figure(data=[go.Bar(x=counts.index, y=counts.values)])
fig.update_layout(title='Bar Plot', xaxis_title='Category', yaxis_title='Count')
fig.show()


#pie chart 
counts = df['Category'].value_counts()

fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts.values)])
fig.update_layout(title='Pie Chart')
fig.show()


# donut chart
counts = df['Category'].value_counts()

fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts.values, hole=.3)])
fig.update_layout(title='Donut Chart')
fig.show()
