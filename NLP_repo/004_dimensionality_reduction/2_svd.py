import numpy as np
import plotly.graph_objs as go
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Center the data by subtracting the mean
X_centered = X - X.mean(axis=0)

# Apply SVD
U, s, VT = np.linalg.svd(X_centered)

# Project data onto the first two principal components
X_svd = X_centered @ VT.T[:, :2]

# Create scatter plots
scatter_original = go.Scatter(x=X_centered[:, 0], y=X_centered[:, 1], mode='markers', marker=dict(color=y), name='Original Data')
scatter_svd = go.Scatter(x=X_svd[:, 0], y=X_svd[:, 1], mode='markers', marker=dict(color=y), name='SVD Transformed Data')

# Create a layout
layout = go.Layout(title='SVD: Original Data vs Transformed Data',
                   xaxis=dict(title='X'),
                   yaxis=dict(title='Y'))

# Combine the plots and display
fig = go.Figure(data=[scatter_original, scatter_svd], layout=layout)
fig.show()
