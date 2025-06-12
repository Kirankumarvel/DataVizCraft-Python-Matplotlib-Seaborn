import matplotlib.pyplot as plt

# Sample data: Monthly expenses
categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Utilities']
expenses = [1200, 450, 300, 150, 200]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create pie chart
plt.pie(expenses,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        shadow=True)

plt.title('Monthly Expenses Breakdown')
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle.
plt.tight_layout()

plt.show()
