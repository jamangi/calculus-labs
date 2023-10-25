import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(0, 5, 100)

# Calculate f(x) values
f_x = x + 2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, f_x, label="x + 2 relationship between x and f(x)", color='blue')

# Add labels and title
plt.xlabel('x', color='black')
plt.ylabel('f(x)', color='black')
plt.title('Plot of f(x) = x + 2', color='black')

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig('simple_plot.png')
plt.show()
