import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
df = pd.DataFrame({
    'Hours_Studied': np.random.uniform(1, 10, 100),
    'Score': np.random.normal(60, 10, 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
})

# Create advanced scatter plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Hours_Studied', y='Score', hue='Gender', style='Gender', palette='Set2')
plt.title('Exam Score vs Hours Studied')
plt.tight_layout()
plt.show()
