import numpy as np
import plotly.graph_objs as go
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply t-SNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Define colorscale
colorscale = ['#EF553B', '#00CC96', '#AB63FA']

# Create scatter plots
scatter_original = go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers', marker=dict(color=[colorscale[i] for i in y]), name='Original Data')
scatter_tsne = go.Scatter(x=X_tsne[:, 0], y=X_tsne[:, 1], mode='markers', marker=dict(color=[colorscale[i] for i in y]), name='t-SNE Transformed Data')

# Create a layout
layout = go.Layout(title='t-SNE: Original Data vs Transformed Data',
                   xaxis=dict(title='X'),
                   yaxis=dict(title='Y'))

# Combine the plots and display
fig = go.Figure(data=[scatter_original, scatter_tsne], layout=layout)
fig.show()
