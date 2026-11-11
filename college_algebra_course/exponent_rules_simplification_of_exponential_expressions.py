import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Example 1: Product, Power, and Negative Exponent Rules
# Simplify: (2x^3 y^2)^4 * (3x^(-1) y^5)^2
expr1 = (2 * x**3 * y**2)**4 * (3 * x**(-1) * y**5)**2
simplified1 = sp.simplify(expr1)

# Example 2: Quotient and Negative Exponent Rules
# Simplify: ((x^2 * y^(-3)) / (x^(-4) * y^5))^(-2)
expr2 = ((x**2 * y**(-3)) / (x**(-4) * y**5))**(-2)
simplified2 = sp.simplify(expr2)

print(f"Example 1 Simplified: {simplified1}")
print(f"Example 2 Simplified: {simplified2}")