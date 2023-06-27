import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({
    'Numerical1': np.random.randn(1000),
    'Numerical2': np.random.randn(1000),
    'Category1': np.random.choice(['A', 'B', 'C', 'D'], 1000),
    'Category2': np.random.choice(['X', 'Y', 'Z'], 1000)
})

# scatter plot 
import plotly.express as px
fig = px.scatter(df, x='Numerical1', y='Numerical2', color='Category1', symbol='Category2')
fig.update_layout(title='Scatter Plot', xaxis_title='Numerical1', yaxis_title='Numerical2')
fig.show()

# facet Grid 
fig = px.scatter(df, x='Numerical1', y='Numerical2', color='Category1', facet_col='Category2')
fig.update_layout(title='Facet Grid')
fig.show()

# parallel coordinates plot 
fig = px.parallel_coordinates(df, color="Numerical1", labels={"Numerical1": "Num 1", "Numerical2": "Num 2",
                                                              "Category1": "Cat 1", "Category2": "Cat 2"},
                              color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=0)
fig.show()




