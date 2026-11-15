import math


def classify_number(x):
    sets = []

    # Check if the number is an integer (or float representing an integer value)
    is_int = isinstance(x, int) or (isinstance(x, float) and x.is_integer())

    if is_int:
        val = int(x)
        if val > 0:
            sets.append("Natural Numbers (N)")
        if val >= 0:
            sets.append("Whole Numbers (W)")
        sets.append("Integers (Z)")
        sets.append("Rational Numbers (Q)")
    else:
        # Check for common irrationals vs standard floats
        # (In Python, standard floats are treated as rational approximations)
        sets.append("Rational Numbers (Q)")

    sets.append("Real Numbers (R)")
    return sets


# Test a variety of numbers
test_values = [7, 0, -4, 3.75, math.sqrt(2)]

for val in test_values:
    print(f"Number: {str(val):<10} -> Belongs to: {classify_number(val)}")