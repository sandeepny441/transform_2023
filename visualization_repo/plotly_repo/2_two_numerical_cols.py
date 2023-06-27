import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Generate random numerical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Value1': np.random.randn(1000),
    'Value2': np.random.randn(1000)
})

# scatter plot
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=df['Value1'], y=df['Value2'], mode='markers'))
fig.update_layout(title='Scatter Plot', xaxis_title='Value1', yaxis_title='Value2')
fig.show()


#Histogram 
# Histogram for Value1
fig = go.Figure(data=[go.Histogram(x=df['Value1'])])
fig.update_layout(title_text='Histogram of Value1')
fig.show()

# Histogram for Value2
fig = go.Figure(data=[go.Histogram(x=df['Value2'])])
fig.update_layout(title_text='Histogram of Value2')
fig.show()


# 2D Histogram 
fig = go.Figure(data=go.Histogram2d(x=df['Value1'], y=df['Value2']))
fig.update_layout(title='2D Histogram', xaxis_title='Value1', yaxis_title='Value2')
fig.show()


# Boxplots
# Boxplot for Value1
fig = go.Figure(data=[go.Box(y=df['Value1'], name='Value1')])
fig.update_layout(title_text='Boxplot of Value1')
fig.show()
# Boxplot for Value2
fig = go.Figure(data=[go.Box(y=df['Value2'], name='Value2')])
fig.update_layout(title_text='Boxplot of Value2')
fig.show()

