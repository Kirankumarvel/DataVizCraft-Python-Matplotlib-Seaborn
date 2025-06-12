import matplotlib.pyplot as plt
import numpy as np

# Generate the same data for comparison
np.random.seed(2)
math_scores = np.random.normal(70, 10, 100)
science_scores = np.random.normal(75, 12, 100)
english_scores = np.random.normal(65, 8, 100)

data = [math_scores, science_scores, english_scores]
labels = ['Math', 'Science', 'English']

# Create violin plot
plt.violinplot(data, showmeans=True, showmedians=True)

plt.title('Violin Plot of Exam Scores')
plt.xticks([1, 2, 3], labels)
plt.ylabel('Scores')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
