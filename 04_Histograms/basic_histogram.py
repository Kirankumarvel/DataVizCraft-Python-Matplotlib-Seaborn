import matplotlib.pyplot as plt
import numpy as np

# Generate random data: e.g., ages of a group of people
ages = np.random.randint(18, 60, size=100)

# Create histogram
plt.hist(ages, bins=8, color='steelblue', edgecolor='black')

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
