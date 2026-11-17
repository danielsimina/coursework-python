import cmath


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Apply the quadratic formula with cmath to handle complex numbers automatically
    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
    print(f"Discriminant (b^2 - 4ac): {discriminant}")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}\n")


# Test cases
solve_quadratic(1, -5, 6)  # Two real rational roots
solve_quadratic(1, -4, 13)  # Complex roots