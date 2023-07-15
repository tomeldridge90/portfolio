import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set a theme for seaborn
sns.set_theme(style='dark')

# Create datasets
data_bar = {'Apples': 20, 'Bananas': 15, 'Cherries': 25, 'Dates': 10}
data_pie = [15, 30, 45, 10]
labels_pie = ['Frogs', 'Hogs', 'Dogs', 'Logs']
data_line = np.cumsum(np.random.randn(1000,1))
data_scatter = np.random.randn(50, 2)
data_hist = np.random.randn(100)
data_box = [np.random.randn(100), 5 * np.random.rand(100) - 2]

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 15))  # 3 rows, 2 columns

# Create a bar chart
axs[0, 0].set_facecolor('black')
axs[0, 0].bar(data_bar.keys(), data_bar.values(), color='blue')
axs[0, 0].set_title('Fruit Count', color='white')
axs[0, 0].set_xlabel('Fruit', color='white')
axs[0, 0].set_ylabel('Count', color='white')
axs[0, 0].tick_params(colors='white')
axs[0, 0].spines['top'].set_visible(False)
axs[0, 0].spines['right'].set_visible(False)


def style_plot(ax):
    ax.set_facecolor('black')
    ax.tick_params(colors='white')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_color('white')


# Create a pie chart
axs[0, 1].pie(data_pie, labels=labels_pie, autopct='%1.1f%%')
axs[0, 1].set_title('Animal Distribution')
style_plot(axs[0, 1])


# Create a line plot
axs[1, 0].plot(data_line)
axs[1, 0].set_title('Cumulative Sum')
style_plot(axs[1, 0])

# Create a scatter plot
axs[1, 1].scatter(data_scatter[:, 0], data_scatter[:, 1])
axs[1, 1].set_title('Random Scatter')
style_plot(axs[1, 1])

# Create a histogram
axs[2, 0].hist(data_hist, bins=20)
axs[2, 0].set_title('Random Histogram')

# Create a box plot
axs[2, 1].boxplot(data_box, vert=False)
axs[2, 1].set_title('Random Boxplot')

# Tweak layout for aesthetics
fig.tight_layout()
fig.set_facecolor('black')

# Adjust the space between plots
plt.subplots_adjust(wspace=0.4, hspace=0.6)

# Display the charts
plt.show()
