import plotly.graph_objects as go
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import NMF

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a DataFrame for the original data
df_original = pd.DataFrame(data=X, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])
df_original['species'] = iris.target_names[y]

# Perform NMF
nmf = NMF(n_components=2)
X_nmf = nmf.fit_transform(X)

# Create a DataFrame for the NMF-transformed data
df_nmf = pd.DataFrame(data=X_nmf, columns=['NMF1', 'NMF2'])
df_nmf['species'] = iris.target_names[y]

# Create a Plotly scatter plot for the original data
fig1 = go.Figure()

for species in iris.target_names:
    data = df_original[df_original['species'] == species]
    fig1.add_trace(go.Scatter(x=data['Feature 1'], y=data['Feature 2'], mode='markers', name=species))

fig1.update_layout(title='Original Iris Dataset',
                   xaxis_title='Feature 1',
                   yaxis_title='Feature 2')
fig1.show()

# Create a Plotly scatter plot for the NMF-transformed data
fig2 = go.Figure()

for species in iris.target_names:
    data = df_nmf[df_nmf['species'] == species]
    fig2.add_trace(go.Scatter(x=data['NMF1'], y=data['NMF2'], mode='markers', name=species))

fig2.update_layout(title='NMF Visualization of the Iris Dataset',
                   xaxis_title='NMF Component 1',
                   yaxis_title='NMF Component 2')
fig2.show()
