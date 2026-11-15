import numpy as np

# Define the parent function f(x) = x^2
def parent_f(x):
    return x**2

# Define the transformed function g(x) = 2(x - 3)^2 + 1
def transformed_g(x):
    return 2 * (x - 3)**2 + 1

# Test specific x values
x_vals = np.array([0, 1, 3, 4, 5])

print("Comparing Parent Function f(x) = x^2 vs Transformed g(x) = 2(x - 3)^2 + 1:")
for x in x_vals:
    print(f"x = {x:2d} | f({x}) = {parent_f(x):3d} | g({x}) = {transformed_g(x):3d}")