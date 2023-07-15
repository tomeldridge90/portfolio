import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Bar chart data
data_bar = {"Apple": 10, "Banana": 15, "Cherry": 7, "Date": 20}
labels_bar = list(data_bar.keys())

# Pie chart data
data_pie = [10, 15, 7, 20]
labels_pie = labels_bar

# Line plot data
data_line = {"Jan": 10, "Feb": 15, "Mar": 7, "Apr": 20, "May": 25, "Jun": 17, "Jul": 30, "Aug": 27, "Sep": 20, "Oct": 15, "Nov": 10, "Dec": 5}

# Scatter plot data
import numpy as np
np.random.seed(0)  # for reproducibility
data_scatter = np.random.rand(50, 2) * 100  # 50 points in 2D

# Histogram data
data_hist = np.random.randn(500)  # 500 data points from a normal distribution

# Box plot data
np.random.seed(0)  # for reproducibility
data_box = [np.random.randn(50) + i for i in range(5)]  # Five sets of data

# Create a subplot layout
fig = make_subplots(rows=3, cols=2)

# Create a bar chart
fig.add_trace(
    go.Bar(x=list(data_bar.keys()), y=list(data_bar.values()), marker_color='white', marker_line_color='black'),
    row=1, col=1
)

# Create a line plot
fig.add_trace(
    go.Scatter(x=list(data_line.keys()), y=list(data_line.values()), mode='lines', line_color='red'),
    row=2, col=1
)

# Create a scatter plot
fig.add_trace(
    go.Scatter(x=data_scatter[:, 0], y=data_scatter[:, 1], mode='markers', marker_color='blue'),
    row=2, col=2
)

# Create a histogram
fig.add_trace(
    go.Histogram(x=data_hist, nbinsx=20, marker_color='green'),
    row=3, col=1
)

# Create a box plot
fig.add_trace(
    go.Box(y=data_box, boxpoints='all', jitter=0.3, pointpos=-1.8),
    row=3, col=2
)

fig.update_layout(height=800, width=800, title_text="Fruit Dashboard")

fig.show()
