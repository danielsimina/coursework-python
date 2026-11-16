import numpy as np

# Define dividend coefficients: 2x^3 - 3x^2 + 4x - 5
dividend = [2, -3, 4, -5]

# Define divisor coefficients: x - 2 -> [1, -2]
divisor = [1, -2]

# Perform polynomial division
quotient, remainder = np.polydiv(dividend, divisor)

# Evaluate f(2) using numpy.polyval to check the Remainder Theorem
c = 2
f_at_c = np.polyval(dividend, c)

print(f"Quotient coefficients: {list(quotient)}")
print(f"Remainder: {remainder[0]}")
print(f"Function value f({c}) evaluated directly: {f_at_c}")