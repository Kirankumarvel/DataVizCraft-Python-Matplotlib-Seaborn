import matplotlib.pyplot as plt

# Sample data: Temperature over a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [30, 32, 33, 31, 29, 28, 27]

plt.plot(days, temperature, marker='o', color='blue', linestyle='-', linewidth=2)

plt.title('Weekly Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()

plt.show()
