# MATH 1113 Precalculus - Section 2.6: Quadratic Functions and Their Properties
import numpy as np

# Given quadratic function: f(x) = -2x^2 + 8x + 10
a, b, c = -2, 8, 10

# 1. Calculate the Vertex (h, k)
h = -b / (2 * a)
k = a * (h**2) + b * h + c

# 2. Calculate Discriminant and x-intercepts (roots)
discriminant = b**2 - 4 * a * c
roots = np.roots([a, b, c])

# 3. Identify y-intercept
y_intercept = c

print(f"General Form: f(x) = {a}x^2 + {b}x + {c}")
print(f"Vertex Form:  f(x) = {a}(x - {h:.0f})^2 + {k:.0f}")
print(f"Vertex: ({h:.0f}, {k:.0f}) | Axis of Symmetry: x = {h:.0f}")
print(f"Maximum Value: {k:.0f} (since a = {a} < 0, parabola opens downward)")
print(f"Discriminant (b^2 - 4ac): {discriminant}")
print(f"x-intercepts: {roots} | y-intercept: (0, {y_intercept})")