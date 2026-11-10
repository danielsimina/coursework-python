import numpy as np

# Define slope (m) and y-intercept (b)
m = 2
b = 3

# Generate x values from -5 to 5
x_vals = np.linspace(-5, 5, 11)

# Calculate corresponding y values: y = 2x + 3
y_vals = m * x_vals + b

for x, y in zip(x_vals, y_vals):
    print(f"x = {x:4.1f} | y = {y:4.1f}")