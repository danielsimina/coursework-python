import numpy as np

# Define polynomial coefficients: P(x) = 1*x^3 - 3*x^2 - 6*x + 8
coefficients = [1, -3, -6, 8]
P = np.poly1d(coefficients)

# 1. Compute all roots using NumPy
roots = np.roots(coefficients)

# 2. Test potential rational zeros (factors of constant 8 / factors of leading coeff 1)
constant_factors = [1, -1, 2, -2, 4, -4, 8, -8]
rational_zeros_found = []

for p in constant_factors:
    if np.polyval(coefficients, p) == 0:
        rational_zeros_found.append(p)

print(f"Polynomial: P(x) = x^3 - 3x^2 - 6x + 8")
print(f"All Computed Roots: {list(roots)}")
print(f"Verified Rational Zeros: {rational_zeros_found}")

# 3. Verify Remainder Theorem / Zero Theorem via direct evaluation
for r in roots:
    val = np.polyval(coefficients, r)
    print(f"P({r.real:.2f}) = {val:.1e} (Confirming zero)")