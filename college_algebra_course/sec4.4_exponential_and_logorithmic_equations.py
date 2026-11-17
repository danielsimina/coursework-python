import sympy as sp

# Define variable
x = sp.Symbol('x')

# 1. Solving an Exponential Equation: 2^(x+1) = 8
eq_exp = sp.Eq(2**(x + 1), 8)
sol_exp = sp.solve(eq_exp, x)
print(f"Solution to 2^(x+1) = 8: x = {sol_exp[0]}")

# 2. Solving a Logarithmic Equation: ln(x) + ln(x - 3) = ln(4)
# Combined: ln(x(x - 3)) = ln(4) => x^2 - 3x = 4 => x^2 - 3x - 4 = 0
eq_log = sp.Eq(sp.log(x) + sp.log(x - 3), sp.log(4))
sol_log = sp.solve(eq_log, x)
print(f"Raw solutions to ln(x) + ln(x-3) = ln(4): {sol_log}")

# Note on domain restriction: x = -1 makes ln(x) undefined, so x = 4 is the only valid solution.