import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a strip plot
plt.figure(figsize=(8, 5))
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True, palette="Set2")
plt.title("Strip Plot of Total Bill per Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()
