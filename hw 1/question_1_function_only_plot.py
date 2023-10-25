import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 5 + np.log(4 * x**3 - 3)

# Generate x values
x = np.linspace(1.0, 2.0, 400)  # Adjust the range as needed

# Calculate corresponding y values
y = f(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="$f(x) = 5 + \ln(4x^3 - 3)$", color='blue')

# Add labels and title
plt.xlabel('x', color='black')
plt.ylabel('f(x)', color='black')
plt.title('Plot of $f(x) = 5 + \ln(4x^3 - 3)$', color='black')

# Display the plot
plt.grid(True)
plt.legend()
plt.savefig('function_only_plot.png')
plt.show()
