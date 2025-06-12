import matplotlib.pyplot as plt

# Sample data: Monthly expenses
categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Utilities']
expenses = [1200, 450, 300, 150, 200]

plt.bar(categories, expenses, color='teal')

plt.title('Monthly Expenses')
plt.xlabel('Category')
plt.ylabel('Amount Spent ($)')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
