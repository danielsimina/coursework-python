import math

print("=== MATH 1113: LESSON 1 PYTHON TOOLKIT ===\n")


# ==========================================
# 1. DISTANCE AND MIDPOINT FORMULAS
# ==========================================
def calculate_distance_and_midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    # Distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Midpoint formula: M = ((x1 + x2)/2, (y1 + y2)/2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return distance, midpoint


# Example: Points (1, 2) and (4, 6)
point_a = (1, 2)
point_b = (4, 6)
dist, mid = calculate_distance_and_midpoint(point_a, point_b)

print("1. Coordinate Geometry:")
print(f"   Points: A{point_a} and B{point_b}")
print(f"   Distance: {dist:.2f}")
print(f"   Midpoint: {mid}\n")


# ==========================================
# 2. EQUATION OF A LINE (Slope-Intercept Form)
# ==========================================
def find_line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return "Vertical line (Undefined slope, x = c)"

    # Slope m = (y2 - y1) / (x2 - x1)
    m = (y2 - y1) / (x2 - x1)
    # Y-intercept b = y1 - m * x1
    b = y1 - m * x1
    return m, b


m, b = find_line_equation(point_a, point_b)
print("2. Equations of Lines:")
print(f"   Slope (m): {m}")
print(f"   Y-Intercept (b): {b}")
print(f"   Line Equation: y = {m}x + {b if b >= 0 else f'- {abs(b)}'}\n")


# ==========================================
# 3. FUNCTIONS, DOMAIN, AND EVALUATION
# ==========================================
# Let's analyze f(x) = sqrt(x - 3)
# Domain requirement: x - 3 >= 0 => x >= 3
def f(x):
    if x < 3:
        return "Undefined (Outside Domain: x < 3)"
    return math.sqrt(x - 3)


test_inputs = [1, 3, 7, 12]
print("3. Function Evaluation & Domain Check for f(x) = sqrt(x - 3):")
print("   Domain restriction: x must be greater than or equal to 3.")
for val in test_inputs:
    result = f(val)
    if isinstance(result, float):
        print(f"   f({val}) = {result:.2f}")
    else:
        print(f"   f({val}) = {result}")