import seaborn as sns
import matplotlib.pyplot as plt

# Load tips dataset
tips = sns.load_dataset("tips")

# Create facet grid: total_bill by day and sex
g = sns.FacetGrid(tips, col="sex", row="day", margin_titles=True)
g.map_dataframe(sns.histplot, x="total_bill", bins=15, color='teal')

# Add titles and layout
g.fig.suptitle("FacetGrid of Total Bill by Day and Sex", fontsize=16)
g.tight_layout()
plt.show()
