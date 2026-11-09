import math

class CoordinateGeometry:
    @staticmethod
    def distance(p1, p2):
        """
        Calculates the distance between two points p1 = (x1, y1) and p2 = (x2, y2).
        Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        """
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    @staticmethod
    def midpoint(p1, p2):
        """
        Calculates the midpoint between two points p1 = (x1, y1) and p2 = (x2, y2).
        Formula: M = ((x1 + x2)/2, (y1 + y2)/2)
        """
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    @staticmethod
    def linear_intercepts(m, b):
        """
        Given a linear equation in slope-intercept form y = mx + b,
        calculates the x-intercept and y-intercept.
        """
        y_int = (0.0, float(b))
        if m == 0:
            x_int = "None (horizontal line)" if b != 0 else "All real numbers (y = 0)"
        else:
            x_int = (-b / m, 0.0)
        return x_int, y_int


# --- Demonstration of Section 1.1 Concepts ---
if __name__ == "__main__":
    print("=== MATH 1111: College Algebra - Section 1.1 Graphs ===\n")

    # Define two points
    point_a = (1, 2)
    point_b = (4, 6)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}\n")

    # 1. Distance Formula Calculation
    dist = CoordinateGeometry.distance(point_a, point_b)
    print(f"1. Distance Formula:")
    print(f"   Distance between A and B = {dist:.2f} (Exact: sqrt({(4-1)**2 + (6-2)**2}) = sqrt(25) = 5)\n")

    # 2. Midpoint Formula Calculation
    mid = CoordinateGeometry.midpoint(point_a, point_b)
    print(f"2. Midpoint Formula:")
    print(f"   Midpoint between A and B = {mid}\n")

    # 3. Finding Intercepts for y = 2x - 4
    m, b = 2, -4
    x_int, y_int = CoordinateGeometry.linear_intercepts(m, b)
    print(f"3. Intercepts for Line y = {m}x + {b}:")
    print(f"   X-Intercept (set y = 0): {x_int}")
    print(f"   Y-Intercept (set x = 0): {y_int}\n")

    # 4. Generating a Table of Values for a Non-Linear Graph: y = x^2 - 4
    print("4. Generating Coordinates for Graphing y = x^2 - 4:")
    print(f"   {'x':<6} | {'y = x^2 - 4':<12}")
    print("-" * 22)
    for x in range(-3, 4):
        y = x**2 - 4
        print(f"{x:<6} | {y:<12}")