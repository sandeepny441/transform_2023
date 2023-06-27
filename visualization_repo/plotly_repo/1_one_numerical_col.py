import pandas as pd
import numpy as np

# Generate random numerical data
np.random.seed(0)  # for reproducible result
df = pd.DataFrame({'Value': np.random.randn(1000)})

#Histogram 
import plotly.graph_objects as go

fig = go.Figure(data=[go.Histogram(x=df['Value'])])
fig.update_layout(title_text='Histogram')
fig.show()

# Box plot
fig = go.Figure(data=[go.Box(y=df['Value'], boxpoints='all', jitter=0.3, pointpos=-1.8 )])
fig.update_layout(title_text='Boxplot')
fig.show()

# Violin plot
fig = go.Figure(data=go.Violin(y=df['Value'], box_visible=True, line_color='black',
                               meanline_visible=True, fillcolor='lightseagreen', opacity=0.6))
fig.update_layout(title_text='Violin Plot')
fig.show()


# Cumulative Frequency Plot (Ogive)
import plotly.graph_objects as go
fig = go.Figure(data=[go.Histogram(x=df['Value'], cumulative_enabled=True)])
fig.update_layout(title_text='Cumulative Frequency Plot')
fig.show()

# Distplot
import plotly.figure_factory as ff
fig = ff.create_distplot([df['Value']], ['Value'], bin_size=0.2)
fig.update_layout(title_text='Distplot')
fig.show()

#Q-Q Plot (Quantile-Quantile plot):
import scipy.stats as stats
import plotly.graph_objects as go

# Generate theoretical quantiles and sample quantiles
theoretical_quantiles = np.sort(stats.norm.rvs(size=1000))
sample_quantiles = np.sort(df['Value'])

fig = go.Figure(data=go.Scatter(x=theoretical_quantiles, y=sample_quantiles, mode='markers'))
fig.update_layout(title='Normal Q-Q Plot',
                  xaxis_title='Theoretical Quantiles',
                  yaxis_title='Sample Quantiles')
fig.show()

