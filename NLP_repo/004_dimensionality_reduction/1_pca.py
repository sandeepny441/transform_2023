import numpy as np
import plotly.graph_objs as go
from sklearn.decomposition import PCA

# Generate random data
np.random.seed(42)
X = np.random.rand(50, 2)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Create scatter plots
scatter_original = go.Scatter(x=X[:, 0], y=X[:, 1], mode='markers', name='Original Data')
scatter_pca = go.Scatter(x=X_pca[:, 0], y=X_pca[:, 1], mode='markers', name='PCA Transformed Data')

# Create a layout
layout = go.Layout(title='PCA: Original Data vs Transformed Data',
                   xaxis=dict(title='X'),
                   yaxis=dict(title='Y'))

# Combine the plots and display
fig = go.Figure(data=[scatter_original, scatter_pca], layout=layout)
fig.show()
