# MATH 1113 Precalculus - Section 2.3: Modeling with Linear Functions
# Problem: Linear Depreciation of an Asset

# Given data points: (t1, V1) = (0, 24000) and (t2, V2) = (3, 15000)
t1, V1 = 0, 24000
t2, V2 = 3, 15000

# 1. Calculate the rate of change (slope m)
m = (V2 - V1) / (t2 - t1)

# 2. Find the initial value (y-intercept b)
b = V1 - m * t1

print(f"Depreciation Rate (Slope m): ${m:,.2f} per year")
print(f"Initial Purchase Price (y-intercept b): ${b:,.2f}")
print(f"Linear Model: V(t) = {m}t + {b}")

# 3. Predict value after 5 years (t = 5)
t_target = 5
V_target = m * t_target + b
print(f"Predicted Value after {t_target} years: ${V_target:,.2f}")

# 4. Find when the asset value reaches $0 (x-intercept)
t_zero = -b / m
print(f"Time until value reaches $0: {t_zero:.1f} years")