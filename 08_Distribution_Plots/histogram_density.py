import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
iris = sns.load_dataset("iris")

# Create histogram and KDE plot
plt.figure(figsize=(8, 5))
sns.histplot(data=iris, x="sepal_length", kde=True, color="green", bins=15)
plt.title("Distribution of Sepal Length (with KDE)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
