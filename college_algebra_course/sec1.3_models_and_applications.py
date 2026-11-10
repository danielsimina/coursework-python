import sympy as sp

# Define the variable x
x = sp.Symbol('x')

# Define the equation: x^2 - 5x + 6 = 0
equation = sp.Eq(x**2 - 5*x + 6, 0)

# Solve the equation
solutions = sp.solve(equation, x)
print("Solutions:", solutions)  # Output: [2, 3]