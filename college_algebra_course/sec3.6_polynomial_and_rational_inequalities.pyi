# MATH 1111 Section 3.6: Polynomial and Rational Inequalities in Python

import numpy as np

print("=== 1. Polynomial Inequality: x^2 - x - 6 > 0 ===")
# Factored form: (x - 3)(x + 2) > 0
# Critical numbers: x = -2, x = 3
roots = [-2, 3]
test_points = [-3, 0, 4]

for pt in test_points:
    val = pt**2 - pt - 6
    satisfies = val > 0
    print(f"Test x = {pt:2d} -> Value = {val:3d} -> Satisfies > 0? {satisfies}")

print("\nSolution Interval: (-inf, -2) U (3, inf)")


print("\n=== 2. Rational Inequality: (x - 1) / (x + 2) <= 0 ===")
# Critical numbers: Numerator root x = 1 (included), Denominator zero x = -2 (excluded)
test_points_rat = [-3, 0, 2]

for pt in test_points_rat:
    if pt == -2:
        print(f"Test x = {pt:2d} -> Undefined (division by zero)")
    else:
      val = (pt - 1) / (pt + 2)
      satisfies = val <= 0
      print(f"Test x = {pt:2d} -> Value = {val:5.2f} -> Satisfies <= 0? {satisfies}")

print("\nSolution Interval: (-2, 1]")