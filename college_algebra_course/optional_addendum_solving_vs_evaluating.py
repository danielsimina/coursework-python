import numpy as np

# Define the function f(x) = x^2 - 4
def f(x):
    return x**2 - 4

# 1. EVALUATION: Given x = 3, find f(3)
input_x = 3
output_y = f(input_x)
print(f"--- EVALUATION ---")
print(f"Given input x = {input_x}")
print(f"Computed output f({input_x}) = {output_y}\n")

# 2. SOLVING: Given f(x) = 5, find x
# x^2 - 4 = 5  =>  x^2 = 9  =>  x = +/- 3
target_y = 5
# Using algebraic roots
solutions = np.roots([1, 0, -4 - target_y])
print(f"--- SOLVING ---")
print(f"Given output f(x) = {target_y}")
print(f"Resolved input solutions for x: {solutions}")