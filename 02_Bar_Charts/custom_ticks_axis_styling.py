import matplotlib.pyplot as plt

# Sample data: Website visitors per hour
hours = list(range(0, 24))
visitors = [30, 25, 20, 18, 15, 20, 35, 60, 80, 100, 120, 140, 160, 150, 130, 110, 90, 80, 60, 50, 40, 35, 30, 25]

plt.bar(hours, visitors, color='coral')

plt.title('Hourly Website Visitors')
plt.xlabel('Hour of Day')
plt.ylabel('Visitors')

# Customize x-axis ticks
plt.xticks(ticks=range(0, 24, 2), labels=[f'{h}:00' for h in range(0, 24, 2)], rotation=45)

# Set y-axis range
plt.ylim(0, 200)

# Styling
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
