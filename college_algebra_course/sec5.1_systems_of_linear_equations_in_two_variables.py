import numpy as np

# Define coefficient matrix A and constant vector b
A = np.array([
    [2, 3],
    [1, -1]
])

b = np.array([8, 1])

# Solve the linear system
solution = np.linalg.solve(A, b)

print(f"Solution:")
print(f"x = {solution[0]:.2f}")
print(f"y = {solution[1]:.2f}")