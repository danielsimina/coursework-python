import numpy as np
import matplotlib.pyplot as plt

# Define polynomial coefficients: P(x) = 1*x^3 + 2*x^2 - 4*x - 8
coefficients = [1, 2, -4, -8]
P = np.poly1d(coefficients)

# Generate x values for plotting
x = np.linspace(-3.5, 3.5, 400)
y = P(x)

# Find roots (zeros) of the polynomial
roots = np.roots(coefficients)

# Find derivative to locate critical points (turning points)
P_prime = np.polyder(P)
turning_x = np.roots(P_prime)
turning_y = P(turning_x)

print(f"Polynomial Function:\nP(x) = {P}")
print(f"Roots (X-intercepts): {roots}")
print(f"Turning Points: {list(zip(np.round(turning_x, 2), np.round(turning_y, 2)))}")

# Plotting the polynomial graph
plt.figure(figsize=(9, 6))
plt.plot(x, y, label="P(x) = x^3 + 2x^2 - 4x - 8", color="blue", linewidth=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="-")
plt.axvline(0, color="black", linewidth=0.8, linestyle="-")

# Highlight roots and turning points
plt.scatter(roots.real, [0]*len(roots), color="red", zorder=5, label="Roots / X-intercepts")
plt.scatter(turning_x, turning_y, color="purple", zorder=5, label="Turning Points (Extrema)")

plt.title("MATH 1113: Polynomial Functions and Their Graphs", fontsize=12)
plt.xlabel("x", fontsize=11)
plt.ylabel("P(x)", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()