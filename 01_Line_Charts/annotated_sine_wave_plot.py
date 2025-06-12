import numpy as np
import matplotlib.pyplot as plt

# Create sine wave data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label='Sine Wave', color='purple')

# Annotate the peak
max_index = np.argmax(y)
plt.annotate('Peak',
             xy=(x[max_index], y[max_index]),
             xytext=(x[max_index]+0.5, y[max_index]),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

plt.title('Annotated Sine Wave')
plt.xlabel('Angle [radians]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
