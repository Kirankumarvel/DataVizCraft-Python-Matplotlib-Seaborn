import matplotlib.pyplot as plt
import numpy as np

# Generate random data for three categories
np.random.seed(1)
math_scores = np.random.normal(70, 10, 100)
science_scores = np.random.normal(75, 12, 100)
english_scores = np.random.normal(65, 8, 100)

data = [math_scores, science_scores, english_scores]
labels = ['Math', 'Science', 'English']

# Create box plot
plt.boxplot(data, labels=labels, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'))

plt.title('Exam Score Distribution by Subject')
plt.ylabel('Scores')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
