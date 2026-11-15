import numpy as np

# Define the function in Python using a lambda or def statement
def f(x):
    return 2 * x**2 - 3 * x + 1

# Evaluate the function at specific x values
x_vals = [-2, 0, 1, 3.5]
results = {x: f(x) for x in x_vals}

print("Function evaluations for f(x) = 2x^2 - 3x + 1:")
for x, val in results.items():
    print(f"f({x}) = {val}")