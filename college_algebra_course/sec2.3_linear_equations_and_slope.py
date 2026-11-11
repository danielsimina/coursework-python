import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
x, y = sp.symbols('x y')

# 1. Calculate slope between two points: (1, 2) and (3, 6)
x1, y1 = 1, 2
x2, y2 = 3, 6
m = (y2 - y1) / (x2 - x1)

# 2. Find the equation of the line using point-slope form: y - y1 = m(x - x1)
# Simplify to slope-intercept form: y = mx + b
eq_point_slope = y - y1 - m * (x - x1)
eq_slope_intercept = sp.solve(eq_point_slope, y)[0]

print(f"Calculated Slope (m): {m}")
print(f"Slope-Intercept Form: y = {eq_slope_intercept}")

# 3. Plotting the line using NumPy and Matplotlib
x_vals = np.linspace(-2, 6, 100)
# Convert SymPy expression to a numerical lambda function
y_func = sp.lambdify(x, eq_slope_intercept, 'numpy')
y_vals = y_func(x_vals)

plt.figure(figsize=(7, 5))
plt.plot(x_vals, y_vals, 'b-', label=f'y = {eq_slope_intercept}')
plt.plot([x1, x2], [y1, y2], 'ro', label='Given Points (1,2) & (3,6)')
plt.title('Linear Equation Graph: $y = 2x$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()