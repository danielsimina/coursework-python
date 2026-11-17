import numpy as np


def analyze_quadratic(a, b, c):
    print(f"Analyzing Quadratic Function: f(x) = {a}x^2 + {b}x + {c}")

    # 1. Direction
    direction = "upward (Minimum)" if a > 0 else "downward (Maximum)"
    print(f"-> Opens: {direction}")

    # 2. Vertex (h, k)
    h = -b / (2 * a)
    k = a * (h ** 2) + b * h + c
    print(f"-> Vertex (h, k): ({h}, {k})")
    print(f"-> Axis of Symmetry: x = {h}")

    # 3. Y-Intercept
    print(f"-> Y-Intercept: (0, {c})")

    # 4. X-Intercepts (Roots)
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + np.sqrt(discriminant)) / (2 * a)
        x2 = (-b - np.sqrt(discriminant)) / (2 * a)
        print(f"-> X-Intercepts: ({x1:.2f}, 0) and ({x2:.2f}, 0)")
    elif discriminant == 0:
        print(f"-> X-Intercept (Vertex touches x-axis): ({h}, 0)")
    else:
        print("-> X-Intercepts: None (Roots are complex)")


# Run analysis on f(x) = 2x^2 - 12x + 10
analyze_quadratic(2, -12, 10)