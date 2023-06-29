import numpy as np
import plotly.graph_objs as go
from sklearn.datasets import load_iris
from sklearn.decomposition import TruncatedSVD

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Apply TruncatedSVD
svd = TruncatedSVD(n_components=2)
X_svd = svd.fit_transform(X)

# Create scatter plots
scatter_original = go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers', marker=dict(color=y), name='Original Data')
scatter_truncated_svd = go.Scatter(x=X_svd[:, 0], y=X_svd[:, 1], mode='markers', marker=dict(color=y), name='TruncatedSVD Transformed Data')

# Create a layout
layout = go.Layout(title='TruncatedSVD: Original Data vs Transformed Data',
                   xaxis=dict(title='X'),
                   yaxis=dict(title='Y'))

# Combine the plots and display
fig = go.Figure(data=[scatter_original, scatter_truncated_svd], layout=layout)
fig.show()
