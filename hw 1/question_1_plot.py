import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) and its derivative
def f(x):
    return 5 + np.log(4 * x**3 - 3)

def derivative(x):
    return 12 * x**2 / (4 * x**3 - 3)

# Create an array of x values
x = np.linspace(1, 2, 400)  # Exclude x=1 to avoid division by zero in the derivative

# Calculate the corresponding y values
y = f(x)
derivative_y = derivative(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = 5 + ln(4x^3 - 3)', color='blue')
plt.plot(x, derivative_y, label="f'(x)", color='red')
plt.axvline(x=1, color='gray', linestyle='--', label='x=1')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x) and its Derivative')
plt.legend()

# Save the plot as an image file in the current directory
plt.savefig('function_and_derivative_plot.png')

# Show the plot
plt.show()
