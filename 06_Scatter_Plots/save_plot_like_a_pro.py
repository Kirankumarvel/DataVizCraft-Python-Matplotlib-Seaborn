import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y, color='purple', linewidth=2)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.tight_layout()

# Save in high-quality formats
plt.savefig('sine_wave_plot.png', dpi=300)
plt.savefig('sine_wave_plot.pdf')
plt.show()
