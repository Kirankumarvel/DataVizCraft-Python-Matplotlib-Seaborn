import matplotlib.pyplot as plt

# Sample data: Morning vs Evening temperatures
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
morning_temp = [22, 23, 24, 22, 21, 20, 19]
evening_temp = [30, 31, 32, 30, 29, 28, 27]

plt.plot(days, morning_temp, marker='o', color='green', label='Morning Temp')
plt.plot(days, evening_temp, marker='s', color='orange', label='Evening Temp')

plt.title('Morning vs Evening Temperature')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
