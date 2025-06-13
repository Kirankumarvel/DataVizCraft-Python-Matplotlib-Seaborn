import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a sample correlation matrix
np.random.seed(42)
data = pd.DataFrame({
    'Math': np.random.randint(60, 100, 10),
    'Science': np.random.randint(55, 95, 10),
    'English': np.random.randint(50, 90, 10),
    'History': np.random.randint(45, 85, 10)
})

correlation_matrix = data.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', linewidths=0.5, fmt=".2f")
plt.title('Subject Score Correlation Heatmap')
plt.tight_layout()
plt.show()
