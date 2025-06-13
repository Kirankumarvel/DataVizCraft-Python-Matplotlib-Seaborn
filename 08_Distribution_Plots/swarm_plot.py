import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a swarm plot
plt.figure(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex", palette="coolwarm")
plt.title("Swarm Plot of Total Bill by Day and Gender")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()
