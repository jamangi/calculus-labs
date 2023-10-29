import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return (2*x**2 + 18) / x

def f_prime(x):
    return (2*x**2 - 18) / x**2

# Generate x values
x = np.linspace(-10, 10, 400)  # Avoid x = 0 for division by zero

# Calculate function and derivative values
y = f(x)
y_prime = f_prime(x)

# Create the plot
plt.figure(figsize=(10, 5))

# Plot the function
plt.plot(x, y, label='f(x) = (2x^2 + 18) / x', color='blue')

# Plot the derivative
plt.plot(x, y_prime, label="f'(x)", color='red')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Set y-axis limits for a better view
plt.ylim(-20, 40)

# Show the plot
plt.grid()
plt.title('Function and its Derivative')
plt.savefig('question_2.pdf')
plt.show()
