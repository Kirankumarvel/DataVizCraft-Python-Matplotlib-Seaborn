import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots in 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# First subplot - Sine Wave
ax1.plot(x, y1, color='blue')
ax1.set_title("Sine Wave")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")

# Second subplot - Cosine Wave
ax2.plot(x, y2, color='green')
ax2.set_title("Cosine Wave")
ax2.set_xlabel("x")
ax2.set_ylabel("cos(x)")

# Adjust layout
plt.suptitle("Subplot Layout Example")
plt.tight_layout()
plt.show()
