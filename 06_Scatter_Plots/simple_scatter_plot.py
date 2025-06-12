import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(0)
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)

# Create scatter plot
plt.scatter(x, y, color='teal', edgecolors='black', alpha=0.7)
plt.title('Simple Scatter Plot: y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.tight_layout()
plt.show()
