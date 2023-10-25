import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return 5 + np.log(4 * x**3 - 3)

def f_prime(x):
    return (12 * x**2) / (4 * x**3 - 3)

def tangent_line(x, x0):
    return f_prime(x0) * (x - x0) + f(x0)

# Create x values
x = np.linspace(1, 5, 400)  # Define the range for x values (avoiding x = 0)

# Calculate function values
y = f(x)
y_prime = f_prime(x)
y_tangent = tangent_line(x, 1)  # Tangent line at x0 = 1

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x)", color="blue")
plt.plot(x, y_prime, label="f'(x)", color="green")
plt.plot(x, y_tangent, label="Tangent line (x0=1)", color="red", linestyle="--")

# Highlight the point of tangency
plt.scatter(1, f(1), color="red")

# Add labels and legend
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

# Save the plot to a file
plt.savefig("tangent_line.png")

# Show the plot
plt.show()
