# MATH 1113 Precalculus - Section 2.5: Transformations of Functions
import numpy as np

# Define parent function values for f(x) = x^2
x = np.array([-2, -1, 0, 1, 2])
parent_y = x**2

# Apply transformation parameters: g(x) = a * f(x - h) + k
# Let a = 2 (vertical stretch), h = 3 (shift right), k = 4 (shift up)
a, h, k = 2, 3, 4

transformed_x = x + h
transformed_y = a * parent_y + k

print("Original x:", x)
print("Parent f(x) = x^2:", parent_y)
print("Transformed x (right by 3):", transformed_x)
print("Transformed g(x) = 2(x-3)^2 + 4:", transformed_y)