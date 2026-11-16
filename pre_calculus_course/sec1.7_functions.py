import numpy as np
import matplotlib.pyplot as plt

# 1. Define parent function
def f(x):
    return x**2

# 2. Define transformed function: g(x) = 2 * f(x - 3) - 4
def g(x):
    return 2 * f(x - 3) - 4

# Generate x values
x = np.linspace(-1, 7, 400)
y_parent = f(x)
y_transformed = g(x)

# 3. Analyze key features
vertex = (3.0, -4.0)
y_intercept = g(0) # 2*(0-3)^2 - 4 = 14
x_intercepts = [3 - np.sqrt(2), 3 + np.sqrt(2)] # approx 1.59 and 4.41

print(f"Vertex of g(x): {vertex}")
print(f"Y-intercept: (0, {y_intercept})")
print(f"X-intercepts: {[round(xi, 2) for xi in x_intercepts]}")

# 4. Plotting
plt.figure(figsize=(8, 5))
plt.plot(x, y_parent, label="Parent: f(x) = x^2", color="gray", linestyle="--")
plt.plot(x, y_transformed, label="Transformed: g(x) = 2(x-3)^2 - 4", color="blue", linewidth=2)
plt.scatter([vertex[0]], [vertex[1]], color="red", zorder=5, label=f"Vertex {vertex}")
plt.axhline(0, color="black", linewidth=0.8, linestyle="-")
plt.axvline(0, color="black", linewidth=0.8, linestyle="-")
plt.title("Function Transformations (MATH 1113)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()