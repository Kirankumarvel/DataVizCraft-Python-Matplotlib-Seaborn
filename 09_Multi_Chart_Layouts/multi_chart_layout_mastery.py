import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.linspace(0, 10, 100)
y_line = np.sin(x)
y_scatter = y_line + np.random.normal(0, 0.1, size=100)
bars = [5, 7, 3, 4, 6]
categories = ['A', 'B', 'C', 'D', 'E']
hist_data = np.random.normal(loc=5, scale=2, size=1000)

# Create subplots grid
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
axs[0, 0].plot(x, y_line, color='blue')
axs[0, 0].set_title("Line Chart (Sine Wave)")

# Bar chart
axs[0, 1].bar(categories, bars, color='green')
axs[0, 1].set_title("Bar Chart (Categories)")

# Histogram
axs[1, 0].hist(hist_data, bins=20, color='orange')
axs[1, 0].set_title("Histogram (Normal Dist)")

# Scatter plot
axs[1, 1].scatter(x, y_scatter, alpha=0.7, color='purple')
axs[1, 1].set_title("Scatter Plot (Noisy Sine)")

# Layout adjustment
plt.suptitle("Multi-Type Charts in One Grid", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
