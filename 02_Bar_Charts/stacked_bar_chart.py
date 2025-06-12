import matplotlib.pyplot as plt

# Sample data: Tasks completed by two teams over a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
team_a = [5, 6, 7, 4, 6]
team_b = [3, 4, 6, 2, 3]

# Create stacked bar chart
plt.bar(days, team_a, label='Team A', color='skyblue')
plt.bar(days, team_b, bottom=team_a, label='Team B', color='lightgreen')

plt.title('Tasks Completed per Day by Teams')
plt.xlabel('Day')
plt.ylabel('Number of Tasks')
plt.legend()
plt.tight_layout()

plt.show()
