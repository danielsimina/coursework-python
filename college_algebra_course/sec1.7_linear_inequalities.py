import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the variable
x = sp.Symbol('x')

# 1. Solving a standard linear inequality: 3x + 5 < 2x - 1
ineq_standard = 3*x + 5 < 2*x - 1
sol_standard = sp.solve_univariate_inequality(ineq_standard, x, relational=False)

# 2. Solving a compound inequality: -3 <= 2x + 1 < 7
ineq_compound_list = [-3 <= 2*x + 1, 2*x + 1 < 7]
sol_compound = sp.reduce_inequalities(ineq_compound_list, x)

print(f"Standard Inequality (3x + 5 < 2x - 1): {sol_standard}")
print(f"Compound Inequality (-3 <= 2x + 1 < 7): {sol_compound}")

# 3. Visualizing a number line solution for x >= -2 and x < 3
x_vals = np.linspace(-6, 6, 400)
# Condition: -2 <= x < 3
in_interval = (x_vals >= -2) & (x_vals < 3)

plt.figure(figsize=(8, 2))
plt.plot([-6, 6], [0, 0], 'k-', lw=2) # Number line
plt.plot(x_vals[in_interval], np.zeros_sum := np.zeros_like(x_vals[in_interval]), 'r-', lw=6, label='Solution Set: [-2, 3)')
plt.plot(-2, 0, 'ro', markersize=10, markerfacecolor='r') # Closed circle at -2
plt.plot(3, 0, 'ro', markersize=10, markerfacecolor='white', markeredgewidth=2) # Open circle at 3

plt.title('Graphical Representation of Solution Set: $[-2, 3)$')
plt.yticks([])
plt.xlabel('x')
plt.ylim(-1, 1)
plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.grid(False)
plt.show()